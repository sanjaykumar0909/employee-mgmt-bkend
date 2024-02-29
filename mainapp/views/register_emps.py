from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from mainapp.models import Employees
from datetime import datetime
@csrf_exempt
def handle(request):
    if request.method == 'POST':
        if request.body:
            # Decode the JSON
            json_data = json.loads(request.body)
            print(json_data)
            for emp in json_data:
                employee_name = emp.get('employeeName')
                employee_id = int(emp.get('employeeId'))
                department = emp.get('department')
                dob= datetime.strptime(emp.get('dob'), "%Y-%m-%d")
                gender= emp.get('gender')
                designation= emp.get('designation')
                salary= int(emp.get('salary'))

                Employees(emp_id= employee_id,
                    emp_name=employee_name,
                    department= department,
                    dob= dob,
                    gender=gender,
                    designation= designation,
                    salary= salary,
                    join_date= datetime.now()
                ).save()
            return JsonResponse({'message': 'Data received successfully'})
        else:
            return JsonResponse({'error': 'No JSON data provided'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
