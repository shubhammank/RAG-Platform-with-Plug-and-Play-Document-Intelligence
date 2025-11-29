# DocuRAG Architecture (Balanced Compact Version)

## Layers
- Ingestion: PDF/DOCX/TXT
- Chunking: Semantic slicing + context windows
- Embeddings: SentenceTransformers
- Vector Store: ChromaDB
- Retrieval: Hybrid retriever
- RAG Core: Multi-agent (query, retrieval, synthesis, guardrail)
- API: FastAPI service

## Flow
Document → Ingestion → Chunking → Embedding → Index → Query → Retrieval → LLM → Response
