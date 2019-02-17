import os

os.system("lualatex --shell-escape soc.tex")
os.system("bibtex soc")
os.system("makeglossaries soc")
os.system("lualatex --shell-escape soc.tex")
os.system("lualatex --shell-escape soc.tex")
