/* select * from dbo.customers
where state = 'WA'
or customerId >=  4
-- only getting the customers from washington

order by customerId desc 

*/

select * from dbo.customers
where 
	state not in ('WA', 'NY', 'UT')
	and (country = 'United States' or country = 'France')