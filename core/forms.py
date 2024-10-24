from cProfile import label

from django import forms
from django.shortcuts import get_object_or_404

from core.models import UserModel, JobModel, CurriculumModel, ApplicationModel, LanguageModel, ExperienceModel, \
    QualificationModel, AddressModel


class UserForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'email@dominio.com'}))
    full_name = forms.CharField(label='Nome Completo',
                                widget=forms.TextInput(attrs={'placeholder': 'ex. Maria Aparecida'}))
    birth_date = forms.DateField(label='Aniversário', widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))
    phone_number = forms.CharField(label='Celular', widget=forms.TextInput(attrs={'placeholder': '(__) _ ____-____'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

    # use_required_attribute = True

    class Meta:
        model = UserModel
        fields = ['email', 'full_name', 'birth_date', 'phone_number', 'password']

    def clean(self):
        cleaned_data = self.cleaned_data
        return cleaned_data

    def save(self, commit=True):
        data = self.clean()
        user = UserModel.objects.create_user(email=data['email'], password=data['password'],
                                             full_name=data['full_name'],
                                             birth_date=data['birth_date'], phone_number=data['phone_number'])
        user.save()


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.TextInput(attrs={'placeholder': 'email@dominio.com'}))
    full_name = forms.CharField(label='Nome Completo', required=True)
    birth_date = forms.DateField(label='Aniversário', required=False,
                                 widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA'}))
    phone_number = forms.CharField(label='Celular', required=False,
                                   widget=forms.TextInput(attrs={'placeholder': '(__) _ ____-____'}))

    class Meta:
        model = UserModel
        fields = ['email', 'full_name', 'birth_date', 'phone_number']


class AddressForm(forms.ModelForm):
    zipcode = forms.CharField(label='CEP', widget=forms.TextInput(attrs={'placeholder': '00000-000'}))
    address = forms.CharField(label='Endereço')
    number = forms.CharField(label='Número')
    complement = forms.CharField(label='Complemento')
    region = forms.CharField(label='Bairro')
    city = forms.CharField(label='Cidade')
    state = forms.CharField(label='Estado')
    country = forms.CharField(label='País')

    class Meta:
        model = AddressModel
        fields = ['zipcode', 'address', 'number', 'complement', 'region', 'city', 'state', 'country']


class JobsForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'


class CurriculumForm(forms.ModelForm):
    level_education = {
        'Incompleto': 'Incompleto',
        'Completo': 'Completo',
        'Cursando': 'Cursando'
    }

    type_education = {
        'Fundamental': 'Fundamental',
        'Médio': 'Medio',
        'Superior': 'Superior',
        'Pós Graduação': 'Pós Graduação',
        'Metrado': 'Metrado',
        'Doutorado': 'Doutorado'
    }

    about = forms.CharField(label='Sobre', widget=forms.Textarea(attrs={'placeholder': 'Conte mais sobre você...'}),
                            required=False)
    education = forms.ChoiceField(label='Escolaridade', choices=type_education)
    level = forms.ChoiceField(label='Nível', choices=level_education)

    class Meta:
        model = CurriculumModel
        fields = ['about', 'education', 'level']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = '__all__'

    @staticmethod
    def create_apply(**kwargs):
        apply = ApplicationModel()
        apply.job = kwargs['job']
        apply.curriculum = get_object_or_404(CurriculumModel, user=kwargs['user'])
        apply.status = 'Confirmada'
        apply.save()


class LanguageForm(forms.ModelForm):
    class Meta:
        model = LanguageModel
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    class Meta:
        model = ExperienceModel
        fields = '__all__'


class QualificationForm(forms.ModelForm):
    class Meta:
        model = QualificationModel
        fields = '__all__'
