from rest_framework import serializers
from ems_app.models import Employee, Department


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('id', 'name', 'code')

    def create(self, validated_data):
        
        is_department_exist = Department.objects.filter(code = validated_data["code"])
        if is_department_exist:
            department = is_department_exist.first()
        else:
            department = Department.objects.create(**validated_data)
        return department
        

class EmployeeSerializer(serializers.ModelSerializer):
    # manager = serializers.RelatedField(
    #     queryset = Employee.objects.all(),
    #     write_only = True,
    #     required = False,
        
    # )
    department = DepartmentSerializer(
        many=True,
        required=False, 
    )

    class Meta:
        model = Employee
        fields = [
            'id', 
            'name', 
            'department', 
            #   'manager', 
            'is_manager',
            ]
        
    def create(self, validated_data):
                
        department_data = validated_data.pop("department", None)

        if department_data:

            department_serializer = DepartmentSerializer(
                        data = department_data[0],
                    )

            if department_serializer.is_valid(raise_exception=True):
                        
                department = department_serializer.save()
            
            # manager_data = validated_data.pop("manager") if "manager" in validated_data else None

            emp = Employee.objects.create(dept=department,**validated_data)

        return emp


