# The Painfully Honest Out-of-Office

[![make.fun](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![Rank](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/ahmed1813544/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/rank.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)
[![Reward](https://make.fun/badge/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/ahmed1813544/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b/reward.svg)](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b)

A [make.fun](https://make.fun/bounty/u-po-pu-the-painfully-honest-out-of-office-63e7ca0b) entry for **The Painfully Honest Out-of-Office** — one brutally honest but still polite out-of-office auto-reply, written by a small stdlib-only Python program.

## What it does

`main.py` writes a single out-of-office email auto-reply — one sentence, 154 characters — to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). It is painfully honest about the sender's inbox and enthusiasm, while staying warm and professional enough that a manager would let it stand.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

Requires only Python 3 (standard library only, no third-party packages).
