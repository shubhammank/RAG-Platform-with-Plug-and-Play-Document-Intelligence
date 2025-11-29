class TextReader:
    def load(self, path):
        items=[]
        with open(path,'r',encoding='utf-8') as f:
            for line in f:
                t=line.strip()
                if t:
                    items.append({'text':t,'type':'paragraph'})
        return items
