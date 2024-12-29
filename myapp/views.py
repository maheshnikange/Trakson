from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from .models import CompanyMaster, BranchMaster, CustomerMaster,DesignationMaster,EmployeeMaster,ProjectMaster,UserRegistration
from .forms import CompanyMasterForm, BranchMasterForm, CustomerMasterForm,DesignationMasterForm,EmployeeMasterForm,ProjectMasterForm,UserRegistrationForm
import json

# Helper function to parse JSON requests
def parse_json_request(request):
    try:
        return json.loads(request.body)
    except json.JSONDecodeError:
        return None


# CompanyMaster CRUD Views
@csrf_exempt
def company_list(request):
    if request.method == "GET":
        companies = list(CompanyMaster.objects.values())
        return JsonResponse({"companies": companies}, safe=False)

    return JsonResponse({"error": "GET method expected"}, status=400)


@csrf_exempt
def company_create(request):
    if request.method == "POST":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = CompanyMasterForm(data)
        if form.is_valid():
            company = form.save()
            return JsonResponse({"message": "Company created", "company_id": company.company_master_id}, status=201)

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)


@csrf_exempt
def company_detail(request, pk):
    company = get_object_or_404(CompanyMaster, pk=pk)

    if request.method == "GET":
        return JsonResponse({"company": model_to_dict(company)})

    if request.method == "PUT":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = CompanyMasterForm(data, instance=company)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Company updated"})

        return JsonResponse({"error": form.errors}, status=400)

    if request.method == "DELETE":
        company.delete()
        return JsonResponse({"message": "Company deleted"})

    return JsonResponse({"error": "Method not allowed"}, status=405)


# BranchMaster CRUD Views
@csrf_exempt
def branch_list(request):
    if request.method == "GET":
        branches = list(BranchMaster.objects.values())
        return JsonResponse({"branches": branches}, safe=False)

    return JsonResponse({"error": "GET method expected"}, status=400)


@csrf_exempt
def branch_create(request):
    if request.method == "POST":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = BranchMasterForm(data)
        if form.is_valid():
            branch = form.save()
            return JsonResponse({"message": "Branch created", "branch_id": branch.branch_master_id}, status=201)

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)


@csrf_exempt
def branch_detail(request, pk):
    branch = get_object_or_404(BranchMaster, pk=pk)

    if request.method == "GET":
        return JsonResponse({"branch": model_to_dict(branch)})

    if request.method == "PUT":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = BranchMasterForm(data, instance=branch)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Branch updated"})

        return JsonResponse({"error": form.errors}, status=400)

    if request.method == "DELETE":
        branch.delete()
        return JsonResponse({"message": "Branch deleted"})

    return JsonResponse({"error": "Method not allowed"}, status=405)


# CustomerMaster CRUD Views
@csrf_exempt
def customer_list(request):
    if request.method == "GET":
        customers = list(CustomerMaster.objects.values())
        return JsonResponse({"customers": customers}, safe=False)

    return JsonResponse({"error": "GET method expected"}, status=400)


@csrf_exempt
def customer_create(request):
    if request.method == "POST":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = CustomerMasterForm(data)
        if form.is_valid():
            customer = form.save()
            return JsonResponse({"message": "Customer created", "customer_id": customer.customer_master_id}, status=201)

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)


@csrf_exempt
def customer_detail(request, pk):
    customer = get_object_or_404(CustomerMaster, pk=pk)

    if request.method == "GET":
        return JsonResponse({"customer": model_to_dict(customer)})

    if request.method == "PUT":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = CustomerMasterForm(data, instance=customer)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Customer updated"})

        return JsonResponse({"error": form.errors}, status=400)

    if request.method == "DELETE":
        customer.delete()
        return JsonResponse({"message": "Customer deleted"})

    return JsonResponse({"error": "Method not allowed"}, status=405)



@csrf_exempt
def designation_list(request):
    if request.method == "GET":
        designations = list(DesignationMaster.objects.values())
        return JsonResponse({"designations": designations}, safe=False)
    return JsonResponse({"error": "GET method expected"}, status=400)


@csrf_exempt
def designation_create(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = DesignationMasterForm(data)
        if form.is_valid():
            designation = form.save()
            return JsonResponse({"message": "Designation created", "designation_id": designation.designation_id}, status=201)
        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)

