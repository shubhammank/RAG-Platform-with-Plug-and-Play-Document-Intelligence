from src.rag_core.rag_orchestrator import RAGOrchestrator
from src.retrieval.hybrid_retriever import HybridRetriever
from src.embeddings.embedder import Embedder
from src.embeddings.vector_store import VectorStore

def test_rag_flow():
    emb=Embedder()
    store=VectorStore()
    r=HybridRetriever(emb,store)
    rag=RAGOrchestrator(r)
    out=rag.run("test query")
    assert 'answer' in out
