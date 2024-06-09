### 2 sales summary tables

` sales_orders_hourly_summary ` &  ` sales_orders_daily_summary `

---

## sales_orders_hourly_summary table

```
TABLE sales_orders_hourly_summary
  PRIMARY KEY ((order_date, order_date_hour), order_code)
```

---

## sales_orders_daily_summary table

```
TABLE sales_orders_daily_summary
  PRIMARY KEY (order_date, order_code)
```

---
