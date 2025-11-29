import chromadb

class VectorStore:
    def __init__(self):
        self.client=chromadb.Client()
        self.col=self.client.create_collection('docurag')

    def add(self,chunks,emb):
        ids=[c['id'] for c in chunks]
        texts=[c['text'] for c in chunks]
        self.col.add(ids=ids,documents=texts,embeddings=emb)

    def query(self,emb,top_k=3):
        res=self.col.query(query_embeddings=[emb],n_results=top_k)
        return res
