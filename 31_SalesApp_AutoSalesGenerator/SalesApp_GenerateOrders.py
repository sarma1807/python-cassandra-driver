#!/usr/bin/env python
# code written for and tested in Python 2.7.5

### import cassConnectionManager.py and other required libraries

from cassConnectionManager import cassConnect
from cassandra             import ConsistencyLevel
from cassandra.query       import SimpleStatement
from datetime              import datetime, date, timedelta
import sys
import random
import uuid
import math
import string

### sys.version_info.major : to identify python version (major release identifier)

### https://docs.datastax.com/en/developer/python-driver/3.24/api/cassandra/#cassandra.ConsistencyLevel
CASS_READ_CONSISTENCY  = ConsistencyLevel.LOCAL_QUORUM
CASS_WRITE_CONSISTENCY = ConsistencyLevel.TWO

### user is expected to pre-generate 10000 users using SalesApp_GenerateUsers.py
var_users_count    = 10000

### user is expected to pre-generate 50000 products using SalesApp_GenerateProducts.py
var_products_count = 50000

v_number_of_orders = 0


### main logic
try:
	cc = cassConnect()

	### build a cql statements
	cql_user_stmt = cc.cass_session.prepare("SELECT user_id, user_email_id, user_name, user_phone_number, user_platform, user_state_code FROM users WHERE user_id = ?")
	cql_user_stmt.consistency_level = CASS_READ_CONSISTENCY
	
	cql_product_stmt = cc.cass_session.prepare("SELECT product_id, product_category, product_code, product_name, product_price, product_qoh FROM products WHERE product_id = ?")
	cql_product_stmt.consistency_level = CASS_READ_CONSISTENCY

	cql_order_insert = cc.cass_session.prepare("INSERT INTO sales_orders (order_date, order_date_hour, order_timestamp, order_code, order_discount_percent, order_estimated_shipping_date, order_grand_total, order_number_of_products, order_total, user_email_id, user_id, user_name, user_phone_number, user_platform, user_state_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)")
	cql_order_insert.consistency_level = CASS_WRITE_CONSISTENCY

	cql_order_products_insert = cc.cass_session.prepare("INSERT INTO sales_order_products (order_date, order_code, product_id, product_category, product_code, product_name, product_price_each, product_price_total, product_sold_quantity) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)")
	cql_order_products_insert.consistency_level = CASS_WRITE_CONSISTENCY

	cql_product_qoh_insert = cc.cass_session.prepare("INSERT INTO products (product_id, product_qoh) VALUES (?, ?)")
	cql_product_qoh_insert.consistency_level = CASS_WRITE_CONSISTENCY


	### generate orders using for loop - start
	for var_orders in range(1, random.randint(4, 22)):

		### pick a user
		cql_stmt              = cql_user_stmt.bind([random.randint(1, var_users_count)])
		user_output           = cc.cass_session.execute(cql_stmt)
		cass_row              = user_output[0]
		var_user_id           = cass_row.user_id
		var_user_email_id     = cass_row.user_email_id
		var_user_name         = cass_row.user_name
		var_user_phone_number = cass_row.user_phone_number
		var_user_platform     = cass_row.user_platform
		var_user_state_code   = cass_row.user_state_code


		### setup order info
		var_order_date                          = datetime.date(datetime.now())
		var_order_date_hour                     = datetime.now().hour
		var_order_timestamp                     = datetime.now()
		var_order_code                          = uuid.uuid4()
		var_order_discount_percent				= random.randint(0, 5)
		var_order_estimated_shipping_date		= date.today() + timedelta(days=random.randint(3, 20))
		var_order_grand_total                   = 0
		var_order_number_of_products            = 0
		var_order_total                         = 0

		### generate order-products using for loop - start
		for var_order_products in range(1, random.randint(2, 8)):

			### pick a product
			cql_stmt                   = cql_product_stmt.bind([random.randint(1, var_products_count)])
			product_output             = cc.cass_session.execute(cql_stmt)
			cass_row                   = product_output[0]
			var_product_id             = cass_row.product_id
			var_product_category       = cass_row.product_category
			var_product_code           = cass_row.product_code
			var_product_name           = cass_row.product_name
			var_product_price          = cass_row.product_price
			var_product_qoh            = cass_row.product_qoh
			var_product_sold_quantity  = random.randint(3, 15)
			var_product_price_total    = (var_product_price * var_product_sold_quantity)

			### save order-products in db only if product quantity on hand is good
			if ( var_product_qoh > (var_product_sold_quantity+50) ):
				cc.cass_session.execute(cql_order_products_insert, (var_order_date, var_order_code, var_product_id, var_product_category, var_product_code, var_product_name, var_product_price, var_product_price_total, var_product_sold_quantity))
				cc.cass_session.execute(cql_product_qoh_insert, (var_product_id, var_product_qoh - var_product_sold_quantity))
				var_order_number_of_products = var_order_number_of_products + 1
				var_order_total = var_order_total + var_product_price_total

		### generate order-products using for loop - end

		var_order_grand_total = var_order_total - ( (var_order_total * var_order_discount_percent) / 100 )

		### save orders in db only if any products were sold
		if ( var_order_number_of_products > 0 ):
			cc.cass_session.execute(cql_order_insert, (var_order_date, var_order_date_hour, var_order_timestamp, var_order_code, var_order_discount_percent, var_order_estimated_shipping_date, var_order_grand_total, var_order_number_of_products, var_order_total, var_user_email_id, var_user_id, var_user_name, var_user_phone_number, var_user_platform, var_user_state_code))
			v_number_of_orders = v_number_of_orders + 1

	### generate orders using for loop - end


except:
	### something went wrong
	print var_order_timestamp, "| something went wrong."
else:
	### all went well
	print var_order_timestamp, "|", v_number_of_orders, "orders generated."
	# print "Done."


### close connection to cassandra cluster
cc.disconnect_from_cassandra()
