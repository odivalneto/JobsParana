from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import stringfilter, register
from django.views.generic import TemplateView, ListView, DetailView, FormView
from core.forms import UserForm, CurriculumForm, ProfileForm
from core.models import JobModel, CurriculumModel, UserModel, ApplicationModel

@register.filter(is_safe=True)
@stringfilter
def split_url(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)

class UserRegistrationView(FormView):
    form_class = UserForm
    template_name = 'registration/registration.html'
    success_url = '/'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()

        return redirect(self.success_url)


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

    # def get_context_data(self, **kwargs):
    #     job = self.queryset.get(id=kwargs['id'])
    #
    #     context = {
    #         'job': job,
    #     }
    #
    #     return context

    # def post(self, request, *args, **kwargs):
    #     return


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


class MyApplicationsView(LoginRequiredMixin, ListView):
    model = ApplicationModel
    context_object_name = 'applications'
    template_name = 'candidates/applications/list.html'
    paginate_by = 100

    def get_queryset(self):
        return self.queryset.filter(is_active=True).order_by('-application_date')


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
