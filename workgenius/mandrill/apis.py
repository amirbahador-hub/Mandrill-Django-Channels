from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, serializers
from .serializers import EventSerializer 
from drf_spectacular.utils import extend_schema
from .services import store_message_payload
from .selectors import get_events


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


class EventList(APIView):
    class OutPutSerializer(serializers.Serializer):
        # TODO: Show event msg 
        events = serializers.SerializerMethodField("get_events")

        def get_events(self, obj):
            return obj

    @extend_schema(responses=OutPutSerializer)
    def get(self, request):
        events = get_events()

        return Response(self.OutPutSerializer(events, context={"request":request}).data)

        
