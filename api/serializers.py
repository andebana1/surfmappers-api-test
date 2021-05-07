from rest_framework import serializers
from . import models

class CasamentoSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(max_length=None, use_url=True, required=False, allow_null=True)
    class Meta:
        model = models.Casamento
        fields = '__all__'
        
    def create(self, validated_data):
        instance = models.Casamento(**validated_data)
        instance.save()
        return instance