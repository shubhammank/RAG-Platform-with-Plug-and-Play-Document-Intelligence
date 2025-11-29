class IntentClassifier:
    def classify(self,q):
        q=q.lower()
        if '?' in q: return 'question_answering'
        if 'find' in q: return 'search'
        return 'general'
