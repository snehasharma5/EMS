from rest_framework import mixins, viewsets
from ems_app.models import Employee, Department
from ems_app.serializers import EmployeeSerializer, DepartmentSerializer
from rest_framework.response import Response


class EmployeeViewset(viewsets.ModelViewSet):

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        queryset = Employee.objects.all().values(
            "id",
            "name",
            "dept__name",
            "dept__code",
            "is_manager"
        )
        
        serializer = EmployeeSerializer(
            queryset,
            many=True,
        )
        
        return Response(serializer.data)

    def update( self, request, *args, **kwargs):

        partial = kwargs.pop("partial", True)

        instance = self.get_object()

        serializer = self.get_serializer(
            instance,
            data=request.data,
            partial=partial,
        )

        serializer.is_valid(
            raise_exception=True,
        )


        serializer.save()

        return Response(serializer.data)
    

    def destroy(self, request, *args, **kwargs):
       return super(EmployeeViewset, self).destroy(request, *args, **kwargs)
    
