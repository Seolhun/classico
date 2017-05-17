from django.contrib import admin
from classico_app.models import WebPage,Topic,AccessRecord,Board

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(Board)

