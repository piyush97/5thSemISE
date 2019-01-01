CREATE TABLE PART (
PNO int,
PNAME VARCHAR2(10),
COLOUR VARCHAR2(10),
PRIMARY KEY (PNO)
);

create table Warehouse(
wno int,
wname varchar(10),
city varchar(20),
primary key(wno)
);

create table shipment(
pno int,
wno int,
quantity int,
shipdate date,
foreign key(pno) references part(pno),
foreign key(wno) references warehouse(wno)
);

insert into part values(1,'hello','red');
insert into part values(2,'hel22','red');
insert into part values(3,'hel22','blue');
insert into warehouse values(1,'housii','delhi');
insert into warehouse values(2,'karkhana','bangalore');
insert into shipment values(1,2,12,'2018-10-20');
insert into shipment values (2,3,122,'2018-12-23');

select wname from warehouse where wno=(select wno from shipment where pno=(select pno from part where colour='red'));

select pno from part where pno=(select pno from shipment where wno=(select wno from warehouse group by wname));

select count(pno) from part where pno=(select pno from shipment where wno=(select wno from warehouse group by wname));
