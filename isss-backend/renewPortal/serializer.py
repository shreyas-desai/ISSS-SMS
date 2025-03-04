from rest_framework import serializers
from .models import Address, Student

class StudentDataSerializer(serializers.ModelSerializer):
	class Meta:
		model = Student
		fields ='__all__'
  
class AddressSerializer(serializers.ModelSerializer):
	class Meta:
		model = Address
		fields ='__all__'
