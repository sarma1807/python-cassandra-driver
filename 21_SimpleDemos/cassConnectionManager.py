#!/usr/bin/env python
# code written for and tested in Python 2.7.5

### import cassandra driver libraries/modules
from cassandra.cluster import Cluster
from cassandra.auth    import PlainTextAuthProvider
from cassandra.query   import SimpleStatement

### connection variables
CASS_CONTACT_POINTS    = ["192.168.1.151", "192.168.1.171"] ;
CASS_PORT              = 9042 ;
CASS_USERNAME          = "thor" ;
CASS_PASSWORD          = "Complic4ted" ;
CASS_KEYSPACE          = "cassdemo" ;

### main class
class cassConnect:

	### init function
	def __init__(self):

		### prep for cassandra connection
		cass_auth_provider = PlainTextAuthProvider(username = CASS_USERNAME, password = CASS_PASSWORD)
		self.cass_cluster = Cluster(contact_points = CASS_CONTACT_POINTS, port = CASS_PORT, auth_provider = cass_auth_provider)

		### connect to cassandra cluster and set default keyspace
		self.cass_session = self.cass_cluster.connect(CASS_KEYSPACE)


	### close cassandra connection function
	def disconnect_from_cassandra(self):
		self.cass_cluster.shutdown()
		self.cass_session.shutdown()
		return (0)

