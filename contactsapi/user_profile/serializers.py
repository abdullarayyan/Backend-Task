from rest_framework.serializers import ModelSerializer
from .models import UserProfile


class user_profileSerializer(ModelSerializer):

    class Meta:
        model = UserProfile

        fields = ['user_id', 'id', 'gender', 'maital_status', 'birth_date',
                  'created_at', 'updated_at'
                  ]