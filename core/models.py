import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _


# Create your models here.

class BaseUserModel(BaseUserManager):

    def _create_user(self, email, password=None, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

    def create_staff(self, email, password=None, **extra_fields):
        user = self._create_user(email, password, **extra_fields)
        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user


class UserModel(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(unique=True)
    full_name = models.CharField(_('Full Name'), max_length=255)
    birth_date = models.DateField(_('Birthday'), null=True, blank=True)
    phone_number = models.CharField(_('Phone'), max_length=255)
    registration_date = models.DateField(_('Date Register'), auto_now_add=True)
    last_login = models.DateField(_('Last Access'), auto_now_add=True)
    is_active = models.BooleanField(_('Active'), default=True)
    is_staff = models.BooleanField(_('Staff'), default=False)
    is_superuser = models.BooleanField(_('Admin'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'password']

    objects = BaseUserModel()

    class Meta:
        ordering = ['email']
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.full_name


class CurriculumModel(models.Model):
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

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='user')
    about = models.TextField(blank=True)
    education = models.CharField(_('Education'), max_length=50, choices=type_education, blank=True)
    level = models.CharField(_('Level'), max_length=50, choices=level_education, blank=True)

    class Meta:
        ordering = ['user']
        verbose_name = 'Curriculum'
        verbose_name_plural = 'Curriculums'

    def __str__(self):
        return self.user.full_name


class ExperienceModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    curriculum = models.ForeignKey('CurriculumModel', on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    is_actual = models.BooleanField(default=False)
    address = models.CharField(max_length=255)
    responsibilities = models.TextField()

    class Meta:
        ordering = ['company']
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'

    def __str__(self):
        return self.company


class QualificationModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    curriculum = models.ForeignKey('CurriculumModel', on_delete=models.CASCADE, related_name='qualifications')
    name = models.CharField(max_length=255)
    institution = models.CharField(max_length=255)
    date = models.DateField()

    class Meta:
        ordering = ['name']
        verbose_name = 'Qualification'
        verbose_name_plural = 'Qualifications'

    def __str__(self):
        return self.name


class LanguageModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    curriculum = models.ForeignKey('CurriculumModel', on_delete=models.CASCADE, related_name='languages')
    name = models.CharField(max_length=255)
    level = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __str__(self):
        return self.name


class CompanyModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_company = models.CharField(_('Nome Company'), max_length=255)
    address = models.CharField(_('Address'), max_length=255)
    district = models.CharField(_('District'), max_length=255)
    city = models.CharField(_('City'), max_length=255)
    state = models.CharField(_('State'), max_length=255)
    country = models.CharField(_('Country'), max_length=255)
    phone = models.CharField(_('Phone'), max_length=255)
    email = models.EmailField(_('Email'), unique=True)

    class Meta:
        ordering = ['name_company']
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.name_company


class JobModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    company = models.ForeignKey('CompanyModel', on_delete=models.CASCADE, related_name='company')
    title = models.CharField(_('Title'), max_length=255)
    id_job = models.CharField(_('ID Job'), max_length=255, default='')
    is_available = models.BooleanField(_('Available'), default=True)
    is_urgent = models.BooleanField(_('Urgent'), default=False)
    is_confidential = models.BooleanField(_('Confidential'), default=False)
    is_pcd = models.BooleanField(_('Only PCD'), default=False)
    is_master_class = models.BooleanField(_('Master Class'), default=False)
    requirements = models.TextField(_('Requirements'), default='')
    registration_date = models.DateField(_('Register Date'), auto_now_add=True)
    end_registration_date = models.DateField(_('End Registration Date'), null=True, blank=True)
    benefits = models.TextField(_('Benefits'), default='')
    time_scale = models.CharField(_('Time Scale'), max_length=255, default='')
    remuneration = models.DecimalField(_('Remuneration'), default=0, decimal_places=2, max_digits=10)
    count_applications = models.IntegerField(_('Applications Count'), default=0)

    REQUIRED_FIELDS = ['title', 'description', 'status', 'company']

    class Meta:
        ordering = ['title', '-registration_date']
        verbose_name = 'Job'
        verbose_name_plural = 'Jobs'

    def __str__(self):
        return self.title


class ApplicationModel(models.Model):

    status_application = {
        'Confirmada' : 'Confirmada',
        'Selecionada' : 'Selecionada',
        'Não Selecionada' : 'Não Selecionada',
        'Finalizada' : 'Finalizada',
    }

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job = models.ForeignKey('JobModel', on_delete=models.CASCADE, related_name='job_applications')
    curriculum = models.ForeignKey('CurriculumModel', on_delete=models.CASCADE, related_name='curriculum_applications')
    application_date = models.DateField(_('Application Date'), auto_now_add=True)
    status = models.CharField(_('Status'), max_length=30, choices=status_application)

    class Meta:
        ordering = ['job', 'curriculum']
        verbose_name = 'Application'
        verbose_name_plural = 'Applications'

    def __str__(self):
        return self.job.title

    def create_application(self, **kwargs):
        application = self
        application.job = kwargs['job']
        application.curriculum = kwargs['curriculum']
        application.status = 'Confirmada'
        application.save()

        print(application)
