from django import forms 
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    
    class Meta():
        model = Post 
        fields = ('author','title','text')
        widget = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }

class CommentForm(forms.ModelForm):
    widget = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }
    
    class Meta:
        model = Comment
        fields = ("author","text")
        

