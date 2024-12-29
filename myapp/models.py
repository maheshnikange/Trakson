from django.db import models
from django.utils.timezone import now
from django.core.validators import MinLengthValidator

class UserRegistration(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, unique=True, null=False)
    email = models.EmailField(unique=True, null=False)
    password_hash = models.TextField(null=False)  # Store hashed password
    mobile_number = models.CharField(max_length=15, unique=True, null=True, blank=True)
    title = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    date_of_birth = models.DateField(null=True, blank=True)
    profile_picture_url = models.TextField(null=True, blank=True)
    gender = models.CharField(
        max_length=10,
        choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')],
        null=True,
        blank=True,
    )
    street_address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=now, null=False)
    updated_at = models.DateTimeField(default=now, null=True, blank=True)
    status = models.CharField(max_length=20, default="active", null=False)
    role = models.CharField(max_length=20, default="user", null=False)
    last_login = models.DateTimeField(default=now, null=True, blank=True)
    failed_login_attempts = models.IntegerField(default=0, null=False)
    account_locked = models.BooleanField(default=False, null=False)
    lock_time = models.DateTimeField(null=True, blank=True)
    auth_token = models.TextField(null=True, blank=True)
    two_fa_enabled = models.BooleanField(default=False, null=False)
    language = models.CharField(max_length=10, default="en", null=False)
    timezone = models.CharField(max_length=50, default="UTC", null=False)
    notification_preferences = models.JSONField(default=dict, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    social_links = models.JSONField(default=dict, null=True, blank=True)
    subscription_status = models.CharField(max_length=50, null=True, blank=True)
    custom_attributes = models.JSONField(default=dict, null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(
                check=models.Q(gender__in=["male", "female", "other"]),
                name="check_gender_valid",
            )
        ]

    def __str__(self):
        return self.username



class CompanyMaster(models.Model):
    company_master_id = models.AutoField(primary_key=True)
    company_code = models.CharField(max_length=8, unique=True)
    company_type = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    company_phone_number = models.CharField(max_length=15)
    company_email = models.EmailField(max_length=100)
    fax_number = models.CharField(max_length=20, null=True, blank=True)
    gst_number = models.CharField(max_length=30, null=True, blank=True)
    tan_no = models.CharField(max_length=30, null=True, blank=True)
    pan_no = models.CharField(max_length=30, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    industry_type = models.CharField(max_length=100)
    registration_number = models.CharField(max_length=50)
    incorporation_date = models.DateField()
    company_size = models.CharField(max_length=50, null=True, blank=True)
    parent_company_code = models.CharField(max_length=8, null=True, blank=True)
    is_subsidiary = models.BooleanField(default=False)
    number_of_employees = models.IntegerField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    operating_income = models.FloatField(null=True, blank=True)
    headquarters_location = models.CharField(max_length=100, null=True, blank=True)
    key_personnel = models.CharField(max_length=255, null=True, blank=True)
    formed_by = models.CharField(max_length=100, null=True, blank=True)
    country_code = models.CharField(max_length=10)
    facebook_link = models.URLField(max_length=255, null=True, blank=True)
    instagram_link = models.URLField(max_length=255, null=True, blank=True)
    linkedin_link = models.URLField(max_length=255, null=True, blank=True)
    youtube_link = models.URLField(max_length=255, null=True, blank=True)
    pinterest_link = models.URLField(max_length=255, null=True, blank=True)
    browser_link = models.URLField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, default='admin')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200, default='admin')
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.company_name} ({self.company_code})"


