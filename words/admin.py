from django.contrib import admin
from . import models


@admin.register(models.Word)
class WordAdmin(admin.ModelAdmin):

    """ Word Admin Definition """

    pass
