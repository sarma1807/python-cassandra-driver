#!/usr/bin/env python

### import cassConnectionManager.py and other required libraries
from cassConnectionManager import cassConnect
import sys

### sys.version_info.major : to identify python version (major release identifier)


try:
	cc = cassConnect()

	### execute queries
	cass_output_1 = cc.cass_session.execute("SELECT cluster_name, release_version FROM system.local")
	for cass_row in cass_output_1:
		output_message = "Connected to " + str(cass_row.cluster_name) + " and it is running " + str(cass_row.release_version) + " version."
		print(output_message)

	cass_output_2 = cc.cass_session.execute("SELECT count(1) AS nodes_count FROM system.peers")
	for cass_row in cass_output_2:
		output_message = "This cluster contains " + str(cass_row.nodes_count+1) + " nodes."
		print(output_message)

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

