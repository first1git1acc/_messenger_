from django import forms

class Login(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"plasceholder":"Username"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"Username"}))

class Registration(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget = forms.EmailInput(attrs={"placeholder":"email"}))
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"Password"}))

class add_new_post(forms.Form):
    title = forms.CharField(max_length = 100)
    body = forms.CharField(max_length = 256)
    slug = forms.SlugField(max_length = 250)

class find_form(forms.Form):
    day = forms.IntegerField(required=True)
    year = forms.IntegerField(required=True)
    month = forms.IntegerField(required=True)
    slug = forms.SlugField(max_length = 250,required=True)

'''class Email(forms.Form):

    email_from = forms.EmailField()
    email_to = forms.EmailField()
    text = forms.CharField(max_length = 256)'''
    