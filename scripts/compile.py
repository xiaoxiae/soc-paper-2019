import os

os.chdir("..")

# clean-up files from the previous compilation
for file in [f for f in os.listdir(".") if os.path.isfile(f)]:
    if file.startswith("soc") and not file.endswith(("tex", "bib")):
        os.remove(file)

# initial lualatex run
os.system("lualatex --shell-escape soc.tex")

# build bibliography
os.system("bibtex soc")

# build glossaries
os.system("makeglossaries soc")

# run lualatex twice to correctly typeset cross-reference-related text
os.system("lualatex --shell-escape soc.tex")
os.system("lualatex --shell-escape soc.tex")
