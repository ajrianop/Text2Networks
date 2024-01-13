import json
import fitz  # imports the pymupdf library
from models import Pagina, Libro

PDF_PATH = "data/raw/proyecto-ley-reforma-salud-msps.pdf"
JSON_EXTRACTED_PATH = "data/pre_processed/proyecto-ley-reforma-salud-msps.json"

doc = fitz.open(PDF_PATH)  # open a document

book: Libro = Libro(
    nombre="Proyecto Ley Reforma Salud Colombia",
    numero_paginas=doc.page_count)

book.contenido = []
for page in doc:  # iterate the document pages
    print("Processing page: ", page.number)
    book.contenido.append(
        Pagina(
            contenido=page.get_text(),
            n_pagina=page.number
            )
        )

with open(JSON_EXTRACTED_PATH, "w", encoding='utf-8') as f:
    json.dump(book.json(), f)