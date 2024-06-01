from rest_framework import serializers

from .models import *

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name_surname', 'description', 'position', ]

class TeamDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TeamDestroySerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'