@csrf_exempt
def designation_update(request, designation_id):
    if request.method == "PUT":
        try:
            designation = DesignationMaster.objects.get(designation_id=designation_id)
        except DesignationMaster.DoesNotExist:
            return JsonResponse({"error": "Designation not found"}, status=404)

        data = json.loads(request.body)
        for key, value in data.items():
            setattr(designation, key, value)
        designation.save()

        return JsonResponse({"message": "Designation updated successfully!"}, status=200)

    return JsonResponse({"error": "PUT method expected"}, status=400)

@csrf_exempt
def designation_delete(request, designation_id):
    if request.method == "DELETE":
        try:
            designation = DesignationMaster.objects.get(designation_id=designation_id)
            designation.delete()
            return JsonResponse({"message": "Designation deleted successfully!"})
        except DesignationMaster.DoesNotExist:
            return JsonResponse({"error": "Designation not found"}, status=404)

    return JsonResponse({"error": "DELETE method expected"}, status=400)

@csrf_exempt
def employee_list(request):
    if request.method == "GET":
        employees = list(EmployeeMaster.objects.values())
        return JsonResponse({"employees": employees}, safe=False)
    return JsonResponse({"error": "GET method expected"}, status=400)



@csrf_exempt
def employee_create(request):
    if request.method == "POST":
        data = json.loads(request.body)

        # Print incoming data for debugging
        print("Received data:", data)

        # If using ForeignKey relations, ensure the IDs are provided in the data
        data['company'] = CompanyMaster.objects.get(id=data['company_id']) if 'company_id' in data else None
        data['branch'] = BranchMaster.objects.get(id=data['branch_id']) if 'branch_id' in data else None
        data['project'] = ProjectMaster.objects.get(id=data['project_id']) if 'project_id' in data else None
        data['username'] = UserRegistration.objects.get(id=data['username_id']) if 'username_id' in data else None

        form = EmployeeMasterForm(data)
        if form.is_valid():
            employee = form.save()
            return JsonResponse({"message": "Employee created", "employee_id": employee.id}, status=201)
        else:
            print("Form errors:", form.errors)
            return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)

@csrf_exempt
def employee_update(request, employee_code):
    if request.method == "PUT":
        try:
            employee = EmployeeMaster.objects.get(employee_code=employee_code)
        except EmployeeMaster.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)

        data = json.loads(request.body)

        # Update fields in the Employee object
        for key, value in data.items():
            if hasattr(employee, key):
                setattr(employee, key, value)

        # Handle ForeignKey relationships
        if 'branch_id' in data:
            try:
                branch = BranchMaster.objects.get(id=data['branch_id'])
                employee.branch = branch
            except BranchMaster.DoesNotExist:
                return JsonResponse({"error": "Branch not found"}, status=404)

        if 'company_id' in data:
            try:
                company = CompanyMaster.objects.get(id=data['company_id'])
                employee.company = company
            except CompanyMaster.DoesNotExist:
                return JsonResponse({"error": "Company not found"}, status=404)

        if 'project_id' in data:
            try:
                project = ProjectMaster.objects.get(id=data['project_id'])
                employee.project = project
            except ProjectMaster.DoesNotExist:
                return JsonResponse({"error": "Project not found"}, status=404)

        if 'username_id' in data:
            try:
                user = UserRegistration.objects.get(id=data['username_id'])
                employee.username = user
            except UserRegistration.DoesNotExist:
                return JsonResponse({"error": "User not found"}, status=404)

        employee.save()

        return JsonResponse({"message": "Employee updated successfully!"}, status=200)

    return JsonResponse({"error": "PUT method expected"}, status=400)
@csrf_exempt
def employee_delete(request, employee_code):
    if request.method == "DELETE":
        try:
            employee = EmployeeMaster.objects.get(employee_code=employee_code)
        except EmployeeMaster.DoesNotExist:
            return JsonResponse({"error": "Employee not found"}, status=404)

        employee.delete()
        return JsonResponse({"message": "Employee deleted successfully!"}, status=200)

    return JsonResponse({"error": "DELETE method expected"}, status=400)
