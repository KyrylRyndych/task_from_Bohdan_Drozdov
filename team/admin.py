from django.contrib import admin
from .models import Team, Employee


class EmployeeInline(admin.TabularInline):
    model = Employee


class TeamAdmin(admin.ModelAdmin):
    list_display = ("name",)
    inlines = [EmployeeInline]


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("firstname", "lastname", "email", "team")
    list_editable = ("team",)


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Team, TeamAdmin)
