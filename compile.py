import os

os.system("pdflatex soc.tex")
os.system("bibtex soc")
os.system("pdflatex soc.tex")
os.system("pdflatex soc.tex")
