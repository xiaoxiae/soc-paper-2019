import os

os.system("lualatex soc.tex")
os.system("bibtex soc")
os.system("makeglossaries soc")
os.system("lualatex soc.tex")
os.system("lualatex soc.tex")
