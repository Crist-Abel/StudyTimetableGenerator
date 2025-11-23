class Recommender:
    def __init__(self, analyzer):
        self.analyzer = analyzer

    def recommend_topics(self, top_n=3):
        summary = self.analyzer.topic_summary()
        summary = summary.sort_values(by='minutes', ascending=True)
        return summary.head(top_n)
