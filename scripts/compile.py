import os

os.chdir("..")

# initial lualatex run
os.system("lualatex --shell-escape soc.tex")

# build bibliography
os.system("bibtex soc")

# build glossaries
os.system("makeglossaries soc")

# run lualatex twice to correctly typeset cross-reference-related text
os.system("lualatex --shell-escape soc.tex")
os.system("lualatex --shell-escape soc.tex")
