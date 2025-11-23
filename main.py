from analytics import Analyzer
from optimizer import Optimizer

raw_subjects = input("Enter your subjects separated by commas: ")
subjects = [s.strip() for s in raw_subjects.split(",")]

print("\nSubjects received:", subjects)

preferences = []
print("\nRate each subject from 1–5 (5 = highest priority):")
for s in subjects:
    while True:
        try:
            pref = int(input(f"Priority for {s}: "))
            if 1 <= pref <= 5:
                preferences.append(pref)
                break
            else:
                print("Enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

total_time = float(input("\nHow many hours do you want to study today? "))

analyzer = Analyzer(subjects, preferences)
opt = Optimizer(analyzer, total_time)

result = opt.run()

print("\n=== Timetable ===")
for subj, hrs in result.items():
    print(f"{subj}: {hrs:.2f} hours")
