import hashlib
class DeltaManager:
    def __init__(self):
        self.cache={}
    def _hash(self,p):
        return hashlib.sha256(open(p,'rb').read()).hexdigest()
    def needs_reindex(self,p):
        h=self._hash(p)
        old=self.cache.get(p)
        self.cache[p]=h
        return h!=old
