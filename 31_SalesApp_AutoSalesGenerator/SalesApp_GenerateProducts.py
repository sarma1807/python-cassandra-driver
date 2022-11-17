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

v_number_of_products = 0

### input verification
# if (len(sys.argv) < 2):
# 	sys.exit('ERROR : Missing Input. Requires 1 Number Input.')
# try:
# 	input_var = int(sys.argv[1])
# except:
# 	sys.exit('ERROR : Requires 1 Number Input.')

input_var = TOTAL_PRODUCTS

### main logic
try:
	cc = cassConnect()

	### build a cql statements
	cql_prdcat_stmt = cc.cass_session.prepare("SELECT product_category FROM lookup_product_categories WHERE id = ?")
	cql_prdcat_stmt.consistency_level = CASS_READ_CONSISTENCY

	cql_product_insert = cc.cass_session.prepare("INSERT INTO products (product_id, product_code, product_name, product_description, product_category, product_price, product_qoh) VALUES (?, ?, ?, ?, ?, ?, ?)")
	cql_product_insert.consistency_level = CASS_WRITE_CONSISTENCY

	### generate data using for loop
	for var_product_id in range(1, input_var+1):
		cql_stmt        = cql_prdcat_stmt.bind([random.randint(1, 20)])
		prdcat_output   = cc.cass_session.execute(cql_stmt)

		if (len(prdcat_output._current_rows) > 0):
			# cass_row = prdcat_output[0]  ### index based row fetching is deprecated in Python 4.x
			cass_row = prdcat_output.one()
			var_product_category = cass_row.product_category
		else:
			print("ERROR: looks like lookup data is missing in the database. use '03_load_data_in_lookup_tables.cql' to load lookup data.")

		var_product_code = str(uuid.uuid4()).replace('-', '')[1:13]
		var_product_name = str(uuid.uuid4()).replace('-', '')[1:random.randint(5, 9)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(5, 9)]
		var_product_description = str(uuid.uuid4()).replace('-', '')[1:random.randint(5, 6)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(6, 9)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(3, 5)] + ' ' + str(uuid.uuid4()).replace('-', '')[1:random.randint(7, 11)]

		var_product_price = str(random.randint(10, 60)) + '.' + str(random.randint(0, 99))
		var_product_qoh = random.randint(555, 5555)

		### save data in db
		cc.cass_session.execute(cql_product_insert, (var_product_id, var_product_code, var_product_name, var_product_description, var_product_category, var_product_price, var_product_qoh))

		v_number_of_products = var_product_id

except Exception as e:
	### something went wrong
	print("something went wrong.")
	print("")
	print(e)
else:
	### all went well
	output_message = str(v_number_of_products) + " products generated."
	print(output_message)
	print("Done.")


### close connection to cassandra cluster
cc.disconnect_from_cassandra()

