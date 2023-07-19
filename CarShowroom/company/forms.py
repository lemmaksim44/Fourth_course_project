from .models import *
from django.forms import ModelForm, TextInput, Textarea, NumberInput, CheckboxInput


class RequestForm(ModelForm):
    class Meta:
        model = Request
        fields = ['name_service', 'client_name', 'client_phone', 'client_email', 'comment', 'status']

        widgets = {
            'name_service': TextInput(attrs={
                'id': 'input_name_service_id',
                'type': 'hidden',
            }),
            'client_name': TextInput(attrs={
                'id': 'input_name_id',
                'class': 'input_text',
                'placeholder': 'Имя',
            }),
            'client_phone': NumberInput(attrs={
                'id': 'input_phone_id',
                'class': 'input_number',
                'placeholder': 'Телефон',
            }),
            'client_email': TextInput(attrs={
                'id': 'input_email_id',
                'class': 'input_text',
                'placeholder': 'E-mail',
            }),
            'comment': Textarea(attrs={
                'id': 'input_comment_id',
                'class': 'input_textarea',
                'placeholder': 'Комментарий',
            }),
            'status': CheckboxInput(attrs={
                'id': 'input_checkbox_id',
                'class': 'input_checkbox',
                'type': 'hidden',
            })
        }


class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['client_name', 'client_phone', 'client_email']

        widgets = {
            'client_name': TextInput(attrs={
                'id': 'input_name_id_2',
                'type': 'hidden',
            }),
            'client_phone': NumberInput(attrs={
                'id': 'input_phone_id_2',
                'type': 'hidden',
            }),
            'client_email': TextInput(attrs={
                'id': 'input_email_id_2',
                'type': 'hidden',
            }),
        }