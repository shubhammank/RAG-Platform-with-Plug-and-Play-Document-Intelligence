class ContextBuilder:
    def build(self,chunks):
        for i,c in enumerate(chunks):
            c['context_before']=chunks[i-1]['text'] if i>0 else ''
            c['context_after']=chunks[i+1]['text'] if i<len(chunks)-1 else ''
        return chunks
