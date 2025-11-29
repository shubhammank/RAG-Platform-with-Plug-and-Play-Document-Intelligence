from .query_rewriter import QueryRewriter
from .intent_classifier import IntentClassifier

class RetrievalOrchestrator:
    def __init__(self,retriever):
        self.rewriter=QueryRewriter()
        self.intent=IntentClassifier()
        self.retriever=retriever

    def run(self,q,top_k=3):
        rq=self.rewriter.rewrite(q)
        intent=self.intent.classify(rq)
        docs=self.retriever.retrieve(rq,top_k)
        return {'intent':intent,'rewritten_query':rq,'results':docs}
