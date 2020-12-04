from rest_framework import serializers
from rest_framework import movie


class movieSerializer(serializers.ModelSerializer):
    class Meta:
        model = movie
        #        fields=('title','rating')
        fields = '__all__'
