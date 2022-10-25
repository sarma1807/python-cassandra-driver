-------------------------------------------------------
-- lookup tables (mostly they stay static)
-------------------------------------------------------

-- create email_servers lookup table
CREATE TABLE sales.lookup_email_servers 
(
    id           int PRIMARY KEY,
    email_server text
) ;


-- create usa_states lookup table
CREATE TABLE sales.lookup_usa_states 
(
    id         int PRIMARY KEY,
    state_code text,
    state_name text
) ;


-- create product_categories lookup table
CREATE TABLE sales.lookup_product_categories 
(
    id               int PRIMARY KEY,
    product_category text
) ;


-- create user_platforms lookup table
CREATE TABLE sales.lookup_user_platforms 
(
    id       int PRIMARY KEY,
    platform text
) ;



-------------------------------------------------------
-- master tables (data will be generated via python code)
-------------------------------------------------------

-- create users table
CREATE TABLE sales.users 
(
    user_id           bigint PRIMARY KEY,
    user_email_id     text,
    user_name         text,
    user_phone_number text,
    user_platform     text,
    user_state_code   text
) ;


-- create products table
CREATE TABLE sales.products 
(
    product_id          bigint PRIMARY KEY,
    product_category    text,
    product_code        text,
    product_description text,
    product_name        text,
    product_price       decimal,
    product_qoh         bigint
) ;



-------------------------------------------------------
-- transaction tables (data will be generated via python code)
-------------------------------------------------------

-- create sales_orders table. 1 entry per order.
CREATE TABLE sales.sales_orders 
(
    order_date                      date,
    order_date_hour                 int,
    order_timestamp                 timestamp,
    order_actual_shipping_date      timestamp,
    order_code                      uuid,
    order_discount_percent          int,
    order_estimated_shipping_date   timestamp,
    order_grand_total               decimal,
    order_number_of_products        int,
    order_total                     decimal,
    user_email_id                   text,
    user_id                         bigint,
    user_name                       text,
    user_phone_number               text,
    user_platform                   text,
    user_state_code                 text,
    PRIMARY KEY ((order_date, order_date_hour), order_timestamp, order_code)
) WITH CLUSTERING ORDER BY (order_timestamp ASC, order_code ASC) ;


-- create sales_order_products table. 1 entry per each product sold via 1 order.
CREATE TABLE sales.sales_order_products 
(
    order_date              date,
    order_code              uuid,
    product_id              bigint,
    product_category        text,
    product_code            text,
    product_name            text,
    product_price_each      decimal,
    product_price_total     decimal,
    product_sold_quantity   int,
    PRIMARY KEY ((order_date, order_code), product_id)
) WITH CLUSTERING ORDER BY (product_id ASC) ;

    

-------------------------------------------------------
-- transaction tables TIME_TO_LIVE (TTL)
-- transaction tables might grow big quickly
-- use following settings to keep them under control
-------------------------------------------------------

-- Apache Cassandra TTL for tables is specified in seconds

-- keep data in following tables only for 15 days
-- TTL : 1296000 seconds = 15 days * 24 hours * 60 minutes * 60 seconds

ALTER TABLE sales.sales_orders WITH default_time_to_live = 1296000 ;

ALTER TABLE sales.sales_order_products WITH default_time_to_live = 1296000 ;

