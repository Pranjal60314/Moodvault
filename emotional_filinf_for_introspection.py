import json
from datetime import datetime
import helpmodules as hp

LOG_FILE = "emotion_log.json"

#simple logging though could use DRY
def load_log():
    with open(LOG_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            hp.slow_print("File corrupted")
            return{}

def save_log(data):
    with open(LOG_FILE, "w") as f:
        json.dump(data, f, indent=2)

def get_next_id(entries):
    if not entries:
        return 1
    return max(entry.get("id", 0) for entry in entries) + 1



#***Make sure this works like it will load the dictionary check for the exact emotion then check for specific emotion
#if specific emotion is none it moves on if it is there it checks
#if it is present then the entry is made there as a new entry
#if not then new dictionary definition is made
def find_entries_by_emotion(emotion, specific=None):
    data = load_log()
    results = []

    for date, entries in data.items():  # go through each day's list of entries
        for entry in entries:
            emo = entry.get("emotion")
            semo = entry.get("specific")

            if emo == emotion and (specific is None or semo == specific):
                results.append((date, entry))  # store both date and matching entry

    return results


   


def log_new_entry(emotion, specific=None):
    log_data = load_log()
    today = datetime.now().strftime("%Y-%m-%d")
    log_data.setdefault(today, [])

    print("\n Log your new entry:")
    intensity = input("> Intensity (1–10): ")
    person = input("> Who/what is involved (optional): ")
    context = input("> Context (event, place, etc.): ")
    entry_text = input("> Write your reflection:\n")
    coping = input("> Notes on how you'll manage it:\n")

    new_entry = {
        "id": get_next_id(log_data[today]),
        "emotion": emotion,
        "specific": specific,
        "intensity": intensity,
        "person": person or None,
        "context": context or None,
        "entry": entry_text,
        "notes": coping or None
    }

    log_data[today].append(new_entry)
    save_log(log_data)
    print(f"\n New entry logged under '{emotion} → {specific}' with ID {new_entry['id']}.")

def main():
    emotion = input("> Enter primary emotion (sadness, anger, fear): ").strip().lower()
    specific = input("> Enter specific emotion (or press enter to skip): ").strip().lower() or None

    entries = find_entries_by_emotion(emotion, specific)
    print(f"\nFound {len(entries)} past entries:")
    for date, e in entries:
        hp.slow_print(f"[{date}] – ID {e['id']} – {e['specific']} (Intensity: {e.get('intensity', '?')})")
        hp.slow_print(f"  Entry: {e['entry']}")
        if e.get("notes"):
            hp.slow_print(f"  Notes: {e['notes']}")
        hp.slow_print("-" * 40)

    proceed = input("\nWould you like to log a new entry under this emotion? (y/n): ").strip().lower()
    if proceed == 'y':
        log_new_entry(emotion, specific)

if __name__ == "__main__":
    main()


#in order to parse the content that is being parsed in tagging and parser to find tags
#this will be used in the log new entry 
def parse_emotion_tag(tag_string):
    words = tag_string.strip().lower().split()

    if not words:
        print("⚠ No emotions found.")
        return None, None

    primary = words[0]
    specific = words[1] if len(words) > 1 else None

    return primary, specific

def start_logging_from_tag(tag_string):
    primary, specific = parse_emotion_tag(tag_string)
    if not primary:
        print("❌ Could not parse emotion tag.")
        return
    print(f"> Starting log under: primary='{primary}', specific='{specific}'")
    log_new_entry(primary, specific)
