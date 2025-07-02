# MoodVault

MoodVault is a spin-off from LifeOS focused entirely on emotional introspection. It allows you to log, categorize, and reflect on your emotions over time. Designed to act like a personal therapist in your terminal, it builds emotional awareness and resilience one entry at a time.

## Features

- Log emotional events using primary and specific feelings
- Auto-tag entries with intensity, people, context, and coping notes
- Retrieve past logs by emotion and date
- Structure daily emotional reflections like a digital journal
- CLI interface with slow-print for introspective pacing
- JSON-based local storage for full control and privacy

## How It Works

1. Run the script
2. Choose to review past logs or enter a new emotion
3. Log details like intensity, cause, and coping mechanisms
4. MoodVault saves it all into structured files for future analysis

## Example

```bash
> Enter primary emotion: sadness
> Enter specific emotion: loneliness
> Intensity (1–10): 7
> Who/what is involved: college move
> Context: late night in hostel
> Write your reflection:
Missing familiarity.
> Notes on how you'll manage it:
Daily check-ins and more calls home.
Future Additions
NLP-based emotion detection from free-text logs

Visual mood charts over time

Integration with LifeOS and voice assistant

Installation
bash
Copy
Edit
git clone https://github.com/yourusername/MoodVault.git
cd MoodVault
python emotional_filing_for_introspection.py
Dependencies
Python 3.8+

json (standard)

datetime (standard)

License
While this repository is open to view, it is not open-source licensed.
If you'd like to use or build upon it, please reach out — I’d love to hear how you're using it!
