from rest_framework import serializers
from api.models import Post

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified','date_published','date_updated','url_image']

class PostLogSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post  
        exclude = ['is_removed', 'created', 'modified','date_updated']