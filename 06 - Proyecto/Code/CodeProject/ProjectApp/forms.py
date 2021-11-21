from django import forms
from .models import TipoDocumento, Usuarios, Roles, Estado

class UsuariosForm(forms.ModelForm): # Formulario para crear usuarios
    NombreUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Nombre del Usuario")
    ApellidoUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Apellido del Usuario")
    TelefonoUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Teléfono del Usuario")
    EmailUsuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Email del Usuario")
    NumeroDocumento = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Número de Documento")
    Usuario = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Usuario")
    Contraseña = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}), label="Contraseña")
    Estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleecione un Estado")
    Roles = forms.ModelChoiceField(queryset=Roles.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Rol")
    TipoDocumento = forms.ModelChoiceField(queryset=TipoDocumento.objects.all(), widget=forms.Select(attrs={'class':'input'}), label="Seleccione un Tipo de Documento")
    class Meta:
        model = Usuarios
        #fields = ['NombreUsuario', 'ApellidoUsuario', 'TelefonoUsuario', 'EmailUsuario', 'NumeroDocumento', 'Usuario', 'Contraseña', 'Estado', 'Roles', 'TipoDocumento']
        fields = '__all__' # sirve para listarlos todos