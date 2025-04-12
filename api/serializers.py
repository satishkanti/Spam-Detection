from rest_framework import serializers
from .models import User, Contact


# Serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'phone_number', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}  # Password should not be included in responses

    def create(self, validated_data):
        # Create a new user instance using the provided validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            phone_number=validated_data['phone_number'],
            email=validated_data.get('email', ''),  # Email is optional
            password=validated_data['password']  # Password is hashed automatically by create_user method
        )
        return user

# Serializer for the Contact model
class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['id', 'name', 'phone_number', 'is_spam']
        extra_kwargs = {'user': {'read_only': True}}

    def create(self, validated_data):
        # Ensure user field is set when creating a contact
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)