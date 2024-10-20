from django.contrib import admin
from .models import UserModel, ExperienceModel, JobModel, QualificationModel, LanguageModel, \
    CurriculumModel, ApplicationModel, CompanyModel


# Register your models here.

@admin.register(UserModel)
@admin.register(ExperienceModel)
@admin.register(JobModel)
@admin.register(QualificationModel)
@admin.register(LanguageModel)
@admin.register(CurriculumModel)
@admin.register(ApplicationModel)
@admin.register(CompanyModel)


class UserModelAdmin(admin.ModelAdmin):
    pass

class CompanyModelAdmin(admin.ModelAdmin):
    pass

class ApplicationAdmin(admin.ModelAdmin):
    pass

class JobModelAdmin(admin.ModelAdmin):
    pass

class CurriculumModelAdmin(admin.ModelAdmin):
    pass

class LanguageModelAdmin(admin.ModelAdmin):
    pass

class QualificationModelAdmin(admin.ModelAdmin):
    pass

class ExperiencesModelAdmin(admin.ModelAdmin):
    pass