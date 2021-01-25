# temple_xnat
Script For Downloading DICOMS from the XNAT REST API in easy python functionality

Download Scans from XNAT
Caleb Haynes 2021

Requires v. python > 3.5, xnat library installed
to install xnat: 

`python3 -m pip install xnat`

this script references the temple xnat server by default
https://xnat.cla.temple.edu

usage: 

`python3 downloadXNAT.py`

Can log into xnat, downlaods subjects DICOMS

As a python module:
from downloadXNAT.py import connect_pull

`connect_pull(url, user, password, session, subject, outputDir)`
