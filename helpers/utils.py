import csv

def rdData(self):
    employees = []
    with open(DBFile, 'r') as csvfile:
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