from django.contrib import admin
from classico_app.models import UserProfile
from classico_board.models import Board, File, Comment

# Register your models here.
admin.site.register(Board)
admin.site.register(File)
admin.site.register(Comment)

admin.site.register(UserProfile)


