import os

# get the number of characters and words of the text
characters = os.popen('perl texcount.pl -0 -sum -utf8 -char ../soc.tex').read()
words = os.popen('perl texcount.pl -0 -sum -utf8 ../soc.tex').read()

# calculate the number of regular pages
# the number of spaces is approximately the number of words
page_count = (int(characters) + int(words)) / 1800

# print the rounded number of regular pages
print("Normostrany: " + str(round(page_count, 2)))
print("Slova: " + str(words).strip())
print("Znaky: " + str(characters).strip())
