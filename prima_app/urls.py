from django.urls import path
from prima_app.views import index,homepage,welcome,lista,chisiamo,variabili



app_name="prima_app"
urlpatterns = [
    path('index', index, name="index"),
    path('homepage', homepage, name="homepage"),
    path('welcome', welcome, name="welcome"),
    path('lista', lista, name="lista"),
    path('chisiamo', chisiamo, name="chisiamo"),
    path('variabili', variabili, name="variabili"),
]