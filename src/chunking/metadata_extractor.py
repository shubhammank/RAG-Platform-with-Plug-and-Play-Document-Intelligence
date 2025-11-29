class MetadataExtractor:
    @staticmethod
    def enrich(items,path):
        for i,it in enumerate(items):
            it['metadata']={'source':path,'block_id':i}
        return items
