"""This module contains the tests for the config module of the dwh_communication sub-app."""
from dwh_communication.dwh_config import config
from pytest import raises


def test_config():
    db_dict = config()
    assert len(db_dict) == 5

    for key in ["host", "port", "database", "user", "password"]:
        assert key in db_dict


def test_config_error(monkeypatch):
    monkeypatch.delenv("PGHOST", raising=True)
    monkeypatch.delenv("PGPORT", raising=True)
    monkeypatch.delenv("PGDATABASE", raising=True)
    monkeypatch.delenv("PGUSER", raising=True)
    monkeypatch.delenv("PGPASSWORD", raising=True)

    with raises(ReferenceError):
        config()
