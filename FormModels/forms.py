from django import forms
from django.core import validators
from FormModels.models import User


class Newuser(forms.ModelForm):
    class Meta():
        model = User
        fields = '__all__'


# def check_for_z(value):
#      if value[0].lower()!='z':
#           raise forms.ValidationError('Name needs to start with z')



# class Formname(forms.Form):
#      name=forms.CharField()
#      email=forms.EmailField()
#      verifyemail=forms.EmailField(label='Enter your email again')
#      text=forms.CharField(widget=forms.Textarea)
#      botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])


#      def clean(self):
#          all_clean_data=super().clean()
#          email=all_clean_data['email']
#          vmail=all_clean_data['verifyemail']


#          if email!=vmail:
#              raise forms.ValidationError('Make sure your email is correct')




