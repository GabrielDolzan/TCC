from django.contrib import admin
from .models import Game, Artifact, Data

# Register your models here.
admin.site.register(Game)
admin.site.register(Artifact)
admin.site.register(Data)