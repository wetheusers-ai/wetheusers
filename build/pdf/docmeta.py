"""Single source of truth for document version + date stamps.

Render scripts import this and call meta_html(key); the printed stamp is read
from versions.json so it cannot drift from the registry. When a document changes
substantively, bump its version and set its 'updated' to as_of in versions.json,
then re-render and run check_meta.py.
"""
import json
import pathlib

_DATA = json.loads((pathlib.Path(__file__).resolve().parent / "versions.json").read_text())

_MONTHS = ["January", "February", "March", "April", "May", "June",
           "July", "August", "September", "October", "November", "December"]


def _fmt(iso):
    y, m, d = (int(x) for x in iso.split("-"))
    return f"{_MONTHS[m - 1]} {d}, {y}"


def as_of_iso():
    return _DATA["as_of"]


def as_of_display():
    return _fmt(_DATA["as_of"])


def _doc(key):
    try:
        return _DATA["documents"][key]
    except KeyError:
        raise KeyError(f"docmeta: unknown document key '{key}'. Add it to versions.json.")


def version(key):
    return _doc(key)["version"]


def updated_iso(key):
    return _doc(key)["updated"]


def updated_display(key):
    return _fmt(_doc(key)["updated"])


def title(key):
    return _doc(key).get("title", key)


def documents():
    return _DATA["documents"]


def meta_html(key, label="Working draft", publication=None):
    """HTML for the header meta line, e.g. 'Working draft v0.2 &middot; June 21, 2026'."""
    d = _doc(key)
    s = f'{label} v{d["version"]}&nbsp;&middot;&nbsp;{_fmt(d["updated"])}'
    if publication:
        s += f'&nbsp;&middot;&nbsp;for publication {publication}'
    return s
