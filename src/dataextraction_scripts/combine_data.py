import sys
import string
import os
import re
import sys
import pickle
from itertools import *

def make_files(dir_list, q_file, sum_file, cont_file):

	files = ["content", "summary", "query"]

	count = 0 
	for d in dir_list:
		print d
		c = os.path.join( d, files[0])
		s = os.path.join( d, files[1])
		q = os.path.join( d, files[2])

		f_q = open(q, "r")
		query_sent = f_q.read().splitlines()[0]

		f_c = open(c, "r")
		f_s = open(s, "r")

		for l1, l2 in izip(f_c, f_s):
			if not(l1.isspace() or l2.isspace()):		
				count = count + 1
				print count
				q_file.write(query_sent + "\n")
				sum_file.write(l2 )
				cont_file.write(l1)


def make_files_all_dicts(dir_lists, name):

	q_file = open(name + "_query", "w")
	c_file = open(name + "_content", "w")
	s_file = open(name + "_summary", "w")

	for d in dir_lists:

		make_files(d, q_file, s_file, c_file)


	q_file.close()
	c_file.close()
	s_file.close()

def main():

	train = pickle.load(open("train.pkl","r"))
	test = pickle.load(open("testdata.pkl","r"))
	valid =  pickle.load(open("valid.pkl","r"))

	make_files_all_dicts([train.keys()], "train")
	make_files_all_dicts([valid.keys()], "valid")
	make_files_all_dicts([test.keys()],"test")

if __name__ == '__main__':
	main()
