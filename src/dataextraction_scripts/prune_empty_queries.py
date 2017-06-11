import os
import sys
import shutil
def get_content(filename, f1):

	with open(filename, "r") as f:
		i = f.read()
		f1.write(i + "\n")


f1 = open("wq","w")

x = sys.argv[1]

with open(x, "r") as f:
	for lines in f:
		get_content(lines.strip(), f1)

f1 = open("qu", "r")
f2 = open("wq", "r")

for (l1, l2) in zip(f1,f2):
	if ('subquestion here' in l2) or ('sub question here' in l2) or ('Videos' in l2) or ('Pro and con videos' in l2) or ('argument #' in l2.lower()):
		shutil.rmtree(l1.strip()[:-6])

