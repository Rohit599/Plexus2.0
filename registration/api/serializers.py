from rest_framework import serializers
from registration.models  import player, society

class PlayerRegistrationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(style={'input_style':'password'}, write_only=True)

	class Meta:
		model = player
		fields = ['name', 
				  'email', 
				  'admissionNo', 
				  'contact', 
				  'college', 
				  'password', 
				  'password2']

		extra_kwargs = {
				'password': {'write_only':True}
		}

	def save(self):
		Player = player(
					name=self.validated_data['name'],
					email=self.validated_data['email'],
					admissionNo=self.validated_data['admissionNo'],
					contact=self.validated_data['contact'],
					password=self.validated_data['password'],
					college=self.validated_data['college'],
				)
		password=self.validated_data['password']
		password2=self.validated_data['password2']

		if password != password2:
			raise serializers.ValidationError({'password':'Passwords must match'})
		Player.save()
		return Player



class SocietyRegistrationSerializer(serializers.ModelSerializer):
	password2 = serializers.CharField(style={'input_style':'password'}, write_only=True)

	class Meta:
		model = society
		fields = ['username', 
				  'name', 
				  'email', 
				  'description', 
				  'password', 
				  'password2']
				  
		extra_kwargs = {
				'password': {'write_only':True}
		}

	def save(self):
		Society = society(
					username=self.validated_data['username'],
					name=self.validated_data['name'],
					email=self.validated_data['email'],
					description=self.validated_data['description'],
					password=self.validated_data['password'],
				)
		password=self.validated_data['password']
		password2=self.validated_data['password2']

		if password != password2:
			raise serializers.ValidationError({'password':'Passwords must match'})
		Society.save()
		return Society