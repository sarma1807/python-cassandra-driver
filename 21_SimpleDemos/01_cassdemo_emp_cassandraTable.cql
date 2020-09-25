-- create a keyspace for python cassandra-driver demos
CREATE KEYSPACE cassdemo WITH replication = {'class': 'NetworkTopologyStrategy', 'east_dc': '2', 'west_dc': '2'} ;

-- if authentication is enabled on cassandra
CREATE ROLE demo_user WITH SUPERUSER = false AND LOGIN = true AND PASSWORD = 'PassCode' ;
GRANT select ON KEYSPACE cassdemo TO demo_user ;
GRANT modify ON KEYSPACE cassdemo TO demo_user ;
LIST ALL PERMISSIONS OF demo_user ;


-- create employees table
CREATE TABLE cassdemo.emp (
    empid int,
    first_name text,
    last_name text,
    PRIMARY KEY (empid)
) ;

-- insert some sample data into employees table
INSERT INTO cassdemo.emp (empid, first_name, last_name) VALUES (1001, 'Scott', 'Tiger') ;
INSERT INTO cassdemo.emp (empid, first_name, last_name) VALUES (1003, 'Queen', 'John') ;


SELECT * FROM cassdemo.emp ;
