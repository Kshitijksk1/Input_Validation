# Input_Validation

Description of how code works:
The code has 3 major functionalities : 1) ADD 2)DEL 3)LIST
ADD: The add function adds a new entry into the phonebook.csv file. When an entry is made into the phonebook.csv file it is also logged into a logfile which shows the actions performed. We check input format by using Regex. If the input is in the correct format then it is added to the file or else it is given as invalid entry.
DEL: The delete function deletes which entry the user wants to delete. The user can delete an entry by giving a name of the contact or the contact number. This is also logged into the log file.
LIST: The list function shows a list of the contacts in the phonebook.
If there are no arguments specified in the command line then we will get all the available options i.e the functionalities.

For compilation:
We can compile the file using the following commands:
python3 phonebook.py ADD “name” “phonenumber”
python3 phonebook.py DEL “name”
python3 phonebook.py DEL “number”
python3 phonebook.py LIST

For compilation we can use lower case letters for ADD, DEL and LIST as well.
We are using some python libraries like Pandas, re, csv, pysimplelog, getpass, etc.
In this code we check the inputs we get from the command line. If the input is not in a particular format then it will be considered as invalid. The main aim is to stop malicious users from using harmful inputs like we did in SQL Injection and Cross Site scripting attacks. We check the inputs like script tags and SQL statements like SELECT and WHERE as well.
I used a logger function to create a log file where we save all the commands that are used.

Assumptions: We assume that the user input we get from the command line is always checked and confirmed with the regular expressions used. After this input validation step only these values are stored
in the phonebook.csv file. When we try to delete the information we do not check the inputs for regular expressions again as the input will be deleted only when both the input and the contact information match.

Pros/Cons:
The pros of my approach are that the program is easy to use as it gives step by step output which helps the user understand what has happened in the previous step.
Cons of m approach are that as per the file given by sir I wasn’t able to cover all the regular expressions for the number format but I tried doing all the possible ones.

References:
https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number
https://realpython.com/python-logging/
https://intellipaat.com/community/18827/how-to-delete-only-one-row-in-csv-with-python
https://stackoverflow.com/questions/24662571/python-import-csv-to-list
https://stackoverflow.com/questions/3878195/python-logging-alternatives
https://logbook.readthedocs.io/en/stable/
https://stackoverflow.com/questions/842059/is-there-a-portable-way-to-get-the-current-username-in-python
https://www.geeksforgeeks.org/python-pandas-dataframe/
