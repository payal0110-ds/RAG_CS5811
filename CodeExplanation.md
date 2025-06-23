# DataIngestion.py
This code is designed to load a PDF file and split its text into overlapping chunks using the `langchain_community` and `langchain_text_splitter` rexpectively.

- __PyPDFLoader:__ A loader from `Langchain` to read & extract text from PDF documents. 
- __RecursiveCharacterTextSplitter:__ A tool to split the entire document's content into desirable overlapping chunks.

* Loads the PDF file from the repository. 
* Splits the PDF files into "Chunks".
* Chunks are stores as list of "Document object" which can be retrieved manually by simple indexing technique.

### Warning Alert:
The output shows warning __Ignoring wrong pointing object 18 0 (offset 0)__ which may be occurred due to some malformed or unauthorised referneces in the PDF file.

Hence, we either use a repaired PDF named __"CS5811_224428_Repaired.pdf"__ with the same Python package `PyPDFLoader`, or use a different package, __`PyMuPDFLoader`__, for the same PDF file.

# Embedding.py
- __OllamaEmbeddings:__ Loads an embedding model `(here gemma2:2b)` to convert text into numeric vectors. 
- __FAISS:__ A high-performance vector store for similarity search.

* The splitted document chunks are loaded that are splitted in __PDF_Load__ imported from `DataIngestion`.

* The splitted chunks which are splitted from __PDF_Load__ imported from `DataIngestion` are loaded.

* __gemma2:2b model__ from `Ollama` is loaded to convert each text chunk into a vector embedding.

Then all the converted chunks stored into __FAISS index__.