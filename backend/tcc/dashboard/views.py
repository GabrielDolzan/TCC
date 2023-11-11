from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from .models import Game, Artifact, Data
from .serializers import GameSerializer, ArtifactSerializer, DataSerializer
from django.http import HttpResponseNotFound, JsonResponse, HttpResponse, HttpRequest
import json
from . import functions
from rest_framework.permissions import IsAuthenticated

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
      data = list(Game.objects.values()) 

      return JsonResponse(data, safe=False)

class ArtifactViewSet(viewsets.ModelViewSet):
    queryset = Artifact.objects.all()
    serializer_class = ArtifactSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
      data = list(Artifact.objects.values()) 

      return JsonResponse(data, safe=False)

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    #permission_classes = (IsAuthenticated,)

    def list(self, request):
      data = list(Data.objects.values()) 

      return JsonResponse(data, safe=False)
    
    def create(self, request):
        data = request.data

        artifact = data.get('artifact')

        if not Artifact.objects.filter(id=artifact).first():
           return HttpResponseNotFound('Artefato não encontrado')

        return super().create(request)

def getIdentifierGame(request, jogo):
    #if request.user and request.user.is_authenticated:
        data = list(Data.objects.filter(game=jogo, id__isnull=False).values('id').distinct())

        return JsonResponse(data, safe=False)
    #else:
    #    return JsonResponse({"detail":"As credenciais de autenticação não foram fornecidas."}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def getArtifactGame(request, jogo):
    #if request.user and request.user.is_authenticated:
        data = list(Artifact.objects.filter(game=jogo).values()) 

        return JsonResponse(data, safe=False)
    #else:
    #    return JsonResponse({"detail":"As credenciais de autenticação não foram fornecidas."}, status=status.HTTP_403_FORBIDDEN)

@api_view(['GET'])
def getDataGame(request, jogo):
    #if request.user and request.user.is_authenticated:
        data = list(Data.objects.filter(game=jogo).values()) 

        return JsonResponse(data, safe=False)
    #else:
    #    return JsonResponse({"detail":"As credenciais de autenticação não foram fornecidas."}, status=status.HTTP_403_FORBIDDEN)


def gerarDashboard(request: HttpRequest):
    """
    Retorna as informações do dashboard
    """
    
    res = request.body
    json_str = res.decode('utf-8')
    json_dict = json.loads(json_str)

    game = json_dict["game"]
    id = json_dict["id"]
    artefato = json_dict["artefato"]
    funcao = json_dict["funcao"]
    tipo = json_dict['tipo']
    inicio = json_dict['inicio']
    final = json_dict['final']

    resposta = functions.get_data(funcao, tipo, game, artefato, id, inicio, final)
    
    return JsonResponse(resposta)

def getFunctions(request: HttpRequest):
    """
    Retorna as funções disponíveis
    """

    return JsonResponse(functions.get_functions(), safe=False)