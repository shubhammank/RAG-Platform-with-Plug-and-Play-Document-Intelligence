from fastapi import FastAPI, UploadFile, File
from src.ingestion.ingestion_controller import IngestionController
from src.chunking.semantic_chunker import SemanticChunker
from src.chunking.context_builder import ContextBuilder
from src.chunking.metadata_extractor import MetadataExtractor
from src.embeddings.embedder import Embedder
from src.embeddings.vector_store import VectorStore
from src.retrieval.hybrid_retriever import HybridRetriever
from src.retrieval.retrieval_orchestrator import RetrievalOrchestrator
from src.rag_core.rag_orchestrator import RAGOrchestrator

app = FastAPI(title="DocuRAG API")

ingestor = IngestionController()
chunker = SemanticChunker()
ctx_builder = ContextBuilder()
embedder = Embedder()
vstore = VectorStore()
retriever = HybridRetriever(embedder, vstore)
rag = RAGOrchestrator(retriever)

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/upload")
async def upload_doc(file: UploadFile = File(...)):
    path=f"/tmp/{file.filename}"
    with open(path,"wb") as f: f.write(await file.read())
    items=ingestor.load(path)
    enriched=MetadataExtractor.enrich(items,path)
    chunks=chunker.process(enriched)
    chunks=ctx_builder.build(chunks)
    embeddings=embedder.embed([c['text'] for c in chunks])
    vstore.add(chunks,embeddings)
    return {"chunks_indexed":len(chunks)}

@app.get("/search")
def search(q: str, top_k: int = 3):
    result=retriever.retrieve(q,top_k)
    return {"query":q,"results":result}

@app.get("/chat")
def chat(q: str):
    return rag.run(q)
