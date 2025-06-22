# DataIngestion.py

The output shows __Warnings__ from the PDF parse being used by `PyPDFLoader` as : __Ignoring wrong pointing object 18 0 (offset 0)__

That means there `structural issues` or ` irregularities` in PDF content.

__Solution__: There are several solutions to achieve the issue.
1. Using different `Loaders` such as __PDFMinerLoader__ or __PyMUPyMuPDFLoader__ etc. 
2. Repair the PDF file (Clean or re-export the PDF): There are some online tools available to `repair` or `clean` the PDF files.

- [ILovePDF](https://www.ilovepdf.com/repair-pdf)
- [PDF24 Tools](https://tools.pdf24.org/en/repair-pdf)
