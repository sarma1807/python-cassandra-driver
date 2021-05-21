###### python cassandra-driver is built by DataStax and distributed via : https://pypi.org/project/cassandra-driver/

---

###### Install all following packages as "root" user

Extra Packages for Enterprise Linux (EPEL) are required : verify and install :
```
rpm -qa | grep epel
yum install epel-release
```

<br><br>

Package manager for Python (PIP) is required : verify and install :
```
rpm -qa | grep pip
yum install python-pip
```

<br><br>

DataStax python cassandra-driver : verify/uninstall/install :
```
pip show cassandra-driver
pip uninstall cassandra-driver
pip install cassandra-driver
```

---

###### sample output :

```
[root@DooM3 ~]# rpm -qa | grep epel

[root@DooM3 ~]# yum install epel-release
Loaded plugins: fastestmirror
Determining fastest mirrors
 * base: mirrors.advancedhosters.com
 * extras: mirror.es.its.nyu.edu
 * updates: mirror.wdc1.us.leaseweb.net
base                                                                                                          | 3.6 kB  00:00:00
extras                                                                                                        | 2.9 kB  00:00:00
updates                                                                                                       | 2.9 kB  00:00:00
(1/2): extras/7/x86_64/primary_db                                                                             | 206 kB  00:00:00
(2/2): updates/7/x86_64/primary_db                                                                            | 4.5 MB  00:00:00
Resolving Dependencies
--> Running transaction check
---> Package epel-release.noarch 0:7-11 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=====================================================================================================================================
 Package                             Arch                          Version                       Repository                     Size
=====================================================================================================================================
Installing:
 epel-release                        noarch                        7-11                          extras                         15 k

Transaction Summary
=====================================================================================================================================
Install  1 Package

Total download size: 15 k
Installed size: 24 k
Is this ok [y/d/N]: y
Downloading packages:
epel-release-7-11.noarch.rpm                                                                                  |  15 kB  00:00:00
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : epel-release-7-11.noarch                                                                                          1/1
  Verifying  : epel-release-7-11.noarch                                                                                          1/1

Installed:
  epel-release.noarch 0:7-11

Complete!
[root@DooM3 ~]#

[root@DooM3 ~]# rpm -qa | grep epel
epel-release-7-11.noarch
```

<br><br>

```
[root@DooM3 ~]# python -V
Python 2.7.5

[root@DooM3 ~]# rpm -qa | grep pip

[root@DooM3 ~]# yum install python-pip
Loaded plugins: fastestmirror
Loading mirror speeds from cached hostfile
epel/x86_64/metalink                                                                                          |  15 kB  00:00:00
 * base: mirrors.advancedhosters.com
 * epel: ewr.edge.kernel.org
 * extras: mirror.es.its.nyu.edu
 * updates: mirror.wdc1.us.leaseweb.net
epel                                                                                                          | 4.7 kB  00:00:00
(1/3): epel/x86_64/group_gz                                                                                   |  95 kB  00:00:00
(2/3): epel/x86_64/updateinfo                                                                                 | 1.0 MB  00:00:00
(3/3): epel/x86_64/primary_db                                                                                 | 6.9 MB  00:00:00
Resolving Dependencies
--> Running transaction check
---> Package python2-pip.noarch 0:8.1.2-14.el7 will be installed
--> Processing Dependency: python-setuptools for package: python2-pip-8.1.2-14.el7.noarch
--> Running transaction check
---> Package python-setuptools.noarch 0:0.9.8-7.el7 will be installed
--> Processing Dependency: python-backports-ssl_match_hostname for package: python-setuptools-0.9.8-7.el7.noarch
--> Running transaction check
---> Package python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7 will be installed
--> Processing Dependency: python-ipaddress for package: python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
--> Processing Dependency: python-backports for package: python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch
--> Running transaction check
---> Package python-backports.x86_64 0:1.0-8.el7 will be installed
---> Package python-ipaddress.noarch 0:1.0.16-2.el7 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

=====================================================================================================================================
 Package                                             Arch                   Version                       Repository            Size
=====================================================================================================================================
Installing:
 python2-pip                                         noarch                 8.1.2-14.el7                  epel                 1.7 M
Installing for dependencies:
 python-backports                                    x86_64                 1.0-8.el7                     base                 5.8 k
 python-backports-ssl_match_hostname                 noarch                 3.5.0.1-1.el7                 base                  13 k
 python-ipaddress                                    noarch                 1.0.16-2.el7                  base                  34 k
 python-setuptools                                   noarch                 0.9.8-7.el7                   base                 397 k

Transaction Summary
=====================================================================================================================================
Install  1 Package (+4 Dependent packages)

Total download size: 2.1 M
Installed size: 9.4 M
Is this ok [y/d/N]: y
Downloading packages:
(1/5): python-backports-1.0-8.el7.x86_64.rpm                                                                  | 5.8 kB  00:00:00
(2/5): python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch.rpm                                           |  13 kB  00:00:00
(3/5): python-ipaddress-1.0.16-2.el7.noarch.rpm                                                               |  34 kB  00:00:00
(4/5): python-setuptools-0.9.8-7.el7.noarch.rpm                                                               | 397 kB  00:00:00
warning: /var/cache/yum/x86_64/7/epel/packages/python2-pip-8.1.2-14.el7.noarch.rpm: Header V4 RSA/SHA256 Signature, key ID 352c64e5: NOKEY
Public key for python2-pip-8.1.2-14.el7.noarch.rpm is not installed
(5/5): python2-pip-8.1.2-14.el7.noarch.rpm                                                                    | 1.7 MB  00:00:00
-------------------------------------------------------------------------------------------------------------------------------------
Total                                                                                                4.1 MB/s | 2.1 MB  00:00:00
Retrieving key from file:///etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
Importing GPG key 0x352C64E5:
 Userid     : "Fedora EPEL (7) <epel@fedoraproject.org>"
 Fingerprint: 91e9 7d7c 4a5e 96f1 7f3e 888f 6a2f aea2 352c 64e5
 Package    : epel-release-7-11.noarch (@extras)
 From       : /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7
Is this ok [y/N]: y
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : python-backports-1.0-8.el7.x86_64                                                                                 1/5
  Installing : python-ipaddress-1.0.16-2.el7.noarch                                                                              2/5
  Installing : python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch                                                          3/5
  Installing : python-setuptools-0.9.8-7.el7.noarch                                                                              4/5
  Installing : python2-pip-8.1.2-14.el7.noarch                                                                                   5/5
  Verifying  : python-ipaddress-1.0.16-2.el7.noarch                                                                              1/5
  Verifying  : python2-pip-8.1.2-14.el7.noarch                                                                                   2/5
  Verifying  : python-setuptools-0.9.8-7.el7.noarch                                                                              3/5
  Verifying  : python-backports-ssl_match_hostname-3.5.0.1-1.el7.noarch                                                          4/5
  Verifying  : python-backports-1.0-8.el7.x86_64                                                                                 5/5

Installed:
  python2-pip.noarch 0:8.1.2-14.el7

Dependency Installed:
  python-backports.x86_64 0:1.0-8.el7                     python-backports-ssl_match_hostname.noarch 0:3.5.0.1-1.el7
  python-ipaddress.noarch 0:1.0.16-2.el7                  python-setuptools.noarch 0:0.9.8-7.el7

Complete!
[root@DooM3 ~]#

[root@DooM3 ~]# rpm -qa | grep pip
python2-pip-8.1.2-14.el7.noarch
```

