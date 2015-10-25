from datetime import datetime

from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Position
utcnow = datetime.now()


class OculusRiftView(APIView):
    def get(self, request):
        position = Position.objects.all()
        return Response({'position': position}, status=200)

    def post(self, request):
        try:
            Position.objects.create(
                w=request.data['w'],
                x=request.data['x'],
                y=request.data['x'],
                z=request.data['z'],
                time_received=utcnow
            )
        except Exception as e:
            return Response({'detail': e}, status=400)
        return Response()
