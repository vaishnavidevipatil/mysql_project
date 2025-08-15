SELECT *,
       CHAR_LENGTH(customer_name) - CHAR_LENGTH(REPLACE(customer_name, ' ', '')) AS no_of_spaces,
       INSTR(customer_name, ' ') AS first_space_position,
       INSTR(SUBSTRING(customer_name, INSTR(customer_name, ' ') + 1), ' ') + INSTR(customer_name, ' ') AS second_space_position
FROM customers;