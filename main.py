import os

LINE = "I cannot make the meeting - my calendar and I are no longer on speaking terms after what it did last Tuesday."

LIMIT = 200
if len(LINE) != 109 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 109 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")

# Blame the calendar, not the person: the excuse writes itself.
