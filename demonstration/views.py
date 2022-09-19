from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from demonstration.models import Persona, Historial, ResultadosHistorial
from difflib import SequenceMatcher
from django.db import connection
import uuid as uuid
from django.db import transaction
from demonstration.serializers import HistorialSerializer, DetalleHistorialSerializer

# Create your views here.


class BuscarPersonaView(APIView):

    permission_classes = (IsAuthenticated, )

    def get(self, request):
        nombre = self.request.query_params.get('nombre', '')
        porcentaje = self.request.query_params.get('porcentaje', 0)

        if porcentaje == '':
            porcentaje = 0

        with connection.cursor() as cursor:
            cursor.execute("select * from demonstration_persona "
                            "where (MATCH(nombre) against(%s IN NATURAL LANGUAGE MODE))", [nombre.lower()])

            personas = self.__dictfetchall(cursor)

        result = []

        with transaction.atomic():

            ratio = 0
            historial = Historial.objects.create(user=self.request.user, porcentaje=porcentaje)

            for persona in personas:
                ratio = SequenceMatcher(None, persona["nombre"], nombre).ratio()
                persona.pop("id")
                persona["ratio"] = ratio
                if porcentaje != 0 and ratio < float(porcentaje):
                    personas.remove(persona)
                else:
                    result.append(persona)
                    ResultadosHistorial.objects.create(historial=historial, **persona)

        return Response(result)


    def __dictfetchall(self, cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]


class HistorialViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin,):

    permission_classes = (IsAuthenticated,)
    serializer_class = HistorialSerializer
    queryset = Historial.objects.all().order_by('-created')

    def get_serializer_class(self):
        if self.action and self.action == "retrieve":
            return DetalleHistorialSerializer
        else:
            return HistorialSerializer
