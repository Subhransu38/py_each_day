"""
Challenge: Daily Learning Journal Logger

Build a Python script that allows you to maintain a daily learning journal. Each entry will be saved into a `.txt` file along with a timestamp.

Your program should:
1. Ask the user what they learned today.
2. Add the entry to a file called `learning_journal.txt`.
3. Each entry should include the date and time it was written.
4. The journal should **append** new entries rather than overwrite.

Bonus:
- Add a optional rating (1-5) for how prductive the day was.
- Show a confirmation message after saving the entry.
- Make sure the format is clean and easy to read when opening the file.

Example:
🗓️2026-09-09 - 11.29 AM
Today I learned about how list comprehensions work in Python!
Productivity Rating: 4/5
"""

from datetime import datetime

timestamp = datetime.now().strftime("%Y-%m-%d - %I:%M %p")
entry = input("What have you learned today? ").strip()
rating = input("What is the Productivity rating for today? (1 to 5) / optional")

journal_entry = f"\n 🗓️ {timestamp}\n{entry}"
if rating:
    journal_entry += f"\n Productivity Rating: {rating}\n"
journal_entry += f"\n{"_"*40}"

with open("learning_journal.txt", "a", encoding="utf-8") as file:
    file.write(journal_entry)

print("\nYour journal entry has been saved to leanrning_journal.txt file")
