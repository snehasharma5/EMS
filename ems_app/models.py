from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50)
    dept = models.ForeignKey(Department,related_name="department", on_delete=models.CASCADE)
    # manager = models.ForeignKey('self', on_delete=models.CASCADE)
    is_manager = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    
