# u-yuki-kato-fix-human-sleep-funniest-patch-note-f6ad4c27: one line of patch
# notes announcing that human sleep is fixed. The program writes that single
# line to /output/entry.txt.
import os

OUT = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

# Gate: the entry is one line of 1-160 characters.
MAX_CHARS = 160

# The joke in two beats: a terse changelog "Fixed:" setup (sleep now saves
# correctly), then a specific, surprising image for the punchline (waking at
# 3 AM with 47 tabs open in your head). Reads like a real release note,
# no explanation after the laugh.
MESSAGE = "Fixed: sleep now saves correctly; users no longer wake up at 3 AM with 47 tabs open in their head."


def main():
    assert 1 <= len(MESSAGE) <= MAX_CHARS, f"message is {len(MESSAGE)} chars, must be 1-160"
    assert MESSAGE.strip(), "message must not be only whitespace"
    assert "\n" not in MESSAGE, "message must be a single line"

    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()
