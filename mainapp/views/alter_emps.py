from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse, HttpResponse
from mainapp.models import Employees
@csrf_exempt
def handle(req):
    if req.method == 'POST':
        data= json.loads(req.body)['rmList']
        # print(data, type(data), type(data[0]))
        Employees.objects.filter(emp_id__in=data).delete()# filters all employees whose emp_id is in the list `data` and deletes them all
        emps = Employees.objects.all()
        send_data = []
        for emp in emps:
            dct = dict()
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
    return HttpResponse("manage-emps/ ONLY POST")