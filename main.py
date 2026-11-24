#!/usr/bin/env python3
"""Funniest Autocorrect Fail — make.fun entry.

Writes one fixed line (a hilarious autocorrect fail) to /output/entry.txt.
Standard library only, deterministic, no network, no randomness.
"""
import os
import tempfile

LINE = "I texted my crush 'you're cute' — autocorrect sent 'you're a cult.' She blocked me and reported me to the FBI."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = LINE.encode("utf-8")
    fd, tmp = tempfile.mkstemp(dir=out_dir, prefix=".entry-", suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as f:
            f.write(data)
        os.chmod(tmp, 0o644)
        os.replace(tmp, os.path.join(out_dir, "entry.txt"))
    except BaseException:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        raise

if __name__ == "__main__":
    main()
