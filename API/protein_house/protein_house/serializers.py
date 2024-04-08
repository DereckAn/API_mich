from protein_house.models import (Addresstype, Pagedata, Phonetype, User, Useraddress,
                          Userinfo, Userphone)
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class UserphoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userphone
        fields = '__all__'
        
class PhonetypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetype
        depth = 1
        fields = '__all__'

class UseraddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Useraddress
        fields = '__all__'

class AddresstypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Addresstype
        fields = '__all__'

class UserinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Userinfo
        fields = '__all__'
        
class PagedataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pagedata
        fields = '__all__'



class PhoneSerializerGet(serializers.ModelSerializer):
    phone_type = PhoneTypeSerializer(read_only=True)
    class Meta:
        model=Userphone
        fields = '__all__'

class PhoneSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=Userphone
        fields = '__all__'
        
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, clean_data):
        user_obj = User.objects.create(email=clean_data['email'],
                                       password=clean_data['password'])

# Path: API/protein_house/protein_house/views.py