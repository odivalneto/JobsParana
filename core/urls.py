from django.shortcuts import redirect
from django.urls import path

from core.views import JobListView, MyProfileView, MyApplicationsView, MyCurriculumView, JobDetailView, \
    UserRegistrationView

app_name = 'core'

urlpatterns = [
    path('', lambda request: redirect('core:jobs'), name='index'),
    path('jobs/', JobListView.as_view(), name='jobs'),
    path('jobs/<pk>/detail/', JobDetailView.as_view(), name='job_detail'),
    path('profile/', MyProfileView.as_view(), name='profile'),
    path('profile/registration/', UserRegistrationView.as_view(), name='registration'),
    path('curriculum/<id>/', MyCurriculumView.as_view(), name='curriculum'),
    path('applications/<id>/', MyApplicationsView.as_view(), name='applications'),
]
