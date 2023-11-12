from django.urls import path
from . import views

game = views.GameViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

artifact = views.ArtifactViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

data = views.DataViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

game_pk = views.GameViewSet.as_view({
    'delete': 'destroy'
})

artifact_pk = views.ArtifactViewSet.as_view({
    'put': 'update',
    #'delete': 'destroy'
})

dashboard = views.DashboardViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

urlpatterns = [
    path('api/game/', game, name='games'),
    #path('api/game/<int:pk>', game_pk, name='gamedelete'),

    path('api/artifact/', artifact, name='artifacts'),
    path('api/artifact/<int:pk>', artifact_pk, name='artifacts'),
    path('api/artifact/game/<int:jogo>', views.getArtifactGame, name='artifactsgame'),

    path('api/data/', data, name='data'),
    path('api/data/<int:jogo>', views.getDataGame, name='data'),

    path('api/identifier/<int:jogo>', views.getIdentifierGame, name='idgame'),
    
    path('gerar-dashboard/', views.gerarDashboard, name="gerardashboard"),
    path('gerar-dashboard-saved/', views.gerarDashboardSaved, name="gerardashboardsaved"),

    path('api/functions/', views.getFunctions, name='functions'),

    path('api/dashboard/', dashboard, name='dashboard'),
    path('api/dashboard/<int:jogo>', views.getDashboardGame, name='dashboardgame')
]