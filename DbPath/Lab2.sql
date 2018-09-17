-- Creating table

create table employee
  (
    ssn integer primary key,
    name varchar2(20),
    dept_no integer
  );

-- Inserting values

insert into employee values(1,'Piyush',1);
  insert into employee values(2,'prajwal',2);
    insert into employee values(3,'mohit',3);
      insert into employee values(4,'Minhaas',4);
        insert into employee values(5,'Kumar',5);

-- showing the values

select * from employee;

-- Showing values order by ssn

select * from employee order by ssn;

-- Showing values order by Name

select * from employee order by Name;

-- Showing values where name is Piyush

select * from employee where name = "Piyush";

-- Made with love by Piyush Mehta
