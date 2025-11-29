from src.embeddings.embedder import Embedder
from src.embeddings.vector_store import VectorStore
from src.retrieval.hybrid_retriever import HybridRetriever

def test_retrieval_basic():
    emb=Embedder()
    store=VectorStore()
    chunks=[{'id':'c1','text':'hello world'}]
    vec=emb.embed(['hello world'])
    store.add(chunks,vec)
    r=HybridRetriever(emb,store)
    res=r.retrieve("hello",top_k=1)
    assert 'documents' in res
