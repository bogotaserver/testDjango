from django.contrib import admin
from .models import Post, Voetbalspelers


admin.site.register(Post)
admin.site.register(Voetbalspelers)


#Hier is nu het model Post zichtbaar en bewerkbaar gemaakt in de admin ruimte.