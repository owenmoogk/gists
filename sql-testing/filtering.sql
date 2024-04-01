select * from kcc.dbo.customers
where CustomerName like 'A%' and
	(country = 'United States' or Country = 'France')