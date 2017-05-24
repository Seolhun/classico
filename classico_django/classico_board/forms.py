from django import forms
from classico_board.models import Board, Comment, File


class BoardForm(forms.ModelForm):
    class Meta():
        model = Board
        fields = ('title', 'text')

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'text' : forms.Textarea(attrs={'class':'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ('text',)

        widgets = {
            'text' : forms.Textarea(attrs={'class':'form-control'}),
        }