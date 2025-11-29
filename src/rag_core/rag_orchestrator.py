from .rag_graph import RAGGraph
class RAGOrchestrator:
    def __init__(self,retriever):
        self.graph=RAGGraph(retriever)
    def run(self,q):
        return self.graph.run(q)
