class RAGGraph:
    def __init__(self, retriever):
        from .query_agent import QueryAgent
        from .retrieval_agent import RetrievalAgent
        from .synthesis_agent import SynthesisAgent
        from .guardrail_agent import GuardrailAgent
        self.q=QueryAgent(); self.r=RetrievalAgent()
        self.s=SynthesisAgent(); self.g=GuardrailAgent()
        self.retriever=retriever

    def run(self,query):
        qd=self.q.run(query)
        rd=self.r.run(qd['refined_query'], self.retriever)
        ans=self.s.run(qd['refined_query'], rd)
        return self.g.run(ans)
