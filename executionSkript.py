import sqlite3
import os

if __name__ == "__main__":
	files = os.listdir("/")
	number_files = len(files)
	print(number_files)

	connection = sqlite3.connect("probadeploy")

	cursor = connection.cursor()

	for x in files:
		file_name = "C:\ScriptFolder\Halk\\" + str(x) + ".sql"

		if (cursor.execute("SELECT 1 FROM AutomationScriptVersions WHERE FilePath = " + file_name) is None):
			sql_file = open(file_name)
			sql_as_string = sql_file.read()
			cursor.executescript(sql_as_string)
			cursor.execute("INSERT INTO AutomationScriptVersions (FilePath, Flag) VALUES (" +file_name+ ",1)")
			print(file_name + " je izvrsena.")

		if (cursor.execute("SELECT 1 FROM AutomationScriptVersions WHERE FilePath = " + file_name + " AND Flag = 0") is not None):
			sql_file = open(file_name)
			sql_as_string = sql_file.read()
			cursor.executescript(sql_as_string)
			cursor.execute("UPDATE AutomationScriptVersions SET Flag = 1 WHERE FilePath = " + file_name)
			print(file_name + " je izvrsena.")