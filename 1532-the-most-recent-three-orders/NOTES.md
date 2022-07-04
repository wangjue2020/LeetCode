ROW_NUMBER() OVER(PARTITION BY cu.customer_id ORDER BY ord.order_date desc)
按照cu.customer_id分组给row number
​
ROW_NUMBER() OVER( ORDER BY ord.order_date desc)
按照order_date 降序排序后给每一行赋予行数