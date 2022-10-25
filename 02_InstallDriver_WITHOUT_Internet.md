#### python cassandra-driver is built by DataStax and distributed via : https://pypi.org/project/cassandra-driver/

### use this method in limited cases, when pip is NOT working or internet is NOT available on the server

---

#### go to https://pypi.org/project/cassandra-driver/#files

search and find a file with .tar.gz

found ` cassandra-driver-3.25.0.tar.gz `, download this file


###### Install all following packages as "root" user

```
cd /tmp
tar -xzvf cassandra-driver-3.25.0.tar.gz
cd /tmp/cassandra-driver-3.25.0
python setup.py install --no-cython
```

---

###### driver version :

```
# pip show cassandra-driver
Name: cassandra-driver
Version: 3.25.0
Summary: DataStax Driver for Apache Cassandra
Home-page: http://github.com/datastax/python-driver
Author: DataStax
Author-email:
License: UNKNOWN
Location: /usr/local/lib64/python3.6/site-packages/cassandra_driver-3.25.0-py3.6-linux-x86_64.egg
Requires: geomet, six
Required-by:
#
```

---

#### further reading : https://docs.datastax.com/en/developer/python-driver/3.25/installation/

