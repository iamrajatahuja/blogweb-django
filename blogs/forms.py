from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        # variable names should be same
        model = Comment
        # fields = "__all__"
        # fields = ["user_name","user_email","comment_text"]
        exclude = ["post"]
        labels = {"user_name":"Name","user_email":"Email","comment_text":"Comment"}
