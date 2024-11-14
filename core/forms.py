from django import forms
from core.models import UserModel, JobModel, CurriculumModel, ApplicationModel, LanguageModel, ExperienceModel, \
    QualificationModel, AddressModel


class UserForm(forms.ModelForm):
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'placeholder': 'email@dominio.com'}))
    full_name = forms.CharField(label='Nome Completo',
                                widget=forms.TextInput(attrs={'placeholder': 'ex. Maria Aparecida'}))
    birth_date = forms.DateField(label='Aniversário',
                                 widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'maxlength': 10}))
    phone_number = forms.CharField(label='Celular',
                                   widget=forms.TextInput(attrs={'placeholder': '(__) _____-____', 'maxlength': 15}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput)

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
                                 widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'maxlength': 10}))
    phone_number = forms.CharField(label='Celular', required=False,
                                   widget=forms.TextInput(attrs={'placeholder': '(__) _____-____', 'maxlength': 15}))

    class Meta:
        model = UserModel
        fields = ['email', 'full_name', 'birth_date', 'phone_number']


class AddressForm(forms.ModelForm):
    zipcode = forms.CharField(label='CEP', widget=forms.TextInput(attrs={'placeholder': '00000-000', 'maxlength': 9}))
    address = forms.CharField(label='Endereço')
    number = forms.CharField(label='Número', required=False)
    complement = forms.CharField(label='Complemento', required=False)
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
        fields = ['education', 'level', 'about']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = '__all__'

    @staticmethod
    def create_apply(**kwargs):
        apply = ApplicationModel()
        apply.job = kwargs['job']
        apply.job.count_applications += 1
        apply.curriculum = CurriculumModel.objects.get_or_create(user=kwargs['user'])[0]
        apply.status = 'Confirmada'

        # SAVE OBJECTS
        apply.job.save()
        apply.save()


class LanguageForm(forms.ModelForm):
    class Meta:
        model = LanguageModel
        fields = '__all__'


class ExperienceForm(forms.ModelForm):
    company = forms.CharField(label='Empresa')
    position = forms.CharField(label='Cargo', widget=forms.TextInput(attrs={'placeholder': 'ex. Diretor'}))
    start_date = forms.DateField(label='Início', required=True,
                                 widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'maxlength': 10}))
    end_date = forms.DateField(label='Saída', required=False,
                               widget=forms.DateInput(attrs={'placeholder': 'DD/MM/AAAA', 'maxlength': 10}))
    is_actual = forms.BooleanField(label='Trabalho Atual', required=False)
    address = forms.CharField(label='Local', widget=forms.TextInput(attrs={'placeholder': 'ex. São Paulo, SP'}))
    responsibilities = forms.CharField(label='Funções', required=False, widget=forms.Textarea(
        attrs={'placeholder': 'ex. Atendimento ao público, Pacote Office'}))

    class Meta:
        model = ExperienceModel
        fields = ['company', 'position', 'start_date', 'end_date', 'address', 'is_actual', 'responsibilities']

    def save(self, commit=True, **kwargs):
        self.instance.curriculum = kwargs['curriculum']
        self.instance.company = self.cleaned_data['company']
        self.instance.position = self.cleaned_data['position']
        self.instance.start_date = self.cleaned_data['start_date']
        self.instance.end_date = self.cleaned_data['end_date']
        self.instance.is_actual = self.cleaned_data['is_actual']
        self.instance.responsibilities = self.cleaned_data['responsibilities']
        self.instance.save()
        return self.instance


class QualificationForm(forms.ModelForm):
    class Meta:
        model = QualificationModel
        fields = ['name', 'institution', 'date']

    def save(self, commit=True, **kwargs):
        self.instance.curriculum = kwargs['curriculum']
        self.instance.name = self.cleaned_data['name']
        self.instance.institution = self.cleaned_data['institution']
        self.instance.date = self.cleaned_data['date']
        self.instance.save()
        return self.instance
