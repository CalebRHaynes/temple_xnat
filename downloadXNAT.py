#Download Scans from XNAT
# Caleb Haynes 2021
# req v python > 3.5, xnat
#to install xnat: python3 -m pip install xnat

'''
usage: python3 downloadXNAT.py <XNAT_username> <XNAT_password> <session> <subject> <outputDir>
Logs into xnat, downlaods subjects DICOMS
'''
#import sys
import os
import json
from pprint import pprint
url='https://xnat.cla.temple.edu'
user = 'CalebHaynes'
session = 'LEARN'
outputDir = os.getcwd()
try:
	import xnat
except ImportError:
	raise ImportError('Module for XNAT not found, try installing with "python3 -m pip install xnat"')

'''
usage: python3 downloadXNAT.py <XNAT_username> <XNAT_password> <session> <subject> <outputDir>
Logs into xnat, downlaods subjects DICOMS
'''

def pass_prompt():
	return input('Password: \n\n>> ')

def connect_pull(url, user, session, subject, outputDir):
	print(url, user, session, subject, outputDir)
	password = pass_prompt()
	with xnat.connect(url, user, password) as connect:

		for sub in connect.projects[session].subjects.values():
			if subject == sub.label:
				print(sub, sub.label, url, user, session, subject, outputDir)
				sub.download_dir(outputDir)

def list_subjects(url, user, password, session):
	with xnat.connect(url, user, password) as connect:
            return [i for i in connect.projects[session].subjects.values()]

def display_sublist():
	password = pass_prompt()
	pprint(list_subjects(url, user, password, session))
	pass

def display_dicom_dir(outputDir):
	pprint(os.listdir(outputDir))
	pass

def home_screen():
	done = False
	while not done:
		print('''\n\nJARCHO LAB XNAT//DICOM//BIDS\n\n
		\n1) DISPLAY XNAT SUBJECTS
		\n2) DISPLAY CURRENT DICOM DIRECTORY
		\n3) TRANSFER DICOM
		\n4) CONVERT BIDS
		\n5) OPTIONS
		\n6) EXIT
		'''
	)
		choice = input("* ")
		if choice == '1':
		    display_sublist()
		elif choice == '2':
		    display_dicom_dir(outputDir)
		elif choice == '3':
			subject = input('Input Subject Number: ')
			connect_pull(url, user, session, subject, outputDir)
		elif choice == '4':
			pprint('Uh oh not built yet ;/')
		elif choice == '5':
			options_screen()
		elif choice == '6':
		    done = True
		else:
		    pprint("Invalid Choice")
		

def options_screen():

	done = False
	while not done:
		print('''\n\nJARCHO LAB XNAT//DICOM//BIDS\n\n
		\n***OPTIONS***
		\n1) NEW CONFIG 
		\n2) DISPLAY CONFIG
		\n3) CHANGE CONFIG
		\n4) DELETE CONFIG
		\n5) VIEW TABLE
		\n6) EXIT
		'''
	)
		choice = input(">> ")
		if choice == '1':
		    pprint('Make New \n\n\n\n\n\n')
		elif choice == '2':
		    pprint('Print JSON \n\n\n\n\n\n')
		elif choice == '3':
		    pprint('EDIT JSON \n\n\n\n\n\n')
		elif choice == '4':
		    pprint('DELETE JSON \n\n\n\n\n\n')
		elif choice == '5':
		    pprint('PRINT TABLE \n\n\n\n\n\n')
		elif choice == '6':
			done = True
		else:
		    pprint("Invalid Choice \n\n\n\n\n\n")
	pass



def main():
	home_screen()

if __name__ == "__main__":
	main()
