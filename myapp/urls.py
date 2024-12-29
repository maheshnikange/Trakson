from django.urls import path
from . import views

urlpatterns = [
    # CompanyMaster URLs
    path("companies/", views.company_list, name="company_list"),
    path("companies/create/", views.company_create, name="company_create"),
    path("companies/<int:pk>/", views.company_detail, name="company_detail"),

    # BranchMaster URLs
    path("branches/", views.branch_list, name="branch_list"),
    path("branches/create/", views.branch_create, name="branch_create"),
    path("branches/<int:pk>/", views.branch_detail, name="branch_detail"),


    path('designations/', views.designation_list, name='designation_list'),
    path('designations/create/', views.designation_create, name='designation_create'),
    path('designations/update/<int:designation_id>/', views.designation_update, name='designation_update'),
    path('designations/delete/<int:designation_id>/', views.designation_delete, name='designation_delete'),


    path('employees/', views.employee_list, name='employee_list'),
    path('employees/create/', views.employee_create, name='employee_create'),

    # Update, retrieve, and delete Employee by employee_code
    path('employees/<str:employee_code>/', views.employee_detail, name='employee_detail'),
    path('employees/update/<str:employee_code>/', views.employee_update, name='employee_update'),
    path('employees/delete/<str:employee_code>/', views.employee_delete, name='employee_delete'),



    # CustomerMaster URLs
    path("customers/", views.customer_list, name="customer_list"),
    path("customers/create/", views.customer_create, name="customer_create"),
    path("customers/<int:pk>/", views.customer_detail, name="customer_detail"),

    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.project_create, name='project_create'),
    path('projects/<int:project_id>/', views.project_detail, name='project_detail'),
    path('projects/<int:project_id>/update/', views.project_update, name='project_update'),
    path('projects/<int:project_id>/delete/', views.project_delete, name='project_delete'),

]
