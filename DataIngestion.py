# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def PDF_Load(path):
#     loader=PyPDFLoader(path)
#     docs=loader.load()
#     text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

#     text=text_splitter.split_documents(docs)
#     return text

# result=PDF_Load('Data/CS5811_224428.pdf')
# print(result[1])

''' CODE 1: REPAIRED PDF FILE'''
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_text_splitters import RecursiveCharacterTextSplitter

# def PDF_Load(path):
#     loader=PyPDFLoader(path)
#     docs=loader.load()
#     text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

#     text=text_splitter.split_documents(docs)
#     return text

# result=PDF_Load('Data/CS5811_224428_Repaired.pdf')
# print(result[5])

''' CODE 2: USING DIFFERENT LOADER - PyMUPyMuPDFLoader '''

from langchain_community.document_loaders import PyMuPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def PDF_Load(path):
    loader=PyMuPDFLoader(path)
    docs=loader.load()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    text=text_splitter.split_documents(docs)
    return text

result=PDF_Load('Data/CS5811_224428.pdf')
print(result[5])