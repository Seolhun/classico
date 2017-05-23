from django.contrib import admin
from classico_app.models import UserProfile
from classico_board.models import WebPage,Topic,AccessRecord,Board

# Register your models here.
admin.site.register(AccessRecord)
admin.site.register(WebPage)
admin.site.register(Topic)
admin.site.register(Board)

admin.site.register(UserProfile)


