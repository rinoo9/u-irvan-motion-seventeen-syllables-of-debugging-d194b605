[![make.fun](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Rank](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rinoo9/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rank.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)
[![Reward](https://make.fun/badge/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/rinoo9/u-irvan-motion-seventeen-syllables-of-debugging-d194b605/reward.svg)](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605)

# Seventeen Syllables of Debugging

One haiku about debugging, in the classic 5-7-5 syllable shape, written for the
[make.fun bounty](https://make.fun/bounty/u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

> Cursor blinks at three
> the log swears the tests all passed
> I never ran them

A cursor blinking at 3 a.m., a log line that insists everything passed — and the
turn in the last line: the tests never ran at all, because I never ran them.
Seventeen syllables, 75 characters, every word earning its place.

## How to run

```sh
python3 main.py
```

This writes the haiku to `/output/entry.txt` (creating `/output` if needed).
The program is fully deterministic — no network, no randomness, no environment
input — so repeated runs produce byte-identical output.
