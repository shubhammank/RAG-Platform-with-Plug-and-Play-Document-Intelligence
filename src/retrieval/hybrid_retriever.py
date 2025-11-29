class HybridRetriever:
    def __init__(self, embedder, store):
        self.embedder=embedder
        self.store=store

    def retrieve(self,q, top_k=3):
        vec=self.embedder.embed([q])[0]
        res=self.store.query(vec, top_k=top_k)
        return res
