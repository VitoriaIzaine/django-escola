from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Curso, Avaliacao
from .serializers import CursoSerializer, AvaliacaoSerializer



def index(request):
    return render(request, 'curso/index.html')




class CursoAPIView(APIView):
    """
    API Senai
    """\

    def get(self, request):
        curso = Curso.objects.all()
        serializer = CursoSerializer(curso, many=True)
        return Response(serializer.data)


class AvaliacaoAPIView(APIView):
    """
    API Senai
    """

    def get(self, request):
        av = Avaliacao.objects.all()
        serializer = AvaliacaoSerializer(av, many=True)
        return Response(serializer.data)


