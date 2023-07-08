from .models import Family
from rest_framework import serializers

# Serializers define the API representation.
class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = ['id', 'title', 'slug', 'photo', 'royal']
