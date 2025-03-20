from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='نام')
    last_name = models.CharField(max_length=50,verbose_name='نام خانوادگی')
    student_code = models.CharField(max_length=20, unique=True,verbose_name='شماره دانشجویی')
    email = models.EmailField(max_length=100, unique=True,verbose_name='ایمیل')
    phone_number = models.CharField(max_length=15,verbose_name='َشماره تماس')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    class Meta:
        verbose_name = 'دانشجو'
        verbose_name_plural = 'دانشجویان'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

class Course(models.Model):
    course_name = models.CharField(max_length=100,verbose_name='نام دوره')
    course_code = models.CharField(max_length=20, unique=True,verbose_name='کد دوره')
    instructor = models.CharField(max_length=100,verbose_name='مدرس')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    class Meta:
        verbose_name = 'دوره'
        verbose_name_plural = 'دوره ها'

    def __str__(self):
        return self.course_name
    

class Attendance(models.Model):
    STATUS_CHOICES = [
        ('present', 'حاضر'),
        ('absent', 'غایب'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='attendances',verbose_name='دانشجو')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='attendances',verbose_name='دوره')
    date = models.DateField(verbose_name='تاریخ و زمان')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='present',verbose_name='وضعیت')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='ایجاد شده')

    class Meta:
        verbose_name='حضور و غیاب'
        verbose_name_plural = 'حضور و غیاب ها'

    def __str__(self):
        return f"{self.student} - {self.course} - {self.date}"