#### python cassandra-driver is built by DataStax and distributed via : https://pypi.org/project/cassandra-driver/

### this method will require internet connection on the server

---

###### Install all following packages as "root" user

Extra Packages for Enterprise Linux (EPEL) are required : verify and install :
```
rpm -qa | grep epel
yum install epel-release --assumeyes
```

<br><br>

Package manager for Python (PIP) is required : verify and install :
```
rpm -qa | grep pip
yum install python-pip --assumeyes
```

<br><br>

DataStax python cassandra-driver : verify/uninstall/install :
```
pip show cassandra-driver
pip uninstall cassandra-driver
pip install cassandra-driver
```

---

###### driver version :

```
[root@oramad ~]# pip show cassandra-driver
Name: cassandra-driver
Version: 3.25.0
Summary: DataStax Driver for Apache Cassandra
Home-page: http://github.com/datastax/python-driver
Author: DataStax
Author-email:
License: UNKNOWN
Location: /usr/local/lib64/python3.9/site-packages
Requires: geomet, six
Required-by:
[root@oramad ~]#
```

---

