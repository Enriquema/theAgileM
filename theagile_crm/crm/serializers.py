from rest_framework import serializers
from .models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)
    updated_by = serializers.StringRelatedField(default=serializers.CurrentUserDefault(), read_only=True)

    class Meta:
        model = Customer
        fields = ['id', 'name', 'surname', 'photo', 'created_by', 'updated_by']
