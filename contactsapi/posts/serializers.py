from rest_framework import serializers
from .models import Posts


class TutorialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ('user_id',
                  'content',
                  'created_at',
                  'updated_at')