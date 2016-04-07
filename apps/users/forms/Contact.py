# coding=utf-8
from django import forms
from apps.users.models import Contact


class ContactForm(forms.ModelForm):

    max_length = 80
    contact_name = forms.CharField(
        label=u'* Nombre Completo:',
        required=True,
        max_length=max_length,
        widget=forms.TextInput(
            attrs={'class': 'form required', 'size': '40', 'placeholder': 'Escriba su nombre'}
        ),
        error_messages={
            'required': u'Este campo es requerido y no se puede dejar vacío.',
            'max_length': u'Este campo es demasiado largo (máximo %d caracteres).' % max_length,
        }
    )

    max_length = 60
    contact_email = forms.CharField(
        label=u'* Email:',
        required=True,
        max_length=max_length,
        widget=forms.EmailInput(
            attrs={'class': 'form required email', 'size': '40', 'placeholder': 'Escriba su email'}
        ),
        error_messages={
            'required': u'Este campo es requerido y no se puede dejar vacío.',
            'max_length': u'Este campo es demasiado largo (máximo %d caracteres).' % max_length,
        }
    )

    max_length = 12
    contact_phone = forms.CharField(
        label=u'* Teléfono / Celular:',
        required=True,
        max_length=max_length,
        widget=forms.TextInput(
            attrs={'class': 'form required', 'size': '40', 'placeholder': 'Escriba su teléfono'}
        ),
        error_messages={
            'required': u'Este campo es requerido y no se puede dejar vacío.',
            'max_length': u'Este campo es demasiado largo (máximo %d caracteres).' % max_length,
        }
    )

    max_length = 500
    contact_message = forms.CharField(
        label=u'Mensaje:',
        required=False,
        max_length=max_length,
        widget=forms.Textarea(
            attrs={'class': 'form required area', 'placeholder': 'Escriba su mensaje...'}
        ),
        error_messages={
            'required': u'Este campo es requerido y no se puede dejar vacío.',
        }
    )

    class Meta:
        model = Contact
        fields = ("contact_name", "contact_email", "contact_phone", "contact_message")