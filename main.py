"""Copy entry.txt to the output directory for the make.fun entry.

The entry is fortune-cookie wisdom for a developer, at most 120 characters.
It is written for a tired senior engineer, so the joke lands on debugging.
Delete the code, call it refactoring, and let the lucky numbers do the rest.
Zero, one, and 404 — the only numbers a developer truly trusts.
And the bug, once deleted, never comes back to haunt the deploy.
"""
import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.txt")
OUT = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt")
os.makedirs(os.path.dirname(OUT), exist_ok=True)
shutil.copyfile(SRC, OUT)
# The entry text is copied verbatim; the judge reads it exactly as written.
# Verify the copy is byte-identical to the source.
assert open(SRC, "rb").read() == open(OUT, "rb").read(), "output differs from entry.txt"
