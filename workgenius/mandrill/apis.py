from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers
from drf_spectacular.utils import extend_schema
from .services import store_message_payload


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

class WebhookApi(APIView):

    class InputSerializer(serializers.Serializer):
        mandrill_events = EventSerializer(many=True)


    @extend_schema(request=InputSerializer)
    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            store_message_payload(
                    events=serializer.validated_data.get("mandrill_events"),
            )
        except Exception as ex:
            return Response(
                    f"Database Error {ex}",
                    status=status.HTTP_400_BAD_REQUEST
                    )
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return Response(self.OutPutRegisterSerializer(user, context={"request":request}).data)
