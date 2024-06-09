### 2 sales summary tables

` sales_orders_hourly_summary ` &  ` sales_orders_daily_summary `

---

## sales_orders_hourly_summary table

```
TABLE sales_orders_hourly_summary
  PRIMARY KEY ((order_date, order_date_hour), order_code)
```

```
SELECT order_date, order_date_hour 
FROM sales.sales_orders_hourly_summary 
LIMIT 1 ;
```

###### sample output :

```
cqlsh> SELECT order_date, order_date_hour
   ... FROM sales.sales_orders_hourly_summary
   ... LIMIT 1 ;

 order_date | order_date_hour
------------+-----------------
 2024-06-09 |              17

(1 rows)

cqlsh>
```

```
SELECT order_date, order_date_hour, 
sum(order_grand_total) as sum_order_grand_total 
FROM sales.sales_orders_hourly_summary 
WHERE order_date = '2024-06-09' AND order_date_hour = 17 ;
```

###### sample output :

```
cqlsh> SELECT order_date, order_date_hour,
   ... sum(order_grand_total) as sum_order_grand_total
   ... FROM sales.sales_orders_hourly_summary
   ... WHERE order_date = '2024-06-09' AND order_date_hour = 17 ;

 order_date | order_date_hour | sum_order_grand_total
------------+-----------------+-----------------------
 2024-06-09 |              17 |            44292.4273

(1 rows)

cqlsh>
```

---

## sales_orders_daily_summary table

```
TABLE sales_orders_daily_summary
  PRIMARY KEY (order_date, order_code)
```

```
SELECT order_date 
FROM sales.sales_orders_daily_summary 
LIMIT 1 ;
```

###### sample output :

```
cqlsh> SELECT order_date
   ... FROM sales.sales_orders_daily_summary
   ... LIMIT 1 ;

 order_date
------------
 2024-06-09

(1 rows)

cqlsh>
```

```
SELECT order_date, 
sum(order_grand_total) as sum_order_grand_total 
FROM sales.sales_orders_daily_summary 
WHERE order_date = '2024-06-09' ;
```

###### sample output :

```
cqlsh> SELECT order_date,
   ... sum(order_grand_total) as sum_order_grand_total
   ... FROM sales.sales_orders_daily_summary
   ... WHERE order_date = '2024-06-09' ;

 order_date | sum_order_grand_total
------------+-----------------------
 2024-06-09 |         11419628.7104

(1 rows)

cqlsh>
```

---
