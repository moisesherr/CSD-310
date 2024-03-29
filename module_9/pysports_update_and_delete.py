import mysql.connector
from mysql.connector import errorcode

config = {
	"user": "pysports_user",
	"password": "seasprite",
	"host": "127.0.0.1",
	"database": "pysports",
	"raise_on_warnings": True
}

try:
	db = mysql.connector.connect(**config)
	print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

	cursor = db.cursor()

	#cursor.execute("INSERT INTO player (first_name, last_name, team_id) VALUES('Smeagol', 'Shire Folk', 1)")
	#cursor.execute("UPDATE player SET team_id = 2 WHERE player_id = 12")
	cursor.execute("DELETE FROM player WHERE player_id = 12")
	db.commit()
	cursor.execute("SELECT player_id, first_name, last_name, team_name FROM player left outer JOIN team on player.team_id = team.team_id")
	players = cursor.fetchall()
	print()
	print("-- DISPLAYING PLAYER RECORDS --")

	for player in players:
		print("Player ID: {}".format(player[0]))
		print("First Name: {}".format(player[1]))
		print("Last Name: {}".format(player[2]))
		print("Team Name: {}".format(player[3]))
		print()
	input("\n\n Press any key to continue...")

except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("   The supplied username or password are invalid")

	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("   The specified database does not exist")

	else:
		print(err)

finally:
	db.close()