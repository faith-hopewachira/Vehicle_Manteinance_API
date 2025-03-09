from django.shortcuts import render
from tasks.models import Maintenance
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import MaintenanceSerializer



class MaintenanceListView(APIView):
    """
    Handles retrieving all maintenance tasks and creating a new task.
    - GET: Retrieves all tasks, with optional filtering by vehicle registration.
    - POST: Creates a new maintenance task if valid data is provided.
    """

    def get(self, request):
        vehicle_reg_no = request.query_params.get("vehicle_reg_no")
    
        if vehicle_reg_no:
            tasks = Maintenance.objects.filter(vehicle_reg_no=vehicle_reg_no)
            if not tasks.exists():
                return Response(
                    {"detail": f"No maintenance records found for vehicle registration number {vehicle_reg_no}."},
                    status=status.HTTP_404_NOT_FOUND
                )
        else:
            tasks = Maintenance.objects.all()
    
        serializer = MaintenanceSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
    
    def post(self, request):
        serializer = MaintenanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MaintenanceDetailView(APIView):
    """
    Handles retrieving, updating, and deleting a specific maintenance task by ID.
    - GET: Retrieves details of a specific maintenance task.
    - PATCH: Updates a maintenance task.
    - DELETE: Removes a maintenance task.
    """
    def get(self, request, id):
        try:
            task = Maintenance.objects.get(pk=id)
        except Maintenance.DoesNotExist:
            return Response({"detail": f"Maintenance task with ID {id} does not exist in our records. Please ensure the ID is correct and try again."
        }, status=status.HTTP_404_NOT_FOUND)
        serializer = MaintenanceSerializer(task)
        return Response(serializer.data, status=status.HTTP_200_OK)

    
  
    def patch(self, request, id):
        try:
            task = Maintenance.objects.get(pk=id)
        except Maintenance.DoesNotExist:
            return Response(
                {"detail": f"Maintenance task with ID {id} does not exist in our records. Please ensure the ID is correct and try again."},
            status=status.HTTP_404_NOT_FOUND,
        )

        serializer = MaintenanceSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    
    def delete(self, request, id):
        try:
            task = Maintenance.objects.get(pk=id)
        except Maintenance.DoesNotExist:
            return Response(
                {"detail": f"Maintenance task with ID {id} does not exist in our records. Please ensure the ID is correct and try again."},
            status=status.HTTP_404_NOT_FOUND,
        )

        task.delete()
        return Response(
            {"detail": f"Maintenance task with ID {id} has been successfully deleted."},
            status=status.HTTP_204_NO_CONTENT,
        )