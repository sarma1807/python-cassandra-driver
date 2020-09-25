#!/usr/bin/env python
# code written for and tested in Python 2.7.5

### import cassConnectionManager.py and other required libraries
from cassConnectionManager import cassConnect
import sys

### sys.version_info.major : to identify python version (major release identifier)


try:
	cc = cassConnect()

	### execute queries
	cass_output_1 = cc.cass_session.execute("SELECT cluster_name, release_version FROM system.local")
	for cass_row in cass_output_1:
		print "Connected to", cass_row.cluster_name, "and it is running", cass_row.release_version, "version."

	cass_output_2 = cc.cass_session.execute("SELECT count(1) AS nodes_count FROM system.peers")
	for cass_row in cass_output_2:
			print "This cluster contains", cass_row.nodes_count+1, "nodes."

except:
	### something went wrong
	print "something went wrong."
else:
	### all went well
	print "Done."


### close connection to cassandra cluster
cc.disconnect_from_cassandra()

