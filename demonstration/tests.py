from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse
from demonstration.models import Persona
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken


def bearer_token():
    # assuming there is a user in User model
    user = User.objects.get(username="dairo")
    refresh = RefreshToken.for_user(user)
    return {"HTTP_AUTHORIZATION": f'Bearer {refresh.access_token}'}


class BuscarPersonaTestCase(TestCase):
    def setUp(self):
        Persona.objects.create(**{
            "departamento": "PUTUMAYO",
            "localidad": "NO APLICA",
            "municipio": "PUERTO_CAICEDO",
            "nombre": "Neider Albeiro Barcenas Portillo",
            "edad_activo": 11,
            "tipo_persona": "PREFERENTE",
            "tipo_cargo": "ACTOR"
        })
        Persona.objects.create(**{
            "departamento": "CALDAS",
            "localidad": "NO APLICA",
            "municipio": "MANIZALES",
            "nombre": "Jimmy Adrian Galvis Gonzalez",
            "edad_activo": 8,
            "tipo_persona": "PREFERENTE",
            "tipo_cargo": "POLITICO",
        })

        User.objects.create(username="dairo", password="123456")

    def test_buscar_exitoso(self):
        url = reverse("personas")
        response = self.client.get(
            url+"?nombre=asd&porcentaje=0",
            format="json",
            **bearer_token()
        )

        self.assertEqual(len(response.data), 0)
        self.assertEqual(response.status_code, 200)

    def test_buscar_credenciales_no_validas(self):
        url = reverse("personas")
        response = self.client.get(
            url,
            format="json",
        )

        self.assertEqual(response.status_code, 401)


class HistorialTestCase(TestCase):
    def setUp(self):
        Persona.objects.create(**{
            "departamento": "BOYACA",
            "localidad": "NO APLICA",
            "municipio": "SAMACA",
            "nombre": "Myriam Rocio Sierra Sierra",
            "edad_activo": 1,
            "tipo_persona": "PREFERENTE",
            "tipo_cargo": "CANTANTE"
        })

        User.objects.create(username="dairo", password="123456")

        url = reverse("personas")
        response = self.client.get(
            url + "?nombre=sierra&porcentaje=",
            format="json",
            **bearer_token()
        )

    def test_historial_list_detail(self):
        url = reverse("historial-list")
        response = self.client.get(
            url,
            format="json",
            **bearer_token()
        )

        self.assertEqual(response.data[0]['username'], "dairo")
        self.assertEqual(response.status_code, 200)

        url = reverse("historial-detail", kwargs={'pk': response.data[0]['id']})
        response = self.client.get(
            url,
            format="json",
            **bearer_token()
        )

        self.assertEqual(response.data['porcentaje'], 0.0)
        self.assertEqual(response.status_code, 200)



