#Download Scans from XNAT
# Caleb Haynes 2021
# req v python > 3.5, xnat

#to install xnat: python3 -m pip install xnat

import sys
try:
	import xnat
except ImportError:
	raise ImportError('Module for XNAT not found, try installing with "python3 -m pip install xnat"')

#this script references the temple xnat server by default
confighttps='https://xnat.cla.temple.edu'


'''
usage: python3 downloadXNAT.py <XNAT_username> <XNAT_password> <session> <subject> <outputDir>

Logs into xnat, downlaods subjects DICOMS
'''

def connect_pull(url, user, password, session, subject, outputDir):
        with xnat.connect(url, user, password) as connect:
            for sub in connect.projects[session].subjects.values():
	            if subject == sub.label:
	                sub.download_dir(outputDir)

def main():
	connect_pull(url=confighttps, 
			user = sys.argv[1], 
			password = sys.argv[2], 
			session = sys.argv[3],
			subject = sys.argv[4],
			outputDir = sys.argv[5]	
	)

if __name__ == "__main__":
	main()
