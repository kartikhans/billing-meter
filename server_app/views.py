from .tasks import BillMetering
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import MeteringApiSerializer


class Metering(APIView):
    def post(self, request):
        data = request.data
        serializer = MeteringApiSerializer(data=data)
        if serializer.is_valid():
            vd = serializer.validated_data
            BillMetering().apply_async(kwargs=vd)
            return Response("Done", status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