class BranchMaster(models.Model):
    branch_master_id = models.BigAutoField(primary_key=True)
    branch_code = models.CharField(max_length=8, unique=True)
    branch_name = models.CharField(max_length=255)
    branch_description = models.TextField()
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=100)
    branch_manager = models.CharField(max_length=100, null=True, blank=True)
    branch_type = models.CharField(max_length=50, null=True, blank=True)
    contact_number = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    opening_date = models.DateField(null=True, blank=True)
    closing_date = models.DateField(null=True, blank=True)
    branch_status = models.CharField(max_length=20)
    is_active = models.BooleanField(default=True)
    is_franchise = models.BooleanField(default=False)
    parent_branch_code = models.CharField(max_length=8)
    company_code = models.ForeignKey(
        'CompanyMaster',  # Reference the `CompanyMaster` model
        on_delete=models.CASCADE,
        related_name='branches'
    )
    total_employees = models.IntegerField()
    total_sales = models.DecimalField(max_digits=15, decimal_places=2)
    revenue = models.DecimalField(max_digits=15, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, default='admin')
    modified_at = models.DateTimeField(auto_now=True)
    modified_by = models.CharField(max_length=200, default='admin')
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.branch_name} ({self.branch_code})"

class ProjectMaster(models.Model):
    project_master_id = models.BigAutoField(primary_key=True)  
    project_code = models.CharField(max_length=8, unique=True)     
    project_name = models.CharField(max_length=200)                
    street_address = models.CharField(max_length=200, null=True, blank=True)                             
    city = models.CharField(max_length=200)                    
    state = models.CharField(max_length=200)                      
    postal_code = models.CharField(max_length=6)              
    project_manager = models.CharField(max_length=200, null=True, blank=True)                            
    company_code = models.ForeignKey(
        'CompanyMaster',  # Reference to the `CompanyMaster` model
        on_delete=models.CASCADE,
        related_name='projects'
    ) 
    branch_code = models.ForeignKey(
        'BranchMaster',  # Reference to the `BranchMaster` model
        on_delete=models.SET_NULL,
        related_name='projects',
        null=True,
        blank=True
    )                              
    project_start_date = models.DateField(null=True, blank=True)                               
    project_end_date = models.DateField(null=True, blank=True)                                
    project_budget = models.DecimalField(max_digits=12, decimal_places=2, null=True, blank=True)
    project_status = models.CharField(max_length=50, default='Planned')          
    client_name = models.CharField(max_length=200, null=True, blank=True)                               
    client_contact = models.CharField(max_length=15, null=True, blank=True)
    country_code = models.CharField(max_length=5, default='+91') 
    project_description = models.TextField(null=True, blank=True)                              
    project_priority = models.CharField(max_length=20, default='Medium')         
    project_category = models.CharField(max_length=100, null=True, blank=True)                         
    project_type = models.CharField(max_length=50, default='General')          
    estimated_completion_days = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.CharField(max_length=200, default='admin')
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    modified_by = models.CharField(max_length=200, default='admin')
    status = models.CharField(max_length=20, default='active')

    def __str__(self):
        return f"{self.project_name} ({self.project_code})"


class CustomerMaster(models.Model):
    customer_master_id = models.BigAutoField(primary_key=True)
    customer_code = models.CharField(max_length=8, unique=True)
    company_code = models.ForeignKey(
        'CompanyMaster',  # Reference the `BranchMaster` model
        on_delete=models.CASCADE,
        related_name='customers'
    )
    customer_name = models.CharField(max_length=200)
    contact_person = models.CharField(max_length=200, null=True, blank=True)
    customer_type = models.CharField(max_length=200)
    customer_industry = models.CharField(max_length=200)
    street_address = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    postal_code = models.CharField(max_length=6)
    country = models.CharField(max_length=200)
    country_code = models.CharField(max_length=5)
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    email = models.EmailField(max_length=255, unique=True, null=True, blank=True)
    fax_number = models.CharField(max_length=15, null=True, blank=True)
    website = models.URLField(max_length=255, null=True, blank=True)
    customer_details = models.CharField(max_length=200, null=True, blank=True)
    created_at = models.DateTimeField(default=now)
    created_by = models.CharField(max_length=200)
    modified_at = models.DateTimeField(auto_now=True, null=True, blank=True)
    modified_by = models.CharField(max_length=200)
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return f"{self.customer_name} ({self.customer_code})"


