-- PART(PNO, PNAME, COLOUR), 
-- SUPPLIER( SNO,SNAME,ADDRESS)
-- SUPPLY(PNO,SNO,QUANTITY)
--  Create the above tables, insert suitable tuples and perform the following operations in SQL:
-- Obtain the PNO of parts supplied by supplier ‘Ram’.
-- Obtain the Names of suppliers who supply bolts
-- Delete the parts which are green in colour

create table part
(
  pno number(10),
  pname varchar(20),
  colour varchar(20),
  primary key(pno)
);

Create table supplier
(
  sno number(10),
  sname varchar(20),
  address varchar(20),
  primary key(sno)
);

create table supply
(
  pno number(10),
  sno number(10),
  quantity varchar(20),
  primary key(pno,sno)
  foreign key
  (pno) references part
  foreign key (sno) references
  supplier
);

  
insert into part
values(1, 'plug', 'black');

insert into part
values(2, 'bolt', 'blue');


insert into part
values(3, 'nut', 'green');


insert into supplier
values(10, 'Anoop', 'udupi');

insert into supplier
values(15, 'Bharath', 'mangalore');

insert into supplier
values(20, 'Ram', 'bangalore');

insert into supply
values(1, 10, 50);


insert into supply
values(2, 10, 30);


insert into supply
values(1, 15, 70);

insert into supply
values(3, 15, 40);


insert into supply
values(1, 20, 55);


insert into supply
values(2, 20, 65);


insert into supply
values(3, 20, 75);

select *
from part;

select *
from supply ;

select * from supplier;

select pno from supply where sno=(select sno from supplier where sname="Ram");

select sname from supplier where sno=(select sno from supply where pno=(select pno from part where pname='bolt'));

delete from part where pname="green";
