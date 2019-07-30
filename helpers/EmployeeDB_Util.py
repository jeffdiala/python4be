import csv

class EmployeeDB_Util():
    def __init__(self, external_file):
        self.DBFile = external_file

    def searchEmployee(self, name):
        employeeList = self.rdData()
        foundList =[]
        for employee in employeeList:
            for k, v in employee.items():
                if(name.lower() in v.lower() or name.lower() in v.lower().split(" ")):
                    foundList.append(employee)
        return foundList

    def addEmployee(self, fname, lname, employeeNo, emailAdd):
        newRow = [{'fname' : fname, 'lname' : lname, 'employeeNo' : employeeNo, 'emailAdd' : emailAdd}]
        self.wrData(mode='a', newRow=newRow)

    def removeEmployee(self, employeeNo):
        newList = []
        remList = dict()
        employeeList = self.rdData()
        successFlag = False
        for employee in employeeList:
            if(employee['employeeNo'] == employeeNo):
                remList = dict(employee)
                successFlag = True
            else:
                newList.append(employee)
        self.wrData(mode='w', newRow=newList)
        return successFlag, remList

    def rdData(self):
        employees = []
        with open(self.DBFile, 'r') as csvfile:
            reader = csv.DictReader(csvfile, ['fname', 'lname', 'employeeNo', 'emailAdd'])
            for row in reader:
                employees.append(row)
        return employees


    def wrData(self, mode='w', newRow=[]):
        with open(self.DBFile, mode, newline='') as csvfile:
            writer = csv.DictWriter(csvfile, ['fname', 'lname', 'employeeNo', 'emailAdd'])
            if (len(newRow) <= 1):
                writer.writerow(newRow[0])
            else:
                writer.writerows(newRow)
