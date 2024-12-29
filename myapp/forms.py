from django import forms
from .models import CompanyMaster, BranchMaster, CustomerMaster,DesignationMaster,EmployeeMaster,ProjectMaster,UserRegistration

class CompanyMasterForm(forms.ModelForm):
    class Meta:
        model = CompanyMaster
        fields = '__all__'


class BranchMasterForm(forms.ModelForm):
    class Meta:
        model = BranchMaster
        fields = '__all__'


class CustomerMasterForm(forms.ModelForm):
    class Meta:
        model = CustomerMaster
        fields = '__all__'


class DesignationMasterForm(forms.ModelForm):
    class Meta:
        model = DesignationMaster
        fields = '__all__'

class EmployeeMasterForm(forms.ModelForm):
    class Meta:
        model = EmployeeMaster
        fields = '__all__'



class ProjectMasterForm(forms.ModelForm):
    class Meta:
        model = ProjectMaster
        fields = '__all__'



class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = UserRegistration
        fields = '__all__'
