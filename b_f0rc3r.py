#!/bin/python 

import base64 
from itertools import *
import sys 
import getopt
from hashlib import *


class colors:
	red = "\033[1;31m"
	white = "\033[1;37m"
	normal = "\033[0;00m"
	blue = "\033[1;34m"
	green = "\033[1;32m"
	lightblue = "\033[0;34m"



def main(argv):
	
	charset = ''
	ch_length = ''
	out_file_name = ''
	prefix = ''
	hash_type = ''
	out_file_flag = 0

	try :
		opts, args = getopt.getopt(argv,"hl:c:o:x:p:",["length=","ofile=","charset=","hash_type=","prefix="])	
	except getopt.GetoptError:
		print colors.red + './b_f0rc3r.py -c <charset> -l <length> [ -o <outputfile> -x <hash_type> -p <prefix>]'
		sys.exit(2)

	for opt, arg in opts:
		if opt == '-h':
			help()
		elif opt in ("-c", "--charset"):
			charset = arg 
		elif opt in ("-l", "--length"):
			ch_length = arg 
		elif opt in ("-o", "--ofile"):
			out_file_name = arg
			out_file_flag = 1
		elif opt in ("-x", "--hash_type"):
			hash_type = arg.lower()
		elif opt in ("-p", "--prefix"):
			prefix = arg 

	try :
		if out_file_flag == 1 :
			file = open(out_file_name , "w")
			
			x = product( charset , repeat=int(ch_length))
			for c in x : 
				if hash_type == "base64":
					file.write(base64.b64encode("{0}{1}".format( prefix ,''.join(c))))
					file.write('\n')
				elif hash_type == "md5":
					file.write(md5("{0}{1}".format( prefix ,''.join(c) )).hexdigest())
					file.write('\n')
				elif hash_type == "sha1":
					file.write(sha1("{0}{1}".format( prefix ,''.join(c) )).hexdigest())
					file.write('\n')
				elif hash_type == "sha256":
					file.write(sha256("{0}{1}".format( prefix ,''.join(c) )).hexdigest())
					file.write('\n')
				elif hash_type == "sha512":
					file.write(sha512("{0}{1}".format( prefix ,''.join(c) )).hexdigest())
					file.write('\n')
				else :
					file.write("{0}{1}\n".format( prefix ,''.join(c)))
			file.close()
			print colors.blue + "[*] Done ... check your file."

		else : 
			x = product( charset , repeat=int(ch_length))
			for c in x : 
				if hash_type == "base64":
					print base64.b64encode("{0}{1}".format( prefix ,''.join(c)))
				elif hash_type == "md5":
					print md5("{0}{1}".format( prefix ,''.join(c))).hexdigest()
				elif hash_type == "sha1":
					print sha1("{0}{1}".format( prefix ,''.join(c))).hexdigest()
				elif hash_type == "sha256":
					print sha256("{0}{1}".format( prefix ,''.join(c))).hexdigest()
				elif hash_type == "sha512":
					print sha512("{0}{1}".format( prefix ,''.join(c))).hexdigest()
				else : 
					print "{0}{1}".format( prefix ,''.join(c))

	except ValueError :
		print "Enter valid input"





def banner():
	signature = colors.red + r""" 
	         ____  _            _        _  __      _       _     _   
		| __ )| | __ _  ___| | __   | |/ /_ __ (_) __ _| |__ | |_ 
		|  _ \| |/ _` |/ __| |/ /   | ' /| '_ \| |/ _` | '_ \| __|
		| |_) | | (_| | (__|   <    | . \| | | | | (_| | | | | |_ 
		|____/|_|\__,_|\___|_|\_\___|_|\_\_| |_|_|\__, |_| |_|\__|
		                        |_____|            |___/           
		""" + "\n"
	print signature 

def help():
	banner()
	print colors.red + './b_f0rc3r.py -c <charset> -l <length> [ -o <outputfile> -x <hash_type> -p <prefix>]\n' 
	print colors.blue + '-h' + colors.normal +'\t' + 'show help menu'
	print colors.blue + '-c' + colors.normal +'\t' + 'charset combination'
	print colors.blue + '-l' + colors.normal +'\t' + 'length of the output (complexity)'
	print colors.blue + '-o' + colors.normal +'\t' + 'output file'
	print colors.blue + '-x' + colors.normal +'\t' + 'hash type : base64 , md5 , sha1 , sha256 , sha512'
	print colors.blue + '-p' + colors.normal +'\t' + 'prefix word\n'
	sys.exit(3) 
	


	
if __name__ == "__main__":
    main(sys.argv[1:])
