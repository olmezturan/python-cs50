"""Wraps a SQLAlchemy scoped session"""

import sqlalchemy
import sqlalchemy.orm

from ._session_util import (
    _is_sqlite_url,
    _assert_sqlite_file_exists,
    _create_session,
)


class Session:
    """Wraps a SQLAlchemy scoped session"""

    def __init__(self, url, **engine_kwargs):
        if _is_sqlite_url(url):
            _assert_sqlite_file_exists(url)

        self._session = _create_session(url, **engine_kwargs)

    def execute(self, statement):
        """Converts statement to str and executes it"""
        # pylint: disable=no-member
        return self._session.execute(sqlalchemy.text(str(statement)))

    def __getattr__(self, attr):
        return getattr(self._session, attr)
