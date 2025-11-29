import os
from .pdf_reader import PDFReader
from .docx_reader import DOCXReader
from .text_reader import TextReader

class IngestionController:
    def __init__(self):
        self.pdf=PDFReader()
        self.docx=DOCXReader()
        self.txt=TextReader()

    def load(self,path):
        ext=os.path.splitext(path)[1].lower()
        if ext=='.pdf': return self.pdf.load(path)
        if ext=='.docx': return self.docx.load(path)
        return self.txt.load(path)
