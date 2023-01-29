from django.urls import path

from measurement.views import SensorsView, SensorViewUpdate, MeasurementCreate

urlpatterns = [
    # TODO: зарегистрируйте необходимые маршруты
    path('sensors/', SensorsView.as_view()),
    path('sensors/<pk>/', SensorViewUpdate.as_view()),
    path('measurements/<pk>/', MeasurementCreate.as_view()),

]
