#!/usr/bin/env python

### import required libraries
from cassandra import ConsistencyLevel


### global variables

# change this to True when using this code with AstraDB : possible values : True / False
USE_ASTRA_DB = False


### https://docs.datastax.com/en/developer/python-driver/3.25/api/cassandra/#cassandra.ConsistencyLevel
CASS_READ_CONSISTENCY  = ConsistencyLevel.LOCAL_QUORUM
CASS_WRITE_CONSISTENCY = ConsistencyLevel.TWO

