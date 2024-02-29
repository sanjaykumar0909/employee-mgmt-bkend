from datetime import datetime
from .generate_dates import generate_dates
from mainapp.models import Employees
def run():
  data = [
    {
      "employeeId": 14,
      "employeeName": "Isaac",
      "department": "department1",
      "dob": "1985-06-30",
      "gender": "male",
      "designation": "Software engineer",
      "salary": 1250000
    },
    {
      "employeeId": 15,
      "employeeName": "Jenny",
      "department": "department2",
      "dob": "1983-10-18",
      "gender": "female",
      "designation": "Web developer",
      "salary": 1050000
    },
    {
      "employeeId": 16,
      "employeeName": "Kevin",
      "department": "department3",
      "dob": "1991-02-27",
      "gender": "male",
      "designation": "System admin",
      "salary": 1100000
    },
    {
      "employeeId": 17,
      "employeeName": "Linda",
      "department": "department1",
      "dob": "1986-05-17",
      "gender": "female",
      "designation": "ML analyst",
      "salary": 980000
    },
    {
      "employeeId": 18,
      "employeeName": "Michael",
      "department": "department2",
      "dob": "1984-09-09",
      "gender": "male",
      "designation": "Web developer",
      "salary": 1150000
    },
    {
      "employeeId": 19,
      "employeeName": "Nancy",
      "department": "department3",
      "dob": "1994-11-23",
      "gender": "female",
      "designation": "Software engineer",
      "salary": 950000
    }
  ]
  for i in data:
    Employees(
      emp_id=int(i['employeeId']),
      emp_name=i['employeeName'],
      department=i['department'],
      dob=datetime.strptime(i['dob'], "%Y-%m-%d"),
      gender=i['gender'],
      designation=i['designation'],
      salary=int(i['salary']),
      join_date=generate_dates()
    ).save()