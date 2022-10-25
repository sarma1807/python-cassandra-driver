#### Global Settings for all the programs in this project folder

`globalSettings.py` Python program to configure global settings used by all the programs in this project folder.

---

#### Configure Cassandra Cluster Connection

`cassConnectionManager.py` Python program to configure connection to Cassandra Cluster.

---

#### Apache Cassandra CQL Commands

`01_cassandra_sales_keyspace.cql` Apache Cassandra CQL commands to create sales keyspace.

`02_sales_create_tables.cql` Apache Cassandra CQL commands to create tables in sales keyspace.

`03_load_data_in_lookup_tables.cql` Apache Cassandra CQL insert data into lookup tables in sales keyspace.

---

#### SalesApp Python code written to use python cassandra-driver.

`SalesApp_GenerateUsers.py` Generates Users. Typically executed only 1 time during initial setup.

`SalesApp_GenerateProducts.py` Generates Products. Typically executed only 1 time during initial setup.

`SalesApp_GenerateOrders.py` Generates Orders. Execute it whenever you want to generate Orders or automate the execution using cron.

---

#### crontab

`crontab_for_auto_order_generation.md` crontab entries to automatically generate Orders.

---

NOTE : PYTHON CODE IS WRITTEN FOR DEMONSTRATION PURPOSES ONLY. IT IS NOT OPTIMIZED, NOR WRITTEN BY A PROFESSIONAL PYTHON PROGRAMMER.

