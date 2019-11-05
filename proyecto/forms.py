from django import forms

class RegistroForm(forms.Form):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Usuario', 'autocomplete': 'off'}))
    first_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Nombres', 'autocomplete': 'off'}))
    last_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Apellidos', 'autocomplete': 'off'}))
    email = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Correo Electronico', 'autocomplete': 'off'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña', 'autocomplete': 'off'}))
    confirm_password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Confirmar contraseña', 'autocomplete': 'off'}))

class IngresarForm(forms.Form):
    username = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Usuario',
                'autocomplete': 'off'
            }
        )
    )

    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Contraseña',
                'autocomplete': 'off'
            }
        )
    )

class PostForm(forms.Form):
    titulo = forms.CharField(
        label='Titulo',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Titulo',
                'autocomplete': 'off'
            }
        )
    )

    texto = forms.CharField(
        label='Texto',
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Texto',
                'autocomplete': 'off'
            }
        )
    )

    post_status_choices = [
        ("DRAFT", "Borrador"),
        ("Publish", "Publicado")
    ]

    estado = forms.ChoiceField(
        choices= post_status_choices
    )

class Comentario(forms.Form):
    texto = forms.CharField(
        label="",
        widget=forms.Textarea(
            attrs={
                'rows':4,
                'cols':80,
                'autocomplete': 'off',
                'placeholder': 'Text',
            }
        )
    )