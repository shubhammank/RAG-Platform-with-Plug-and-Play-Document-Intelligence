from src.chunking.semantic_chunker import SemanticChunker

def test_chunking():
    c=SemanticChunker(max_tokens=2)
    items=[{'text':"one two three four"}]
    out=c.process(items)
    assert len(out)>=2
