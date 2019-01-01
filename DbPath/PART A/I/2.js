db.createCollection("EMPLOYEE")

db.EMPLOYEE.insert({"SSN":4567,"Name":'James',"DeptNo":'XYZ',"ProjectNo":101}) 
db.EMPLOYEE.insert({"SSN":3256, "Name":'Jack',"DeptNo" :'XYZ',"ProjectNo":102})

db.EMPLOYEE.find().pretty()
db.EMPLOYEE.find({"DeptNo":'XYZ'}).pretty()
db.EMPLOYEE.find({"ProjectNo":104}).pretty()
