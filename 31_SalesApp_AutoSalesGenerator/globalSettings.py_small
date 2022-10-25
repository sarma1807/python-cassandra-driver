#!/usr/bin/env python

### import required libraries
from cassandra import ConsistencyLevel


### global variables

# change this to True when using this code with AstraDB : possible values : True / False
USE_ASTRA_DB = False


### https://docs.datastax.com/en/developer/python-driver/3.25/api/cassandra/#cassandra.ConsistencyLevel
CASS_READ_CONSISTENCY  = ConsistencyLevel.LOCAL_QUORUM
CASS_WRITE_CONSISTENCY = ConsistencyLevel.TWO


### for small system
TOTAL_USERS    = 1000        # SalesApp_GenerateUsers.py    will generate this number of users
TOTAL_PRODUCTS = 5000        # SalesApp_GenerateProducts.py will generate this number of products
GEN_MAX_ORDERS = 12          # minimum 10. SalesApp_GenerateOrders.py will generate less than this number of orders randomly
GEN_MAX_PRODUCTS_ORDER = 6   # minimum 5. SalesApp_GenerateOrders.py will generate less than this number of products per order randomly

