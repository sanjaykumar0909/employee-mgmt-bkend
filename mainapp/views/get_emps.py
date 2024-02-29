from django.http import JsonResponse, HttpResponse
from mainapp.models import Employees

def handle(req):
    if req.method =="GET":
        emps= Employees.objects.all()
        send_data=[]
        for emp in emps:
            dct= dict()
            dct['employeeId'] = emp.emp_id
            dct['employeeName'] = emp.emp_name
            dct['department'] = emp.department
            dct['dob'] = emp.dob
            dct['gender'] = emp.gender
            dct['designation'] = emp.designation
            dct['joinDate']= emp.join_date
            dct['salary'] = emp.salary
            send_data.append(dct)
        print(send_data)
        return JsonResponse(send_data, safe=False)
    return HttpResponse("show-emps ONLY GET")