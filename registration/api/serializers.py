from rest_framework import serializers
from registration.models  import player, society, User


class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ['username',
				  'password',
				  ]


class PlayerRegistrationSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)

	class Meta:
		model = player
		fields = ['user',
				  'name',  
				  'email',
				  'admissionNo', 
				  'contact', 
				  'college', 
				  ]


	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user_obj = User.objects.create_user(**user_data)
		Player = player.objects.create(user=user_obj, **validated_data)
		Player.save()
		return player



class SocietyRegistrationSerializer(serializers.ModelSerializer):
	user = UserSerializer(required=True)

	class Meta:
		model = society
		fields = ['name',
				  'email', 
				  'user',
				  'description',
				  ]


	def create(self, validated_data):
		user_data = validated_data.pop('user')
		user_obj = User.objects.create_user(**user_data)
		Society = society.objects.create(user=user_obj, **validated_data)
		Society.save()
		return Society



class UserLoginSerializer(serializers.ModelSerializer):
	table = serializers.IntegerField()
	username = serializers.CharField()
	password = serializers.CharField(max_length=20)

	class Meta:
		model = User
		fields = ['table',
				  'username',
				  'password',
			]
				  
		extra_kwargs = {
				'password': {'write_only':True}
		}


