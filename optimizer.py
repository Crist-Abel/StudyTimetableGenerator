class Optimizer:
    def __init__(self, analyzer, total_time):
        self.analyzer = analyzer
        self.total_time = total_time

    def run(self):
        subjects = self.analyzer.get_subjects()
        prefs = self.analyzer.get_preferences()
        total = self.total_time

        total_weight = sum(prefs)

        result = {}

        for subject, weight in zip(subjects, prefs):
            allocated = (weight / total_weight) * total
            result[subject] = allocated

        print("\n----- YOUR STUDY TIMETABLE -----")
        for s, hours in result.items():
            print(f"{s}: {hours:.2f} hours")
