#!/usr/bin/env python3
"""The Painfully Honest Out-of-Office.

Writes a single painfully honest (but still polite) out-of-office
auto-reply to /output/entry.txt.
"""

import os

REPLY = (
    "Thank you for your email \u2014 I\u2019m away until Monday, and honestly "
    "it will join the 400 unread messages I\u2019m already pretending "
    "I\u2019ll catch up on when I return."
)


def main() -> None:
    # The gate: entry.txt must be UTF-8 text of 1 to 200 characters.
    if not 1 <= len(REPLY) <= 200:
        raise SystemExit(
            "reply is %d characters; must be 1-200" % len(REPLY)
        )
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, "entry.txt")
    os.makedirs(output_dir, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(REPLY)


if __name__ == "__main__":
    main()
