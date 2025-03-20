from django.contrib import admin
from .models import Student, Course, Attendance


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name','student_code')
    search_fields = ('first_name','last_name','student_code','email','phone_number')
    list_display_links = ('first_name','last_name','student_code')
    list_per_page = 10

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name','course_code','instructor')
    search_fields = ('course_name','course_code','instructor')
    list_per_page = 10

@admin.register(Attendance)
class Attendance(admin.ModelAdmin):
    list_display = ('student','course','status')
    search_fields = ('student','course')
    raw_id_fields = ('student','course')
    list_editable = ('status',)
    list_per_page = 10