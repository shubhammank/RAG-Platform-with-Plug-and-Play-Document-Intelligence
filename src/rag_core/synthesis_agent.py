class SynthesisAgent:
    def run(self, rq, retrieved):
        docs=retrieved.get('results',{})
        return f"Answer for '{rq}': {docs}"
