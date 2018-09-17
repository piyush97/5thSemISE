-- Creating table

CREATE TABLE employee ( ssn integer PRIMARY KEY,
                                            name varchar2(20),
                                                 dept_no integer );

-- Inserting values

INSERT INTO employee
VALUES(1,
       'Piyush',
       1);


INSERT INTO employee
VALUES(2,
       'prajwal',
       2);


INSERT INTO employee
VALUES(3,
       'mohit',
       3);


INSERT INTO employee
VALUES(4,
       'Minhaas',
       4);


INSERT INTO employee
VALUES(5,
       'Kumar',
       5);

-- showing the values

SELECT *
FROM employee;

-- Showing values order by ssn

SELECT *
FROM employee
ORDER BY ssn;

-- Showing values order by Name

SELECT *
FROM employee
ORDER BY Name;

-- Showing values where name is Piyush

SELECT *
FROM employee
WHERE name = "Piyush";

-- Made with love by Piyush Mehta
