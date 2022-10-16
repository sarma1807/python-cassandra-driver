## Known Issues

```
As of 16-Oct-2022 :

Software versions :
CentOS Stream release 9 (5.14.0-171.el9.x86_64)
Python version 3.9.14
python cassandra-driver 3.25.0
Apache Cassandra Release Version 4.1-beta1

# when executing following python code :
SalesApp_GenerateUsers.py
SalesApp_GenerateProducts.py
SalesApp_GenerateOrders.py

# we are getting following WARNING :

>>> *.py:55: DeprecationWarning: ResultSet indexing support will be removed in 4.0. Consider using ResultSet.one() to get a single row.
>>>   cass_row = email_output[0]

```

