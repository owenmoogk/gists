select 
	orderId, 
	orderDate,
	orderTotal,
	Orders.customerID as [Order Table Customer Id],
	Customers.customerID as [Customer Table Customer ID],
	customerName,
	phone
from dbo.orders left outer join dbo.customers on dbo.Orders.customerID = dbo.customers.customerId

order by OrderTotal desc