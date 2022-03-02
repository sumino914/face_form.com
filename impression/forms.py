from socket import fromshare
from django import forms
from .models import Impression,Evaluation

eval_choice =[
    (1,'1'),
    (2,'2'),
    (3,'3'),
    (4,'4'),
    (5,'5')
]

class ImpressionBasicForm(forms.ModelForm):
    class Meta:
        model = Impression
        fields = ['name','age','gender']

class ImpressionCreateForm1(forms.ModelForm):

    pattern1 = forms.ChoiceField(
        label="[1]笑顔の度合いの変化",
        choices=eval_choice,
        widget=forms.RadioSelect,
    )
    class Meta:
        model = Impression
        fields = ['pattern1']

class ImpressionCreateForm2(forms.ModelForm):

    pattern2 = forms.ChoiceField(
        label="[2]視線の方向の変化",
        choices=eval_choice,
        widget=forms.RadioSelect,
    )
    class Meta:
        model = Impression
        fields = ['pattern2']

class ImpressionCreateForm3(forms.ModelForm):
    pattern3 = forms.ChoiceField(
        label="[3]",
        choices=eval_choice,
        widget=forms.RadioSelect,
    )
    class Meta:
        model = Impression
        fields = ['pattern3']

class ImpressionCreateForm4(forms.ModelForm):

    pattern4 = forms.ChoiceField(
        label="[4]",
        choices=eval_choice,
        widget=forms.RadioSelect,
    )
    class Meta:
        model = Impression
        fields = ['pattern4']

