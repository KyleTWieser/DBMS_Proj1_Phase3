import sqlite3
from sqlite3 import Error

def create_Conection(db_file):
	"""
	this will connect to the db file that is specified later on in the code
	:param_db is the db we want to connect to
	:return the connection to the db"""
	conn = None
	try:
		conn = sqlite3.connect(db_file)
		print("Connected to the Database")
	except Error as e:
		print(e)
	return conn

def select_all_task(conn):
	"""
	this will query all rows in the table
	:param conn: is the connection object to the db
	:return 
	"""
	cur = conn.cursor() #this is the cursor for the db
	cur.execute("SELECT * FROM Employee") #after we select cursor from earlier line, 
	#this will input the text and execute the command"""
	
	rows = cur.fetchall() #this gets all the data returned from the db and stores it in variable
	for row in rows:
		print(row)
		
def select_custom_input(conn, query):
	"""
	this fucntion will take a custom query for the db and use that to grab data from the db
	:param conn is the connetion to the db
	:param query is the query as a string we want to use on our db
	:return 
	"""
	print("\nThe query that is input is: ")
	print (query)
	print("")
	cur = conn.cursor() #this is the cursor for the db
	cur.execute(query) #after we select cursor from earlier line, 
	#this will input the query that is defined at the start of the function and execute the command
	
	rows = cur.fetchall() #this gets all the data returned from the db and stores it in variable
	for row in rows:
		print(row)

def user_input_query(conn):
	"""
	this fucntion will ask the user to input the query into the console and then query the db
	:param conn is the connection to the db
	:return
	"""
	query = input("Enter a query for the database: ")
	print("")
	cur = conn.cursor() #this is the cursor for the db
	cur.execute(query) #after we select cursor from earlier line, 
	#this will input the query that is defined at the start of the function and execute the command
	
	rows = cur.fetchall() #this gets all the data returned from the db and stores it in variable
	for row in rows:
		print(row)

query1 = "SELECT First_Name, Last_Name FROM Passenger where Flight_Number = '12345ABCDE'"
query2 = "select Pilot_ID, Flight_Number, Destination_City from Flight where Departure_Time between '3/15/2021 0:00' and '3/15/2021 23:59'"
query3 = "select Flight_Number, Inspection_Date, Departure_Time from Flight inner join Inspection on Flight.Inspection_ID = Inspection.Inspection_ID where Inspection_Date >= Departure_Time"
query4 = "select * from Flight where Flight_Duration > 180"
query5 = "select * from employee where exists(select * from Passenger where employee.First_Name = passenger.First_Name and employee.Last_Name = passenger.Last_Name)"
dbIn = input("Enter the name of the database you want to scan: ")

if dbIn == "Nelson_Wieser.db":
	dbConnection = create_Conection(dbIn)
	while(True):
		print("\n\n**************************************************\n")
		print("1.) Select the first and last names of passengers on flight 12345ABCDE")
		print("2.) Select the cities that each pilot flew to on 3/15/2021")
		print("3.) Select each inspection that occurred after original departure time")
		print("4.) Select each flight that is longer than 180 minutes")
		print("5.) Select each employee that is listed as a passenger")
		print("6.) Enter a custom query")
		print("\n**************************************************\n")
		inputSelect = input("Enter the number for which query you want to execute or enter 0 to exit: ")
		print("---------------------------------------------------")
		if(inputSelect == '0'):
			print("You are now exiting the program")
			break
		if(inputSelect == '1'):
			select_custom_input(dbConnection, query1)
		if(inputSelect == '2'):
			select_custom_input(dbConnection, query2)
		if(inputSelect == '3'):
			select_custom_input(dbConnection, query3)
		if(inputSelect == '4'):
			select_custom_input(dbConnection, query4)
		if(inputSelect == '5'):
			select_custom_input(dbConnection, query5)
		if(inputSelect == '6'):
			user_input_query(dbConnection)
		
	#after this comment is where we should put all of our queries use the one directly under this for an example, i do not want it to be one of our solutions
	#select_custom_input(dbConnection, "SELECT First_Name, Last_Name FROM Passenger where Flight_Number = '12345ABCDE'") #TODO DELETE THIS LINE IT IS ONLY AN EXAMPLE
	#user_input_query(dbConnection) #TODO DELETE THIS ONE AS WELL IF YOU DO NOT USE IT, NOT NEEDED IF WE HARD CODE THE QUERIES
else:
	print("Not the expected database connected")
	print("If the file connected to is not db will throw error")
	print("Now using the user input for queries.")
	print("")
	user_input_query(dbConnection)
	user_input_query(dbConnection)
	user_input_query(dbConnection)
	user_input_query(dbConnection)
	user_input_query(dbConnection)

dbConnection.close() #this closes the connection to the db, shouldnt really matter though