-- 1.Consider the relations --
--EMPLOYEE(SSN, Name, DeptNo), --
--ASSIGNED_TO(USN , ProjectNo) 
--PROJECT(ProjectNo, ProjectArea). 
--Create the above tables, insert suitable tuples and perform the following operations in SQL: 
--Obtain the SSN of employees assigned to database projects.
--Find the number of employees working in each department
--Update the ProjectNo of Employee bearing SSN=1 to ProjectNo=20
--create table employee(ssn varchar(6),name varchar(10),deptno int, primary key(ssn));

create table project(projectno varchar(10),projectarea varchar(20),primary key(projectno));

create table assigned_to(ssn varchar(6),projectno varchar(10),foreign key(ssn)references employee(ssn),foreign key(projectno)references p(projectno));

insert into employee values('01','abc',10);

insert into employee values('02','xyz',20);

insert into employee values('03','pqr',30);

insert into employee values('04','lmn',40);

insert into project values('100','database');

insert into project values('200','network');

insert into project values('300','android');

insert into assigned_to values('01','100');

insert into assigned_to values('02','200');

insert into assigned_to values('03','300');

insert into assigned_to values('01','200');

--a
SELECT ssn from assigned_to where ProjectNo = (Select ProjectNo from project where ProjectArea='database');
--b
select count(ssn),deptno from employee group by deptno;
--c
UPDATE ASSIGNED_TO SET ProjectNo=20 WHERE SSN=1;
