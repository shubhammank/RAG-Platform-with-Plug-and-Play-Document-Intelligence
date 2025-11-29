import fitz
class PDFReader:
    def load(self,path):
        doc=fitz.open(path)
        blocks=[]
        for page in doc:
            text=page.get_text().strip()
            for line in text.split('\n'):
                if line.strip():
                    blocks.append({'text':line.strip(),'type':'paragraph'})
        return blocks
