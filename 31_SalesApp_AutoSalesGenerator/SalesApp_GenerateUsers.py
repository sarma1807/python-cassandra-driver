#!/usr/bin/env python

### import cassConnectionManager.py and other required libraries

from cassConnectionManager import cassConnect
from cassandra             import ConsistencyLevel
from cassandra.query       import SimpleStatement
from globalSettings        import *
import sys
import random
import uuid
import math
import string

### sys.version_info.major : to identify python version (major release identifier)

v_number_of_users = 0

### input verification
# if (len(sys.argv) < 2):
# 	sys.exit('ERROR : Missing Input. Requires 1 Number Input.')
# try:
# 	input_var = int(sys.argv[1])
# except:
# 	sys.exit('ERROR : Requires 1 Number Input.')

input_var = TOTAL_USERS

### main logic
try:
	cc = cassConnect()

	### build a cql statements
	cql_email_stmt    = cc.cass_session.prepare("SELECT email_server FROM lookup_email_servers WHERE id = ?")
	cql_state_stmt    = cc.cass_session.prepare("SELECT state_code FROM lookup_usa_states WHERE id = ?")
	cql_platform_stmt = cc.cass_session.prepare("SELECT platform FROM lookup_user_platforms WHERE id = ?")
	cql_email_stmt.consistency_level    = CASS_READ_CONSISTENCY
	cql_state_stmt.consistency_level    = CASS_READ_CONSISTENCY
	cql_platform_stmt.consistency_level = CASS_READ_CONSISTENCY

	cql_user_insert = cc.cass_session.prepare("INSERT INTO users (user_id, user_name, user_email_id, user_state_code, user_phone_number, user_platform) VALUES (?, ?, ?, ?, ?, ?)")
	cql_user_insert.consistency_level = CASS_WRITE_CONSISTENCY

	### generate data using for loop
	for var_user_id in range(1, input_var+1):
		cql_stmt        = cql_email_stmt.bind([random.randint(1, 10)])
		email_output    = cc.cass_session.execute(cql_stmt)
		cql_stmt        = cql_state_stmt.bind([random.randint(1, 51)])
		state_output    = cc.cass_session.execute(cql_stmt)
		cql_stmt        = cql_platform_stmt.bind([random.randint(1, 10)])
		platform_output = cc.cass_session.execute(cql_stmt)

		if (len(email_output._current_rows) > 0):
			# cass_row = email_output[0]  ### index based row fetching is deprecated in Python 4.x
			cass_row = email_output.one()
			var_email_server = cass_row.email_server
		else:
			print("ERROR: looks like lookup data is missing in the database. use '03_load_data_in_lookup_tables.cql' to load lookup data.")

		if (len(state_output._current_rows) > 0):
			# cass_row = state_output[0]  ### index based row fetching is deprecated in Python 4.x
			cass_row = state_output.one()
			var_state_code = cass_row.state_code
		else:
			print("ERROR: looks like lookup data is missing in the database. use '03_load_data_in_lookup_tables.cql' to load lookup data.")

		if (len(platform_output._current_rows) > 0):
			# cass_row = platform_output[0]  ### index based row fetching is deprecated in Python 4.x
			cass_row = platform_output.one()
			var_platform = cass_row.platform
		else:
			print("ERROR: looks like lookup data is missing in the database. use '03_load_data_in_lookup_tables.cql' to load lookup data.")

		var_user_name = str(uuid.uuid4()).replace('-', '')[1:13]
		var_user_email_id = var_user_name + var_email_server
		var_user_phone_number = str(random.randint(700, 900)) + '-' + str(random.randint(100, 900)) + '-' + str(random.randint(1001, 9999))

		### save data in db
		cc.cass_session.execute(cql_user_insert, (var_user_id, var_user_name, var_user_email_id, var_state_code, var_user_phone_number, var_platform))

		v_number_of_users = var_user_id

except Exception as e:
	### something went wrong
	print("something went wrong.")
	print("")
	print(e)
else:
	### all went well
	output_message = str(v_number_of_users) + " users generated."
	print(output_message)
	print("Done.")


### close connection to cassandra cluster
cc.disconnect_from_cassandra()