@csrf_exempt
def employee_detail(request, employee_code):
    pass
    # try:
    #     employee = EmployeeMaster.objects.select_related(
    #         'company', 'branch', 'reporting_branch', 'project', 'username'
    #     ).get(employee_code=employee_code)
    # except EmployeeMaster.DoesNotExist:
    #     return JsonResponse({"error": "Employee not found"}, status=404)

    # if request.method == "GET":
    #     # Return employee data along with related objects as JSON
    #     return JsonResponse({
    #         "employee": model_to_dict(employee, fields=['employee_master_id', 'employee_code', 'employee_name', 'company__name', 'branch__name', 'project__name', 'username__username'])
    #     })

    # return JsonResponse({"error": "Method not allowed"}, status=405)

# ----------project-----------
# List all projects
@csrf_exempt
def project_list(request):
    if request.method == "GET":
        projects = list(ProjectMaster.objects.values())
        return JsonResponse({"projects": projects}, safe=False)

    return JsonResponse({"error": "GET method expected"}, status=400)


# Create a new project
@csrf_exempt
def project_create(request):
    if request.method == "POST":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = ProjectMasterForm(data)
        if form.is_valid():
            project = form.save()
            return JsonResponse({"message": "Project created", "project_id": project.project_master_id}, status=201)

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)


# Retrieve a specific project by ID
@csrf_exempt
def project_detail(request, project_id):
    try:
        project = ProjectMaster.objects.get(project_master_id=project_id)
    except ProjectMaster.DoesNotExist:
        return JsonResponse({"error": "Project not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"project": model_to_dict(project)})

    return JsonResponse({"error": "GET method expected"}, status=400)


# Update a specific project by ID
@csrf_exempt
def project_update(request, project_id):
    try:
        project = ProjectMaster.objects.get(project_master_id=project_id)
    except ProjectMaster.DoesNotExist:
        return JsonResponse({"error": "Project not found"}, status=404)

    if request.method == "PUT":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = ProjectMasterForm(data, instance=project)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Project updated"})

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "PUT method expected"}, status=400)


# Delete a specific project by ID
@csrf_exempt
def project_delete(request, project_id):
    try:
        project = ProjectMaster.objects.get(project_master_id=project_id)
    except ProjectMaster.DoesNotExist:
        return JsonResponse({"error": "Project not found"}, status=404)

    if request.method == "DELETE":
        project.delete()
        return JsonResponse({"message": "Project deleted"})

    return JsonResponse({"error": "DELETE method expected"}, status=400)


# List all users
@csrf_exempt
def user_list(request):
    if request.method == "GET":
        users = list(UserRegistration.objects.values())
        return JsonResponse({"users": users}, safe=False)

    return JsonResponse({"error": "GET method expected"}, status=400)


# Create a new user
@csrf_exempt
def user_create(request):
    if request.method == "POST":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = UserRegistrationForm(data)
        if form.is_valid():
            user = form.save()
            return JsonResponse({"message": "User created", "user_id": user.user_id}, status=201)

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "POST method expected"}, status=400)


# Retrieve a specific user by ID
@csrf_exempt
def user_detail(request, user_id):
    try:
        user = UserRegistration.objects.get(user_id=user_id)
    except UserRegistration.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    if request.method == "GET":
        return JsonResponse({"user": model_to_dict(user)})

    return JsonResponse({"error": "GET method expected"}, status=400)


# Update a specific user by ID
@csrf_exempt
def user_update(request, user_id):
    try:
        user = UserRegistration.objects.get(user_id=user_id)
    except UserRegistration.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    if request.method == "PUT":
        data = parse_json_request(request)
        if not data:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        form = UserRegistrationForm(data, instance=user)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "User updated"})

        return JsonResponse({"error": form.errors}, status=400)

    return JsonResponse({"error": "PUT method expected"}, status=400)


# Delete a specific user by ID
@csrf_exempt
def user_delete(request, user_id):
    try:
        user = UserRegistration.objects.get(user_id=user_id)
    except UserRegistration.DoesNotExist:
        return JsonResponse({"error": "User not found"}, status=404)

    if request.method == "DELETE":
        user.delete()
        return JsonResponse({"message": "User deleted"})

    return JsonResponse({"error": "DELETE method expected"}, status=400)



