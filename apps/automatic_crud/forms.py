from django import forms
from django.contrib.auth.forms import AuthenticationForm


class PanelLoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super(PanelLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Usuario'
        self.fields['password'].widget.attrs['class'] = 'form-control'
        self.fields['password'].widget.attrs['placeholder'] = 'Contraseña'


class GeneralForms(forms.ModelForm):

    def custom_styles(self, fields):
        for field in fields:
            # if ('Select' in str(type(fields[field].widget))):
            #     fields[field].widget.attrs.update(
            #         {'class': 'form-select'}
            #     )
            # else:
            #     fields[field].widget.attrs.update(
            #         {'class': 'form-control'}
            #     )
            fields[field].widget.attrs.update(
                {'class': 'form-control'}
            )

        return fields

    def __init__(self, *args, **kwargs):
        super(GeneralForms, self).__init__(*args, **kwargs)
        self. fields = self.custom_styles(self.fields)

    class Meta:
        model = None
        exclude = ('model_state', )