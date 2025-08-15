create table test.customers  (customer_name varchar(30));

insert into test.customers values ('Ankit Bansal')
,('Vishal Pratap Singh')
,('Michael'); 

SELECT * FROM test.customers;

SELECT *,
       CHAR_LENGTH(customer_name) - CHAR_LENGTH(REPLACE(customer_name, ' ', '')) AS no_of_spaces
FROM customers;

drop table test.customers;
