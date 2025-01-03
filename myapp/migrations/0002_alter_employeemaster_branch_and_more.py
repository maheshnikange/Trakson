# Generated by Django 5.1.4 on 2024-12-29 15:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeemaster',
            name='branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.branchmaster'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.companymaster'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='project',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='myapp.projectmaster'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='reporting_branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting_branch', to='myapp.branchmaster'),
        ),
        migrations.AlterField(
            model_name='employeemaster',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.userregistration'),
        ),
    ]
