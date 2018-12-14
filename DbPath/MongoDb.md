1. Create the below tables, insert suitable tuples and perform the following  operations using  MongoDB
EMPLOYEE (SSN, Name, DeptNo)
ASSIGNED_TO (USN , ProjectNo) 
a. List all the employees of department “XYZ”.
b. Name the employees working on Project Number :#PNo


Solution

Create the collection:
db.createCollection("EMPLOYEE")

Inserting the values:

>db.EMPLOYEE.insert({"SSN":4567,"Name":'James',"DeptNo":'XYZ',"ProjectNo":101})
>db.EMPLOYEE.insert({"SSN":3256,"Name":'Jack',"DeptNo":'XYZ',"ProjectNo":102})

>db.EMPLOYEE.find().pretty()
> db.EMPLOYEE.find({"DeptNo":'XYZ'}).pretty()
> db.EMPLOYEE.find({"ProjectNo":104}).pretty()

2. Create the below tables, insert suitable tuples and perform the following operations using  MongoDB
PART (PNO,PNAME, COLOUR), 
SUPPY (SNO, SNAME, PNO, ADDRESS)
a. Update the parts identifier 
b. Display all suppliers who supply the part with part identifier: #PNO


Solution:

Create the collection:
 >db.createCollection("WAREHOUSE")

Inserting the values:

>db.WAREHOUSE.insert({"PNO":1947,"Pname":'bolts',"Colour":'Black',"SNO":1234,"Sname":'ABC',"Address":'blore'})
>db.WAREHOUSE.insert({"PNO":1950,"Pname":'chain',"Colour":'Blue',"SNO":4567,"Sname":'DEF',"Address":'chen'})


>db.WAREHOUSE.find().pretty()

> db.WAREHOUSE.update({"PNO":1950},{$set:{"PNO":2017}},{multi:true})
>db.WAREHOUSE.find().pretty()


> db.WAREHOUSE.find({"PNO":2017}).pretty()



3. Create the below tables, insert suitable tuples and perform the following operations using  MongoDB
BOAT (BID, BNAME, COLOUR)
RESERVES (BID, SNAME, SID, DAY)
a. Obtain the number of boats obtained by sailor :#sname
b. Retrieve boats of color :”White”


Create the collection:
> db.createCollection("BOATRES")

Insert the values:
>db.BOATRES.insert({"BID":9988,"BNAME":'ABC',"COLOUR":'Black',"SNAME":'John',"SID":1234,"DAY":'2017-12-25'})
>db.BOATRES.insert({"BID":8877,"BNAME":'DEF',"COLOUR":'Black',"SNAME":'Smith',"SID":4567,"DAY":'2017-11-24'})


> db.BOATRES.find({"SNAME":'Sucre'}).count()
> db.BOATRES.find({"COLOUR":'Black'}).pretty()




4.Create the below tables, insert suitable tuples
and perform the following operations using  MongoDB
PART (PNO, PNAME, COLOUR)
SHIPMENT (PNO, WNO, WNAME, QUANTITY, DATE)
a.Find the parts shipped from warehouse :Wname”
b.List the total quantity supplied from each warehouse 



Create the collection:
>db.createCollection("SHIPMENT")


Insert the values:
>db.SHIPMENT.insert({"PNO":11,"PNAME":'bolts',"COLOUR":'Black',"WNO":99,"WNAME":'ABC',"QUANTITY":45,"DATE":'2017-09-25'})
>db.SHIPMENT.insert({"PNO":12,"PNAME":'nuts',"COLOUR":'Black',"WNO":99,"WNAME":'ABC',"QUANTITY":38,"DATE":'2017-09-28'})




> db.SHIPMENT.find().pretty()
>db.SHIPMENT.find({"WNAME":'ABC'}).pretty()
>db.SHIPMENT.aggregate([{ $group:{_id:"$WNAME",total:{$sum:"$QUANTITY"}}}])





5.Create the below tables, insert suitable tuples and perform the following operations using  MongoDB
BOOK (ISBN, TITLE, AUTHOR, PUBLISHER)
BORROW (ISBN, USN, DATE)
a.Obtain the name of the student who has borrowed the book bearing ISBN "123‟ 
b.Obtain the Names of students who have borrowed database books.



Solution:

Create the collection:
>db.createCollection("LIBRARY")


Insert the values:

>db.LIBRARY.insert({"ISBN":1122,"TITLE":'datbase',"AUTHOR":'ABC',"PUBLISHER":'selina',"SSN":2015,"date":'2017-05-29'})
>db.LIBRARY.insert({"ISBN":2233,"TITLE":'datbase',"AUTHOR":'DEF',"PUBLISHER":'mcgraw',"SSN":2016,"date":'2017-06-29' })



>db.LIBRARY.find().pretty()
>db.LIBRARY.find({"ISBN":1122},{"SSN":1,_id:0}).pretty()
>db.LIBRARY.find({"TITLE":'datbase'},{"SSN":1,_id:0}).pretty()
