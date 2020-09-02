from django import forms
from .models import Write
from ckeditor_uploader.widgets import CKEditorUploadingWidget

widgets = {
    'title': forms.TextInput(
        attrs={'class': 'form=control', 'style': 'width: 100%', 'placeholder': '제목을 입력하세요.'}
    ),
    'author': forms.Select(
        attrs={'class': 'custom-select'}
    ),
    'body': forms.CharField(
        widget=CKEditorUploadingWidget()
    ),
}

class CreateWrite(forms.ModelForm):
    class Meta:
        model = Write

        fields = ['title', 'author', 'body']
