import os

# this makes it so that the name of the tex file isn't hardcoded
file = [f for f in os.listdir(".") if f.endswith(".tex")][0]

# get the number of characters and words of the text
characters = os.popen('perl texcount.pl -0 -sum -utf8 -char ../' + file).read()
words = os.popen('perl texcount.pl -0 -sum -utf8 ../' + file).read()

# the number of spaces is approximately the number of words
page_count = (int(characters) + int(words)) / 1800

print("Normostrany: " + str(round(page_count, 2)))
print("Slova: " + str(words).strip())
print("Znaky: " + str(characters).strip())