<br><br>

```
[root@DooM3 ~]# pip show cassandra-driver

[root@DooM3 ~]# pip install cassandra-driver
Collecting cassandra-driver
  Downloading https://files.pythonhosted.org/packages/0d/11/473b6b054e592fda6f998ffd7cb32c1b98da11a269308330c4aaa8ac6f3c/cassandra_driver-3.24.0-cp27-cp27mu-manylinux1_x86_64.whl (3.5MB)
    100% || 3.5MB 411kB/s
Collecting geomet<0.3,>=0.1 (from cassandra-driver)
  Downloading https://files.pythonhosted.org/packages/cf/21/58251b3de99e0b5ba649ff511f7f9e8399c3059dd52a643774106e929afa/geomet-0.2.1.post1.tar.gz
Collecting futures (from cassandra-driver)
  Downloading https://files.pythonhosted.org/packages/d8/a6/f46ae3f1da0cd4361c344888f59ec2f5785e69c872e175a748ef6071cdb5/futures-3.3.0-py2-none-any.whl
Collecting six>=1.9 (from cassandra-driver)
  Downloading https://files.pythonhosted.org/packages/ee/ff/48bde5c0f013094d729fe4b0316ba2a24774b3ff1c52d924a8a4cb04078a/six-1.15.0-py2.py3-none-any.whl
Collecting click (from geomet<0.3,>=0.1->cassandra-driver)
  Downloading https://files.pythonhosted.org/packages/d2/3d/fa76db83bf75c4f8d338c2fd15c8d33fdd7ad23a9b5e57eb6c5de26b430e/click-7.1.2-py2.py3-none-any.whl (82kB)
    100% || 92kB 8.7MB/s
Installing collected packages: click, six, geomet, futures, cassandra-driver
  Running setup.py install for geomet ... done
Successfully installed cassandra-driver-3.24.0 click-7.1.2 futures-3.3.0 geomet-0.2.1.post1 six-1.15.0

[root@DooM3 ~]# pip show cassandra-driver
Metadata-Version: 2.1
Name: cassandra-driver
Version: 3.24.0
Summary: DataStax Driver for Apache Cassandra
Home-page: http://github.com/datastax/python-driver
Author: DataStax
Author-email: None
Installer: pip
License: UNKNOWN
Location: /usr/lib64/python2.7/site-packages
Requires: geomet, futures, six
Classifiers:
  Development Status :: 5 - Production/Stable
  Intended Audience :: Developers
  License :: OSI Approved :: Apache Software License
  Natural Language :: English
  Operating System :: OS Independent
  Programming Language :: Python
  Programming Language :: Python :: 2.7
  Programming Language :: Python :: 3.4
  Programming Language :: Python :: 3.5
  Programming Language :: Python :: 3.6
  Programming Language :: Python :: 3.7
  Programming Language :: Python :: 3.8
  Programming Language :: Python :: Implementation :: CPython
  Programming Language :: Python :: Implementation :: PyPy
  Topic :: Software Development :: Libraries :: Python Modules
```
---
