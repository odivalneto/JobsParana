from django.shortcuts import redirect
from django.urls import path

from core.views import JobListView, MyProfileView, MyApplicationsView, MyCurriculumView, JobDetailView, \
    UserRegistrationView, MyAddressDetailView, MyQualificationsDetailView, MyExperienceDetailView, MyProfileDetailView

app_name = 'core'

urlpatterns = [
    path('', lambda request: redirect('core:jobs'), name='index'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/<pk>/detail/', JobDetailView.as_view(), name='job_detail'),
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('profile/registration/', UserRegistrationView.as_view(), name='registration'),
    path('curriculum/', MyCurriculumView.as_view(), name='curriculum'),
    path('curriculum/<pk>/profile/', MyProfileDetailView.as_view(), name='curriculum_profile'),
    path('curriculum/<pk>/address/', MyAddressDetailView.as_view(), name='curriculum_address'),
    path('curriculum/<id>/qualifications/', MyQualificationsDetailView.as_view(), name='curriculum_qualifications'),
    path('curriculum/<id>/experiences/', MyExperienceDetailView.as_view(), name='curriculum_experiences'),
    path('applications/<id>/', MyApplicationsView.as_view(), name='applications'),
]
