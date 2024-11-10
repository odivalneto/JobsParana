from django.shortcuts import redirect
from django.urls import path

from core.views import JobListView, MyProfileView, MyCurriculumView, JobDetailView, \
    UserRegistrationView, MyAddressDetailView, MyQualificationsDetailView, MyExperienceDetailView, MyProfileDetailView, \
    MyApplicationDetailView, SearchView, MyExperienceListView, MyApplicationsListView

app_name = 'core'

urlpatterns = [
    path('', lambda request: redirect('core:jobs'), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/<pk>/detail/', JobDetailView.as_view(), name='job_detail'),
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('profile/registration/', UserRegistrationView.as_view(), name='registration'),
    path('curriculum/', MyCurriculumView.as_view(), name='curriculum'),
    path('curriculum/<pk>/profile/', MyProfileDetailView.as_view(), name='curriculum_profile'),
    path('curriculum/<pk>/address/', MyAddressDetailView.as_view(), name='curriculum_address'),
    path('curriculum/<id>/qualifications/', MyQualificationsDetailView.as_view(), name='curriculum_qualifications'),
    path('curriculum/<id>/experiences/', MyExperienceListView.as_view(), name='curriculum_experiences'),
    path('curriculum/<id>/experiences/<pk>/detail/', MyExperienceDetailView.as_view(),
         name='curriculum_experiences_detail'),
    path('applications/<id>/', MyApplicationsListView.as_view(), name='applications'),
    path('applications/<pk>/detail/', MyApplicationDetailView.as_view(), name='application_detail'),
]
