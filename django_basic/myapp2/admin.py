from django.contrib import admin
from .models import StaffInformation
from .models import StaffInformation, Staff,Department,Book

admin.site.register(StaffInformation)
admin.site.register(Staff)
admin.site.register(Department)
admin.site.register(Book)