from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView
from core.forms import UserForm, CurriculumForm, ProfileForm, ApplicationForm, AddressForm
from core.models import JobModel, CurriculumModel, UserModel, ApplicationModel, QualificationModel, AddressModel


# MARK: - PROFILE
class UserRegistrationView(FormView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = 'core:index'

    def post(self, *args, **kwargs):
        form = self.form_class(self.request.POST)
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
    paginate_by = 30
    allow_empty = True
    queryset = JobModel.objects.all()

    def get_queryset(self):
        return self.queryset.filter(is_available=True).order_by('-id')


class JobDetailView(LoginRequiredMixin, DetailView):
    model = JobModel
    context_object_name = 'job'
    template_name = 'candidates/jobs/detail.html'
    success_url = 'jobs:detail'

    def get_context_data(self, **kwargs):
        job = self.get_object()
        is_already = ApplicationModel.objects.filter(job=job, curriculum__user=self.request.user).exists()
        is_curriculum_created = CurriculumModel.objects.filter(user=self.request.user).exists()

        context = {
            'job': job,
            'is_already': is_already,
            'is_curriculum_created': is_curriculum_created
        }

        return context

    def post(self, *args, **kwargs):
        form = ApplicationForm()
        form.create_apply(user=self.request.user, job=self.get_object())

        return self.get(*args, **kwargs)


# MARK: - CURRICULUM
class MyCurriculumView(LoginRequiredMixin, TemplateView):
    template_name = 'candidates/profile/index.html'


class MyProfileDetailView(LoginRequiredMixin, DetailView):
    model = UserModel
    template_name = 'candidates/profile/profile.html'
    success_url = 'core:profile'

    def get_context_data(self, **kwargs):
        form = ProfileForm(instance=self.get_object())
        context = {
            'form': form
        }
        return context

    def post(self, *args, **kwargs):
        form = ProfileForm(self.request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return self.get(*args, **kwargs)


class MyAddressDetailView(LoginRequiredMixin, DetailView):
    model = AddressModel
    template_name = 'candidates/profile/address.html'

    def get_context_data(self, **kwargs):
        form = AddressForm(instance=self.get_object())
        context = {
            'form': form
        }
        return context

    def get_object(self, queryset=None):
        obj = AddressModel.objects.get_or_create(user_id=self.request.user.id)[0]
        return obj

    def post(self, *args, **kwargs):
        form = AddressForm(self.request.POST, instance=self.get_object())
        if form.is_valid():
            form.save()
        return self.get(*args, **kwargs)


class MyQualificationsDetailView(LoginRequiredMixin, ListView):
    model = QualificationModel
    template_name = 'candidates/profile/qualifications.html'
    context_object_name = 'qualifications'


class MyExperienceDetailView(LoginRequiredMixin, ListView):
    model = ApplicationModel
    template_name = 'candidates/profile/experiences.html'
    context_object_name = 'experiences'


# MARK: - APPLICATIONS
class MyApplicationsView(LoginRequiredMixin, ListView):
    model = ApplicationModel
    context_object_name = 'applications'
    template_name = 'candidates/applications/list.html'
    paginate_by = 20
    queryset = ApplicationModel.objects.all().order_by('-id')

    def get(self, request, *args, **kwargs):
        applications = self.queryset.filter(curriculum__user_id=kwargs.get('id'))

        return render(request, self.template_name, context={'applications': applications})


# MARK: - ACCOUNTS
def login(request):
    return render(request, 'registration/login.html')
