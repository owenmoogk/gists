select count(*) from dbo.orders
--where OrderDate >= Dateadd(month, -1, getDate())

select sum(orderTotal) from dbo.orders
--where OrderDate >= Dateadd(month, -1, getDate())
group by CustomerID