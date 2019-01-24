import subprocess

subprocess.run("pdflatex soc.tex")
subprocess.run("bibtex soc")
subprocess.run("pdflatex soc.tex")
subprocess.run("pdflatex soc.tex")