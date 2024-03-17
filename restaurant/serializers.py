from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Menu, Booking

class MenuSerializer (serializers.ModelSerializer):
    # user = serializers.PrimaryKeyRelatedField(
    #         queryset=User.objects.all(),
    #         default=serializers.CurrentUserDefault()
    # )

    class Meta:
        model = Menu
        fields = "__all__"

        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Rating.objects.all(),
        #         fields=['user', 'menuitem_id']
        #     )
        # ]

        # extra_kwargs = {
        #     'rating': {'min_value': 0, 'max_value':5},
        # }

class BookingSerializer (serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer): 

    class Meta: 
        model = User 
        fields = ['url', 'username', 'email', 'groups']