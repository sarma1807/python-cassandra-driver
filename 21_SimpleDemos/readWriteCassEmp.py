#!/usr/bin/env python

### import cassConnectionManager.py and other required libraries
from cassConnectionManager import cassConnect
from cassandra             import ConsistencyLevel
from cassandra.query       import SimpleStatement
from globalSettings        import *
import sys
import random
import uuid

### sys.version_info.major : to identify python version (major release identifier)

try:
	cc = cassConnect()

	### build a cql statement
	cass_dml = "INSERT INTO emp (empid, first_name, last_name) VALUES (?, ?, ?)"
	cql_prepared_stmt_1 = cc.cass_session.prepare(cass_dml)
	cql_prepared_stmt_1.consistency_level = CASS_WRITE_CONSISTENCY
	### value for empid will be generated using random funtion
	### value for first_name and last_name will be generated using uuid function
	cc.cass_session.execute(cql_prepared_stmt_1, (random.randint(1111, 9999), str(uuid.uuid4()).replace('-', '')[1:11], str(uuid.uuid4()).replace('-', '')[1:11]))
	print("---- 1 row inserted -----------------------------------")
	print("")

	### print header
	print("---- select and print only 1 row ----------------------")
	print("-------------------------------------------------------")
	print("first_name | last_name | empid")
	print("-------------------------------------------------------")
	### prepare and execute select query with only 1 row output
	cass_select = "SELECT empid, first_name, last_name FROM emp WHERE empid = ?"
	cql_prepared_stmt_2 = cc.cass_session.prepare(cass_select)
	cql_prepared_stmt_3 = cql_prepared_stmt_2.bind([1001])
	cql_prepared_stmt_3.consistency_level = CASS_READ_CONSISTENCY
	cass_output_1 = cc.cass_session.execute(cql_prepared_stmt_3)
	if (len(cass_output_1._current_rows) > 0):
		# cass_row_1 = cass_output_1[0]  ### index based row fetching is deprecated in Python 4.x
		cass_row_1 = cass_output_1.one()
		output_message = cass_row_1.first_name + " | " + cass_row_1.last_name + " | " + str(cass_row_1.empid)
		print(output_message)
	else:
		print("ERROR: looking for empid=1001 and that row was not found in the database")
	print("-------------------------------------------------------")
	print("")

	### print header
	print("---- select and print 5 rows --------------------------")
	print("-------------------------------------------------------")
	print("first_name | last_name | empid")
	print("-------------------------------------------------------")
	### execute select query - might return multiple row output
	cass_select = SimpleStatement("SELECT empid, first_name, last_name FROM emp LIMIT 5", consistency_level = CASS_READ_CONSISTENCY)
	cass_output_1 = cc.cass_session.execute(cass_select)
	for cass_row in cass_output_1:
		output_message = cass_row.first_name + " | " + cass_row.last_name + " | " + str(cass_row.empid)
		print(output_message)
	print("-------------------------------------------------------")
	print("")


except Exception as e:
	### something went wrong
	print("something went wrong.")
	print("")
	print(e)
else:
	### all went well
	print("Done.")


### close connection to cassandra cluster
cc.disconnect_from_cassandra()

