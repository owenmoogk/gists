select OrderDate as [Order Date], CustomerID, OrderTotal
from kcc.dbo.orders
where ordertotal between 1000 and 2000