class DesignationMaster(models.Model):
    designation_id = models.BigAutoField(primary_key=True)
    designation_code = models.CharField(max_length=20, unique=True)
    designation_name = models.CharField(max_length=255)
    designation_grade = models.CharField(max_length=10, blank=True, null=True)
    designation_function = models.CharField(max_length=150, blank=True, null=True)
    salary_range_min = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    salary_range_max = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    designation_type = models.CharField(max_length=50, blank=True, null=True)
    job_level = models.CharField(max_length=50, blank=True, null=True)
    work_hours_per_week = models.IntegerField(blank=True, null=True)
    bonus_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    health_benefits = models.BooleanField(default=False)
    vacation_days = models.IntegerField(blank=True, null=True)
    contract_end_date = models.DateField(blank=True, null=True)
    reporting_manag_code = models.CharField(max_length=200, blank=True, null=True)
    is_remote = models.BooleanField(default=False)
    contract_renewal_option = models.BooleanField(default=False)
    equity_grant = models.BooleanField(default=False)
    performance_review_period = models.CharField(max_length=50, blank=True, null=True)
    job_posting_url = models.URLField(max_length=255, blank=True, null=True)
    career_path = models.TextField(blank=True, null=True)
    last_promotion_date = models.DateField(blank=True, null=True)
    created_by = models.CharField(max_length=200)
    modified_by = models.CharField(max_length=200)
    created_at = models.DateTimeField(default=now)
    modified_at = models.DateTimeField(default=now)
    status = models.CharField(max_length=50, default="Active")

    def __str__(self):
        return self.designation_name

from django.db import models
from django.utils.timezone import now

class Branch(models.Model):
    branch_code = models.CharField(max_length=10, unique=True)
    branch_name = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name


class Project(models.Model):
    project_code = models.CharField(max_length=10, unique=True)
    project_name = models.CharField(max_length=100)

    def __str__(self):
        return self.project_name


class Company(models.Model):
    company_code = models.CharField(max_length=10, unique=True)
    company_name = models.CharField(max_length=100)

    def __str__(self):
        return self.company_name


class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username


class EmployeeMaster(models.Model):
    employee_master_id = models.AutoField(primary_key=True)
    employee_code = models.CharField(max_length=10, unique=True)
    employee_name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=10)
    country = models.CharField(max_length=50)
    country_code = models.CharField(max_length=10)
    employee_phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    joining_date = models.DateField()
    designation = models.CharField(max_length=50)
    department = models.CharField(max_length=50)
    company = models.ForeignKey(CompanyMaster, on_delete=models.CASCADE)
    branch = models.ForeignKey(BranchMaster, on_delete=models.CASCADE)
    reporting_branch = models.ForeignKey(BranchMaster, on_delete=models.CASCADE, related_name="reporting_branch")
    project = models.ForeignKey(ProjectMaster, on_delete=models.SET_NULL, null=True, blank=True)
    grade = models.CharField(max_length=5, blank=True, null=True)
    username = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
    personal_email = models.EmailField(blank=True, null=True)
    office_email = models.EmailField(blank=True, null=True)
    pan_number = models.CharField(max_length=20, blank=True, null=True)
    aadhar_number = models.CharField(max_length=20, blank=True, null=True)
    reporting_manager_code = models.CharField(max_length=10, blank=True, null=True)
    reporting_manager_designation = models.CharField(max_length=50, blank=True, null=True)
    gross_salary = models.FloatField(blank=True, null=True)
    salary_start_date = models.DateField(blank=True, null=True)
    target_applicable = models.BooleanField(default=False)
    incentive_applicable = models.BooleanField(default=False)
    attendance_type = models.BooleanField(default=False)
    daily_work_master_applicable = models.BooleanField(default=False)
    employee_manager = models.CharField(max_length=50, blank=True, null=True)
    created_at = models.DateTimeField(default=now)
    created_by = models.CharField(max_length=50, default='admin')
    modified_at = models.DateTimeField(default=now)
    modified_by = models.CharField(max_length=50, default='admin')
    status = models.CharField(max_length=20, default='Active')

    def __str__(self):
        return self.employee_name
