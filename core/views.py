from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import stringfilter, register
from django.views.generic import TemplateView, ListView, DetailView, FormView
from core.forms import UserForm, CurriculumForm, ProfileForm
from core.models import JobModel, CurriculumModel, UserModel, ApplicationModel


@register.filter(is_safe=True)
@stringfilter
def split_url(string, sep):
    return string.split(sep)


# MARK: - PROFILE
class UserRegistrationView(FormView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return redirect(self.success_url)


class MyProfileView(LoginRequiredMixin, FormView):
    model = UserModel
    template_name = 'candidates/profile/index.html'
    form_class = ProfileForm

    def get_initial(self):
        form = ProfileForm(self.request.user)

        return form

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
            self.form_class = form_class
            return form_class


# MARK: - JOBS
class JobListView(LoginRequiredMixin, ListView):
    model = JobModel
    context_object_name = 'jobs'
    template_name = 'candidates/jobs/list.html'
    paginate_by = 100
    allow_empty = True
    queryset = JobModel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_available=True).order_by('-id')


class JobDetailView(LoginRequiredMixin, DetailView):
    model = JobModel
    context_object_name = 'job'
    template_name = 'candidates/jobs/detail.html'


# MARK: - CURRICULUM
class MyCurriculumView(LoginRequiredMixin, TemplateView):
    template_name = 'candidates/profile/curriculum.html'

    def post(self, request, *args, **kwargs):

        curriculum = get_object_or_404(CurriculumModel, user_id=kwargs.get('id'))

        if request.method == 'POST':
            form = CurriculumForm(request.POST, instance=curriculum)

            if form.is_valid():
                form.save()

        return self.get(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):

        curriculum = CurriculumModel.objects.get_or_create(user_id=kwargs.get('id'))[0]
        form = CurriculumForm(instance=curriculum)

        return render(request, 'candidates/profile/curriculum.html', context={'curriculum': curriculum, 'form': form})

# MARK: - APPLICATIONS
class MyApplicationsView(LoginRequiredMixin, ListView):
    model = ApplicationModel
    context_object_name = 'applications'
    template_name = 'candidates/applications/list.html'
    paginate_by = 100

    def get_queryset(self):
        return self.queryset.filter(is_active=True).order_by('-application_date')

# MARK: - ACCOUNTS
def login(request):
    return render(request, 'registration/login.html')
