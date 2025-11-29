from docx import Document
class DOCXReader:
    def load(self,path):
        doc=Document(path)
        return [{'text':p.text,'type':'paragraph'} for p in doc.paragraphs if p.text.strip()]
