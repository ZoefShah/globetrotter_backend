from place.models import Place, UserExperience, Image

from rest_framework import serializers

class PlaceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Place
		fields = '__all__'

	def create(self, validated_data):
		return Place.objects.create(**validated_data)

	def update(self, instance, validated_data):
		instance.name = validated_data.get('name', instance.name)
		instance.address = validated_data.get('address', instance.address)
		instance.likes = validated_data.get('likes', instance.likes)
		instance.views = validated_data.get('views', instance.views)
		instance.save()
		return instance

class UserExperienceSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserExperience
		fields = '__all__'
		depth = 1	


