"""Shared, explicit Bitbucket server configuration for both command-line tools."""
import os
from urllib.parse import urlsplit


def add_base_url_argument(parser):
    parser.add_argument(
        "--base-url", default=os.environ.get("BITBUCKET_BASE_URL"),
        help="HTTPS Bitbucket application URL (default: BITBUCKET_BASE_URL)",
    )


def validate_base_url(value):
    if not value or not value.strip():
        raise ValueError("Set --base-url or BITBUCKET_BASE_URL.")
    value = value.strip()
    try:
        parts = urlsplit(value)
        _ = parts.port  # Reject malformed/out-of-range ports.
        valid = (parts.scheme == "https" and parts.hostname and
                 parts.username is None and parts.password is None and
                 not parts.query and not parts.fragment and
                 not any(c.isspace() or ord(c) < 32 for c in value) and
                 "\\" not in value)
    except ValueError:
        valid = False
    if not valid:
        raise ValueError("--base-url must be an HTTPS application URL without credentials/query/fragment.")
    return value.rstrip("/")
