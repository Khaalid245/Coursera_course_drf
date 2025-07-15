from rest_framework import serializers


from .models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model =User
        fields=['id','email','username','password', 'first_name', 'last_name']

        def create(self, validated_data):
            user = User.objects.create_user(
                email = validated_data['email'],
                username= validated_data['username'],
                password= validated_data['password'],
                first_name= validated_data.get['first_name',''],
                last_name= validated_data.get['last_name',''],
                )

            return user

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=['id','email','username','first_name','last_name']