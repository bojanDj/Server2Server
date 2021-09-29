import sqlite3
import os

if __name__ == "__main__":
	list = os.listdir("/")
	number_files = len(list)
	print(number_files)

	connection = sqlite3.connect(":memory:") #db name izmeni

	cursor = connection.cursor()

	for x in range(1,number_files):
		file_name = "datoteka" + str(x) + ".sql"

		if (cursor.execute("SELECT 1 FROM bokipom WHERE datoteka = " + file_name + " AND flag = 0") is not None):
			sql_file = open(file_name)
			sql_as_string = sql_file.read()
			cursor.executescript(sql_as_string)
			cursor.execute("UPDATE bokipom SET flag = 1 WHERE datoteka = " + file_name)
			print(file_name + " je izvrsena.")
