from rest_framework import serializers
from tasks.models import Maintenance
from django.utils import timezone

class MaintenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Maintenance
        fields = '__all__'
        extra_kwargs = {
            'vehicle_reg_no': {'required': True, 'error_messages': {'blank': 'Vehicle registration number is required.'}},
            'maintenance_type': {'required': True, 'error_messages': {'blank': 'Maintenance type cannot be empty.'}},
            'description': {'required': True, 'error_messages': {'blank': 'Description cannot be empty.'}},
            'next_due_date': {'required': True, 'error_messages': {'null': 'Next due date is required.'}},
            'status': {'required': True, 'error_messages': {'invalid_choice': 'Invalid status choice.'}},
        }

    
    """Ensure next_due_date is in the future"""
    def validate_next_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Next due date must be in the future.")
        return value

    """Ensure status is a valid choice"""
    def validate_status(self, value):
        valid_statuses = [choice[0] for choice in Maintenance.STATUS_CHOICES]
        if value not in valid_statuses:
            raise serializers.ValidationError(f"Invalid status. Choose from {valid_statuses}.")
        return value

    """Ensure maintenance_date is not after next_due_date"""
    def validate(self, data):
        maintenance_date = data.get("maintenance_date", timezone.now())
        next_due_date = data.get("next_due_date")

        if next_due_date and maintenance_date > next_due_date:
            raise serializers.ValidationError(
                {"next_due_date": "Next due date cannot be earlier than the maintenance date."}
            )

        return data
