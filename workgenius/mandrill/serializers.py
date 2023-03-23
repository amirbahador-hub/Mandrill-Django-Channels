from rest_framework import serializers


class MessageSerializer(serializers.Serializer):
        ts = serializers.IntegerField()
        email = serializers.EmailField()
        sender = serializers.EmailField()
        subject = serializers.CharField()
        state = serializers.CharField()
        _id = serializers.CharField()
        _version = serializers.CharField()

class EventSerializer(serializers.Serializer):
        msg = MessageSerializer()
        event = serializers.CharField()
        _id = serializers.CharField()

