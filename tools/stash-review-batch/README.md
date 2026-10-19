# Bitbucket PR reports

Python 3.10+; no third-party packages. Read-only Bitbucket Server/Data Center scanner.

## macOS

```sh
python3 stash_batch.py stats --fresh --workers 4 --months 2026-09 2026-10
python3 stash_batch.py ready --fresh --workers 4 --limit 3
```

## Windows CMD

```bat
stats.cmd --fresh --workers 4 --months 2026-09 2026-10
ready.cmd --fresh --workers 4 --limit 3
```

Both commands prompt for an email/Bitbucket username and hidden personal access token.
Use a personal read token to cover repositories available to your account. A repository token restricts discovery to its repository.
On macOS, system curl uses the OS certificate store. An existing Netscape SSO cookie export can be provided using `--cookie-file`; the newest `cookiefile*.txt` under Downloads/Documents is otherwise detected. Cookie support for these commands currently uses macOS system curl.

## Reports and recovery

- `stats`: formatted `PR-raporu.xlsx` with monthly/unique totals and event details, plus CSV/JSON.
- `ready`: newest open, non-draft PRs by creation date, excluding your own PRs and PRs with your retrievable comment history; formatted `Review-adaylari.xlsx`.
- All accessible repositories and all PR activity pages are scanned. Old PR creation dates do not exclude newer comments.
- `--workers 1` through `--workers 8` bounds simultaneous activity requests; default 4.
- `--fresh` creates an independent report folder without removing previous reports.
- `--resume "reports/stats_<timestamp>"` resumes the saved scan using the same account, mode and months. Successful PRs are reused; failed PRs are retried. Resume keeps the saved discovery snapshot; use fresh to refresh newer changes.
- Checkpoints and live monthly totals are saved in the report folder. Errors mark a report incomplete.
- `--verify-pr "PROJECT/REPO#ID" --expected-comments 1` validates a known commented PR before scanning. A previously verified control PR is configured for the original account/server; other users can provide their own.

Monthly review-only counts are distinct PRs with formal review activity but no comment in that period. They are **not approval counts**. Current event exports group formal actions as Review; raw action labels are not retained in the new checkpoints. Deleted/unavailable history cannot be fully reconstructed. See [detailed usage and counting rules](README.txt).

Tokens and cookie contents are not written to reports/checkpoints. Reports contain internal repository metadata and must not be committed. This directory's ignore rules exclude generated reports, caches, archives and personal launchers.

## Tests

```sh
python3 -m unittest discover -s . -v
```

Legacy `run`, `start`, `status` and `import-legacy` commands remain available with their original dashboard-only scope and options. New interactive commands above scan all accessible repositories.
