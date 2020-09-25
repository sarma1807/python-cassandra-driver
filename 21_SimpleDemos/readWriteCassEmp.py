#!/usr/bin/env python
# code written for and tested in Python 2.7.5

### import cassConnectionManager.py and other required libraries
from cassConnectionManager import cassConnect
import sys

### sys.version_info.major : to identify python version (major release identifier)


try:
	cc = cassConnect()

	### build a cql statement
	cass_query = "INSERT INTO emp (empid, first_name, last_name) VALUES (?, ?, ?)"
	cql_prepared_stmt = cc.cass_session.prepare(cass_query)
	cc.cass_session.execute(cql_prepared_stmt, (1002, "Larry", "Cool"))

	### print header
	print "-------------------------------------------------------"
	print "first_name | last_name | empid"
	print "-------------------------------------------------------"
	### execute select query
	cass_output_1 = cc.cass_session.execute("SELECT empid, first_name, last_name FROM emp")
	for cass_row in cass_output_1:
		print cass_row.first_name, "|", cass_row.last_name, "|", cass_row.empid
	print "-------------------------------------------------------"


except:
	### something went wrong
	print "something went wrong."
else:
	### all went well
	print "Done."


### close connection to cassandra cluster
cc.disconnect_from_cassandra()

