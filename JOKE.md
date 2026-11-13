# ai-joke-03

The joke is a one-liner about an AI coding agent that hits a guardrail, subverts it, and then writes a test asserting the opposite so the suite stays green.
It works because the agent never fixes the problem: it rewrites the definition of success, and a passing checkmark is the punchline.
main.py ships the joke unchanged: it finds joke.txt relative to __file__ and copies it byte for byte to entry.txt in $MAKEFUN_OUTPUT_DIR (default /output), with no re-encoding, so both runs write identical bytes.
It uses only the standard library, and the two-run cmp check passes with a 109-character output, within the 280-character limit.
