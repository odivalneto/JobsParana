from django.contrib import admin
from .models import UserModel, ExperienceModel, JobModel, QualificationModel, LanguageModel, \
    CurriculumModel, ApplicationModel, CompanyModel, AddressModel


# Register your models here.


@admin.register(AddressModel)
class AddressModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'user__email']
    pass


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
    list_filter = ['is_staff', 'is_superuser']
    filter_horizontal = ['groups', 'user_permissions']
    pass


@admin.register(CompanyModel)
class CompanyModelAdmin(admin.ModelAdmin):
    list_display = ['name_company', 'address', 'email', 'phone']
    pass


@admin.register(ApplicationModel)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['curriculum', 'job', 'application_date']
    pass


@admin.register(JobModel)
class JobModelAdmin(admin.ModelAdmin):
    list_display = ['title','registration_date', 'is_available']
    pass


@admin.register(CurriculumModel)
class CurriculumModelAdmin(admin.ModelAdmin):
    list_display = ['user','user__email', 'user_id']
    pass


@admin.register(LanguageModel)
class LanguageModelAdmin(admin.ModelAdmin):
    pass


@admin.register(QualificationModel)
class QualificationModelAdmin(admin.ModelAdmin):
    pass


@admin.register(ExperienceModel)
class ExperiencesModelAdmin(admin.ModelAdmin):
    pass
