import subprocess
import urllib.request
import requests
import os 
import time
import math


def executeSAT():
	os.chdir("/Users/Jadon/desktop/ECE108/Project 2")
	fileVar = input("Filename: ")
	os.system("gcc dimacs_reader.c {} -o D".format(fileVar))
	auto_input = 'y'
	file_format = '.cnf'
	satisfiable = unsatisfiable = tautology = 0
	too_long = []
	total_time = 0
	# auto_input = input("auto input? [yn] ")
	# file_format = input("file format: ")

	if auto_input == 'y':
		for i in range(0, 100):
			try:
				cmd = "./D sample{0}{1}".format(i, file_format)
				file_time_start = time.time()
				os.system(cmd)
				file_time_end = time.time()
				total_time += file_time_end - file_time_start
				if file_time_end - file_time_start > 1:
					print("sample{0}{1} took too long to solve: {2}".format(i, file_format, file_time_end - file_time_start) + " seconds\n")
					too_long.append("sample{0}{1}".format(i, file_format))
				file_time_start = file_time_end = 0

				output = subprocess.Popen(cmd, shell = True, stdout = subprocess.PIPE).communicate()[0]
				if "unsatisfiable".encode() in output:
					unsatisfiable += 1
				elif "satisfiable".encode() in output:
					satisfiable += 1
				elif "tautology".encode() in output:
					tautology += 1
			except:
				print("ERROR! Terminating...")
				return None;
	else:
		cmd = input("Input to terminal: ")
		while cmd != 'q':
			os.system(cmd)
			cmd = input("Input to terminal: ")

	print("-" * 30)
	print("USER TIME: " + str(round(total_time, 3)) + " seconds")
	print("-" * 30)
	print("Satisfiable:   {0}/100\nUnsatisfiable: {1}/100\nTautology:     {2}/100\nTBF: {3}".format(satisfiable, unsatisfiable, tautology, too_long))
	print("-" * 30 + "\n")
			
	return None;


def downloadSamples():
	for i in range(0, 100):
		URL = "https://ecesvn.uwaterloo.ca/courses/ece108/Dimacs/samples/sample" + str(i) + ".cnf"

		login_info = dict(login = "****", password = "*****")
		web_responses = requests.post(URL, data = login_info)
		print(web_responses.text)

		CNF_file = urllib.request.urlretrieve(URL, "sample" + str(i) + ".cnf")

	return None;


def test():
	print("-" * 30)
	print("STARTING NOW")
	print("-" * 30)

	return None;


## DANGER: RUN ONLY AT WILL
'''
def renameCNFFiles():
	target_dir = "/Users/Jadon/desktop/HyperDownloader/3_11_2018"
	os.chdir(target_dir)
	print("Accessing " + target_dir)
	confirm = input("Are you sure? [yn] ")
	if confirm != 'y':
		return None;
	else:
		password = input("Password: ")
		if password != "108Confirm":
			return None;

	print("Wait several seconds... press control + C (^C) on terminal to cancel the request")
	time.sleep(10)

	for file_name in os.listdir(target_dir):
		if "sample" not in file_name:
			print("TERMINATE NOW! WRONG DIRECTORY.")
			return None;
		elif "sample" in file_name and ".cnf" in file_name:
			num = ""
			skipNext = False;
			for char in file_name:
				if char.isdigit() and not skipNext:
					num += char
					skipNext = False;
				if char == '(':
					skipNext = True;
			os.rename(file_name, "sample{0}.cnf".format(num))

	return None;
'''
## DANGER: RUN ONLY AT WILL 
## END

test()
executeSAT()