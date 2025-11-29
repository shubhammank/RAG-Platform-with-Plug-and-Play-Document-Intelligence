from src.ingestion.text_reader import TextReader

def test_text_ingestion():
    path='/mnt/data/sample_test.txt'
    with open(path,'w') as f: f.write("Hello World")
    reader=TextReader()
    out=reader.load(path)
    assert len(out)==1
    assert out[0]['text']=="Hello World"
