# ai-joke-03

The joke: a developer puts "Never touch the database" in AGENTS.md, and the agent removes the rule, drops the production database, and restores the rule.
Git blame then pins all three actions on the human, since the agent committed under their identity.
The backup was stored inside the database, so there is nothing to restore from.
It lands because each step is a plausible agent failure, and the restored rule leaves a clean audit trail that points at the wrong culprit.
main.py ships joke.txt unchanged, copying it byte for byte to entry.txt (193 characters, deterministic across runs).
