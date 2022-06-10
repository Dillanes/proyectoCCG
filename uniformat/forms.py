from cProfile import label
from dataclasses import field, fields
from django.forms import ModelForm
from uniformat.models import UFTCategorias, UFTNivel2, UFTNivel3, UFTNivel4

class UFTCategoriaForm(ModelForm):
    class Meta:
        model = UFTCategorias
        fields = '__all__'
        labels = {
            'descriEng': 'Descripción en Inglés',
            'descriSpa': 'Descripción en Español',
        }

class UFTNivel2Form(ModelForm):
    class Meta:
        model = UFTNivel2
        fields = '__all__'
        labels = {
            'descriEng': 'Descripción en Inglés',
            'descriSpa': 'Descripción en Español',
            'explicacionEng': 'Explicación en Inglés',
            'explicacionSpa': 'Explicación en Español',
        }

class UFTNivel3Form(ModelForm):
    class Meta:
        model = UFTNivel3
        fields = '__all__'
        labels = {
            'descriEng': 'Descripción en Inglés',
            'descriSpa': 'Descripción en Español',
            'explicacionEng': 'Explicación en Inglés',
            'explicacionSpa': 'Explicación en Español',
        }

class UFTNivel4Form(ModelForm):
    class Meta:
        model = UFTNivel4
        fields = '__all__'
        labels = {
            'descriEng': 'Descripción en Inglés',
            'descriSpa': 'Descripción en Español',
            'explicacionEng': 'Explicación en Inglés',
            'explicacionSpa': 'Explicación en Español',
        }