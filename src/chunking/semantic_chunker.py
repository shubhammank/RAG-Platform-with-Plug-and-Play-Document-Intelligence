class SemanticChunker:
    def __init__(self, max_tokens=120):
        self.max_tokens=max_tokens

    def split(self,text):
        words=text.split()
        chunks=[]
        for i in range(0,len(words),self.max_tokens):
            chunks.append(' '.join(words[i:i+self.max_tokens]))
        return chunks

    def process(self,items):
        out=[]
        for it in items:
            parts=self.split(it['text'])
            for idx,p in enumerate(parts):
                out.append({'id':f'{it.get("type","chunk")}_{idx}','text':p})
        return out
