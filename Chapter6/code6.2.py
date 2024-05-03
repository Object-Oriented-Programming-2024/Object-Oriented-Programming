# Open the configuration file
config = open('config.ini','w')
#Create the Details of the application's database to a file
db_name="employees"
db_user = "ahmed_alhameli"
db_password="&V63fh!r5$"
#Creating a config file that stores the application's database details
config.write(f"db_name={db_name}\ndb_user={db_user}\ndb_password={db_password}")
config.close()
