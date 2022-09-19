from rest_framework import serializers
from demonstration.models import Historial, ResultadosHistorial


class ResultadoHistorialSerializer(serializers.ModelSerializer):

    class Meta:
        model = ResultadosHistorial
        fields = '__all__'


class HistorialSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        source="user.username", read_only=True
    )

    class Meta:
        model = Historial
        fields = '__all__'


class DetalleHistorialSerializer(serializers.ModelSerializer):

    resultados_historial = ResultadoHistorialSerializer(many=True, read_only=True)

    class Meta:
        model = Historial
        fields = '__all__'

