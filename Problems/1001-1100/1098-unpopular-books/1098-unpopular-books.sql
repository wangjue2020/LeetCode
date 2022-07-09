select books.book_id,name
from books left join orders on books.book_id = orders.book_id 
and orders.dispatch_date >= date('2018-06-23')
where available_from < date('2019-05-23')
group by books.book_id
having sum(ifnull(quantity,0))< 10