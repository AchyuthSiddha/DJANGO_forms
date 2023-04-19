from django import forms

g=[['male','MALE'],('female','FEMALE')]
c=[('python','PYTHON'),['java','JAVA'],('html','HTML')]
class StudentForm(forms.Form):
    name=forms.CharField(max_length=100)
    age=forms.IntegerField()
    email=forms.EmailField()
    password=forms.CharField(max_length=100,widget=forms.PasswordInput)
    #gender=forms.ChoiceField(choices=g)
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    address=forms.CharField(max_length=100,widget=forms.Textarea(attrs={'cols':5,'rows':5}))
    # course=forms.MultipleChoiceField(choices=c)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)

