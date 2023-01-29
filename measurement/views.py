# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Sensor, Measurement
from .serializers import SensorSerializer, MeasurementSerializer, SensorDetailSerializer


class SensorsView(generics. ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SensorViewUpdate(generics.RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorDetailSerializer


class MeasurementCreate(generics.CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementSerializer


# @api_view(['GET', 'POST'])
# def sensors(request):
#     if request.method == "GET":
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#     if request.method == "POST":
#         return Response({'status': 'ok'})


# class SensorsView(APIView):
#     def get(self, request):
#         sensors = Sensor.objects.all()
#         ser = SensorSerializer(sensors, many=True)
#         return Response(ser.data)
#
#     def post(self, request):
#         return Response({'status': 'ok'})


# class SensorDetailSerializer(serializers.ModelSerializer):
#     measurements = MeasurementSerializer(read_only=True, many=True)
#
#     class Meta:
#         model = Sensor
#         fields = ['id', 'name', 'description', 'measurements']
#
# class SensorSerializer(serializers.Serializer):
#     # measurements = MeasurementSerializer(read_only=True, many=True)
#     name = serializers.CharField(max_length=50, )
#     description = serializers.CharField(max_length=50, )