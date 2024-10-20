from django import forms
from core.models import UserModel, JobModel, CurriculumModel, ApplicationModel, LanguageModel, ExperienceModel, \
    QualificationModel


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    birth_date = forms.DateField(widget=forms.DateInput, required=False)

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
                                             birth_date=data['birth_date'])
        user.save()


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    birth_date = forms.DateField(required=False, widget=forms.DateInput())
    phone_number = forms.CharField(required=False)

    class Meta:
        model = UserModel
        fields = ['email', 'full_name', 'birth_date', 'phone_number']


class JobsForm(forms.ModelForm):
    class Meta:
        model = JobModel
        fields = '__all__'


class CurriculumForm(forms.ModelForm):
    about = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = CurriculumModel
        fields = ['about']


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = ApplicationModel
        fields = '__all__'


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
