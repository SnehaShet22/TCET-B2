select == SELECT 
SQL IS NOT CASE SENSITIVE 

SELECT emp_name FROM employee

SELECT DISTINCT col_name FROM table_name: unique values (no duplicates)

SELECT COUNT (DISTINCT name) FROM demo 
/ SELECT COUNT (*) FROM (SELECT DISTINCT name FROM demo);

SELECT emp_name FROM employee
WHERE name LIKE = 'a%' (starts from a)

SELECT emp_name FROM employee
WHERE name LIKE = '%a' (ends with a)

SELECT emp_name FROM employee
WHERE name LIKE = '%a%' (a is present in string )

SELECT emp_name FROM employee
WHERE name LIKE = 'a%o' (starts with a and ends with o )

SELECT emp_name FROM employee
WHERE name LIKE = '%a_' (a is 2nd last character)

SELECT emp_name FROM employee
WHERE name NOT LIKE = 'a%' (everything which doesnt starts with a)

SELECT emp_name FROM employee
WHERE name ='something' or city = 'something' 

SELECT emp_name FROM employee
WHERE name ='something' AND city = 'something' 

SELECT emp_name FROM employee
WHERE not name ='something' 

SELECT col1 , col2 ,...
FROM table_name
ORDER BY col1 , col2 ,...
ASC|DESC ;


INSERT INTO table_name (col1 , col2 ,...)
VALUES (val1 , val2 ,...)


INSERT INTO table_name 
VALUES (val1 , val2 ,...)


UPDATE table_name
SET col1=val1 , col2=val2,...
WHERE condition;    # if you dont use WHERE it will update whole column 

DELETE FROM table_name WHERE condition;  # if you dont use WHERE it will clear whole table 

SELECT MIN(col_name) FROM table_name WHERE condition;(where is optional)
SELECT MAX(col_name) FROM table_name WHERE condition;(where is optional)
SELECT COUNT(col_name) FROM table_name WHERE condition;(where is optional)
SELECT AVG(col_name) FROM table_name WHERE condition;(where is optional)

LIKE (%) , (_)
% sign represents zero , one or multiple characters
_ sign represents one single character

SELECT col1,col2
FROM table_name
WHERE colN LIKE pattern 