import io
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

import pr_tools
import stash_batch
from bitbucket_config import validate_base_url


class ConfigurationTests(unittest.TestCase):
    def test_url_validation_and_normalization(self):
        self.assertEqual(validate_base_url(' https://bitbucket.example.com:8443/git/ '),
                         'https://bitbucket.example.com:8443/git')
        for value in (None, '', '  ', 'http://example.com', 'https://',
                      'https://user:pass@example.com', 'https://example.com?x=1',
                      'https://example.com/#fragment', 'https://example.com:bad',
                      'https://exa mple.com', 'https://example.com/\npath',
                      'https://example.com\\path'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                validate_base_url(value)

    def test_interactive_commands_require_url_before_credentials(self):
        for mode in ('stats', 'ready'):
            with self.subTest(mode=mode), patch.dict(os.environ, {}, clear=True), \
                 patch('builtins.input') as login, patch.object(pr_tools.getpass, 'getpass') as token, \
                 patch.object(pr_tools, 'Client') as client, redirect_stderr(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    pr_tools.main([mode])
                self.assertEqual(error.exception.code, 2)
                login.assert_not_called()
                token.assert_not_called()
                client.assert_not_called()

    def test_interactive_environment_and_cli_precedence(self):
        for mode in ('stats', 'ready'):
            for cli, expected in (([], 'https://env.example.com/git'),
                                  (['--base-url', 'https://cli.example.com/git/'],
                                   'https://cli.example.com/git')):
                with self.subTest(mode=mode, cli=cli), \
                     patch.dict(os.environ, {'BITBUCKET_BASE_URL': 'https://env.example.com/git'}), \
                     patch('builtins.input', return_value='user'), \
                     patch.object(pr_tools.getpass, 'getpass', return_value='dummy'), \
                     patch.object(pr_tools, 'Client', side_effect=RuntimeError('stop before network')) as client:
                    with self.assertRaisesRegex(RuntimeError, 'stop before network'):
                        pr_tools.main([mode, *cli])
                    self.assertEqual(client.call_args.args[0], expected)

    def test_invalid_url_fails_before_prompt(self):
        with patch('builtins.input') as login, redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                pr_tools.main(['stats', '--base-url', 'http://example.com'])
            login.assert_not_called()

    def test_expected_comments_requires_explicit_pr(self):
        with patch('builtins.input') as login, redirect_stderr(io.StringIO()):
            with self.assertRaises(SystemExit):
                pr_tools.main(['stats', '--base-url', 'https://example.com', '--expected-comments', '3'])
            login.assert_not_called()

    def test_legacy_commands_require_url_before_side_effects(self):
        for command in ('run', 'start', 'import-legacy'):
            with self.subTest(command=command), tempfile.TemporaryDirectory() as folder, \
                 patch.dict(os.environ, {}, clear=True), redirect_stderr(io.StringIO()), \
                 patch.object(sys, 'argv', ['stash_batch.py', command, '--user', 'user',
                                          '--output', str(Path(folder)/'new')]), \
                 patch.object(stash_batch, 'run') as run, \
                 patch.object(stash_batch.subprocess, 'Popen') as start:
                with self.assertRaises(SystemExit) as error:
                    stash_batch.main()
                self.assertEqual(error.exception.code, 2)
                run.assert_not_called()
                start.assert_not_called()
                self.assertFalse((Path(folder)/'new').exists())

    def test_legacy_run_environment_and_cli_precedence(self):
        for cli, expected in (([], 'https://env.example.com/git'),
                              (['--base-url', 'https://cli.example.com/git/'],
                               'https://cli.example.com/git')):
            with self.subTest(cli=cli), patch.dict(os.environ, {'BITBUCKET_BASE_URL': 'https://env.example.com/git'}), \
                 patch.object(sys, 'argv', ['stash_batch.py', 'run', '--user', 'user', '--output', 'reports', *cli]), \
                 patch.object(stash_batch, 'run', return_value=0) as run:
                self.assertEqual(stash_batch.main(), 0)
                self.assertEqual(run.call_args.args[0].base_url, expected)

    def test_status_stays_offline_without_url(self):
        with tempfile.TemporaryDirectory() as folder, patch.dict(os.environ, {}, clear=True), \
             patch.object(sys, 'argv', ['stash_batch.py', 'status', '--user', 'user', '--output', folder]), \
             redirect_stdout(io.StringIO()):
            self.assertEqual(stash_batch.main(), 0)

    def test_explicit_control_pr_uses_requested_minimum(self):
        user = {'id': 1, 'name': 'user'}
        client = unittest.mock.Mock()
        client.pages.return_value = iter([
            {'comment': {'id': 1, 'author': user, 'createdDate': 1000}},
            {'comment': {'id': 2, 'author': user, 'createdDate': 2000}},
        ])
        with redirect_stdout(io.StringIO()):
            result = pr_tools.verification(client, user, 'DEMO/sample#42', 2)
        self.assertEqual(result['found_comments'], 2)
        client.pages.assert_called_once_with('projects/DEMO/repos/sample/pull-requests/42/activities')
        client.pages.return_value = iter([])
        with self.assertRaises(pr_tools.ScanError):
            pr_tools.verification(client, user, 'DEMO/sample#42', 2)


if __name__ == '__main__':
    unittest.main()
