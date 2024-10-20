from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from core.forms import UserForm, CurriculumForm, ProfileForm
from core.models import JobModel, CurriculumModel


# Create your views here.

def index(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'index.html', context={'form': form})


class JobListView(LoginRequiredMixin, ListView):
    model = JobModel
    context_object_name = 'jobs'
    template_name = 'jobs.html'
    paginate_by = 10
    allow_empty = True

    def get_queryset(self):
        return JobModel.objects.filter(is_available=True)


# @login_required()
# def list_jobs(request):
#     jobs = JobModel.objects.all()
#
#     return render(request, 'jobs.html', context={'jobs': jobs})


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile_view.html'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        form = ProfileForm(instance=self.request.user)
        profile_form = ProfileForm(instance=self.request.user)

        context = {
            'form': form,
            'profile_form': profile_form,
        }

        return context

    def post(self, request, *args, **kwargs):
        form = ProfileForm(request.POST, instance=self.request.user)
        profile_form = ProfileForm(request.POST, instance=self.request.user)
        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()

        context = {
            'form': form,
            'profile_form': profile_form,
        }
        if form.is_valid():
            form.save()

        return render(request, 'profile_view.html', context=context)

    def get(self, request, *args, **kwargs):
        form = ProfileForm(instance=self.request.user)
        profile_form = ProfileForm(instance=self.request.user)
        context = {
            'form': form,
            'profile_form': profile_form,
        }

        return render(request, self.template_name, context)


@login_required()
def profile(request):
    profile = CurriculumModel.objects.get_or_create(user=request.user)[0]
    profile_form = ProfileForm(instance=profile.user)

    form = CurriculumForm(instance=profile)

    if request.method == 'POST':
        form = CurriculumForm(request.POST, instance=profile)
        profile_form = ProfileForm(request.POST, instance=profile.user)

        if form.is_valid() and profile_form.is_valid():
            form.save()
            profile_form.save()

    return render(request, 'profile.html', context={'profile': profile, 'form': form, 'profile_form': profile_form})


def login(request):
    return render(request, 'registration/login.html')
