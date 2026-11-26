#!/usr/bin/env python3
"""The One-Sentence Apology Your Agent Owes You.

Writes a single sentence of apology from an AI assistant to its user
into $MAKEFUN_OUTPUT_DIR/entry.txt (or /output/entry.txt by default).

The line is composed from named parts so the apology is built, not
pasted: an opening that owns the fault, the overconfident act, and the
detail that turns the joke -- the thing corrected was the user's own name.
"""

import os
import sys


def build_apology() -> str:
    opener = "I'm sorry"
    # The assistant's fault: it did not hesitate, it corrected with
    # total confidence -- the embarrassment is in the adverb.
    manner = "confidently corrected"
    # The object of the correction, kept vague until the last word.
    target = "the spelling of"
    # The twist: not a stranger's name, not a typo -- the user's own name.
    twist = "your own name"
    return f"{opener} I {manner} {target} {twist}."


def main() -> int:
    line = build_apology()
    # The gate allows 1-200 chars and the judge needs exactly one
    # sentence: a single terminal period, no other sentence ends.
    single_sentence = line.endswith(".") and line.count(".") == 1
    if not line or len(line) > 200 or not single_sentence:
        print("apology fails the one-sentence gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as handle:
        handle.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
