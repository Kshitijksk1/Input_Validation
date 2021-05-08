#Libraries
from pysimplelog import Logger
import pandas as pd
import sys
import re
import csv
import getpass
import os

#Variable Declaration and Regular Expressions
Script_open = "<script>"
SQL_format = "select * from"
Script_close = "</script>"
name_r = "^[A-Z]\\'?([a-zA-Z]?\\'?[a-zA-Z]?\\,?[ ]?\\'?\\-?\\.?){1,3}$"
phone_r1 = "^(\+\d{1,2}\s?)?1?\-?\.?\s?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}$"
phone_r2 = "(\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4})"
phone_r3 = "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
L = Logger()

#ADD Function
if sys.argv[1].lower()=="add":
	with open('phonebook.csv', 'a') as newFile:
		newFileWriter = csv.writer(newFile)
		newFileWriter.writerow([sys.argv[1],sys.argv[2],sys.argv[3]])
		log = "logfile.log"
		if SQL_format in sys.argv[2].lower():
			L.info(["invalid entry",getpass.getuser(),os.getuid(), sys.argv[1:]])
		elif (Script_open in sys.argv[2].lower()) and (Script_close in sys.argv[2].lower()) and (sys.argv[2].index(Script_open)<sys.argv[2].index(Script_close)):
			L.info(["invalid entry",getpass.getuser(),os.getuid(), sys.argv[1:]])
		elif re.match(phone_r1,sys.argv[3]) or (re.match(phone_r2,sys.argv[3])) or (re.match(phone_r3,sys.argv[3])) and (re.search(name_r,sys.argv[2])):
			L.info([getpass.getuser(),os.getuid(), sys.argv[1:]])
		else:
			L.info(["invalid argument",getpass.getuser(),os.getuid(), sys.argv[1:]])
		
#LIST Function
elif (sys.argv[1]).lower()=="list":
	args = sys.argv[1]
	data_frame = pd.read_csv('phonebook.csv')
	print(data_frame)
	log = "logfile.log"
	L.info([getpass.getuser(),os.getuid(), sys.argv[1:]])

#DELETE Function
elif (sys.argv[1]).lower()=="del":
	args = sys.argv[2]
	data_frame1 = pd.read_csv('phonebook.csv',encoding='utf-8')
	data_frame_1 = data_frame1[data_frame1['name']!=args]
	data_frame_1.to_csv('phonebook.csv', index=False)
	data_frame2 = pd.read_csv('phonebook.csv',encoding='utf-8')
	data_frame_2 = data_frame2[data_frame2['number']!=args]
	data_frame_2.to_csv('phonebook.csv', index=False)
		
	frame1 = data_frame1.equals(data_frame_1)
	frame2 = data_frame2.equals(data_frame_2)
	frame3 = frame1 and frame2
	if frame3:
		log = "logfile.log"
		L.info(["Trying to remove invalid entry",getpass.getuser(),os.getuid(), sys.argv[1:]])
	else:
		log = "logfile.log"
		L.info(["Removed valid entry",getpass.getuser(),os.getuid(), sys.argv[1:]])	
		
#No Input
else:
	print("The commands are as follows:")
	print("ADD “<Person>” “<Telephone #>” - Add a new person to the database")
	print("DEL “<Person>” - Remove someone from the database by name")
	print("DEL “<Telephone #>” - Remove someone by telephone #")
	print("LIST - Produce a list of the members of the database")