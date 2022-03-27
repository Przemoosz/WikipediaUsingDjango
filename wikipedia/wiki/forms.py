from django import forms
from .models import Comments,forum_post


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', ]


# class PostSearchForm1(forms.ModelForm):
#     class Meta:
#         #model = forum_post
#         fields = ['title',
#                   'semestr',
#                   'category',
#                   'text']
class PostSearchForm(forms.Form):
    #search_word_title = forms.CharField(label='Title',required=False)
    search_word_text = forms.CharField(label='Text',required=False)
