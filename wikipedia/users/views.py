from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import (UserCreationForm,
                    UserRegisterForm,
                    UserUpdateForm,
                    UserPrivacyForm)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (DetailView,
                                  UpdateView,
                                  DeleteView,
                                  View)
from django.contrib.auth.models import User
from .models import Profile, ProfilePrivacy
from django.http import Http404


# from django.contrib.postgres.search import

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Sucesfully registered {form.cleaned_data.get("username")}')
            return redirect('login')
        else:
            messages.warning(request, 'Something went wrong!')
            return redirect('register')
    else:
        context = {'form': UserRegisterForm(),
                   'title': 'Elektro | Register'}
        return render(request, 'wikipedia/register.html', context)


@login_required(login_url='login')
def profile(request):
    current_user = request.user
    if Profile.objects.filter(user_id=current_user).exists():
        Profile_object = Profile.objects.get(user_id=current_user.id)

    else:
        Profile_object = Profile

    context = {'user': current_user,
               'profile': Profile_object,
               'title': 'Elektro | Profile'}
    return render(request, 'wikipedia/profile.html', context)


class AuthorView(DetailView):
    model = Profile
    template_name = 'wikipedia/author.html'


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'wikipedia/user_delete.html'
    success_url = '/'


class ProfileView(LoginRequiredMixin, DetailView):
    model = Profile
    template_name = 'wikipedia/profile.html'
    # pk_url_kwarg = 'username'
    # context_object_name = "Profile"
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['Profile']=Profile.objects.filter(user_id=1)
    #     return context


class ProfileUpdate(LoginRequiredMixin, UpdateView):
    model = Profile
    fields = ['Name', 'surname']
    template_name = 'wikipedia/profile_update.html'


@login_required(login_url='login')
def profile_edit(request):
    if request.method == 'POST':
        # form = UserUpdateForm(request.POST, instance=request.user)
        # form.save()
        # Potrzebne jest przekazanie instancji klasy USER i referencji do profile
        form = UserUpdateForm(request.POST, instance=request.user.profile)
        print('Before valid')
        if form.is_valid():
            print('Valid')
            print(form.visible_fields())
            form.save()

            messages.success(request, "Edited your profile!")
            return redirect('/profile')
        else:
            messages.warning(request, 'Made some mistake during profile edit!')
            return redirect('/edit')
        pass
    else:
        return render(request, 'wikipedia/profile_update.html', {'form': UserUpdateForm(), 'title': 'Edycja Proflu'})
        # return render(request, 'wikipedia/profile_update.html',
        #               {'form': UserUpdateForm(instance=request.user.profile), 'title': 'Edycja Proflu'})


class OutsideProfileView(View):
    # Exists from 13
    def get(self, request, **kwargs):
        watched_user_id = kwargs['int']

        if User.objects.filter(id=watched_user_id).exists():
            current_profile = Profile.objects.get(user_id=watched_user_id)
            viewed_user = User.objects.get(id=watched_user_id)
            context = {'title': "Profile Overview",
                       'profile': current_profile,
                       'watched_user': viewed_user}
            return render(request, 'wikipedia/outside_profile_view.html', context=context)
        else:
            # custom 404 page for not found profile
            raise Http404


class UserPrivacyView(LoginRequiredMixin, View):

    def get(self, request):
        if ProfilePrivacy.objects.filter(user_id=request.user.id).exists():
            context = {
                'title': 'Profile privacy settings',
                'form': UserPrivacyForm(instance=request.user.profileprivacy)
            }
        else:
            context = {
                'title': 'Profile privacy settings',
                'form': UserPrivacyForm()
            }
        return render(request, 'wikipedia/user_privacy.html', context=context)

    def post(self, request, **kwargs):

        if ProfilePrivacy.objects.filter(user_id=request.user.id).exists():
            form = UserPrivacyForm(request.POST, instance=request.user)
            if form.is_valid():
                print(form.cleaned_data)
                form.save()
        else:
            form = UserPrivacyForm(request.POST)
            if form.is_valid():
                print(form.cleaned_data)
                form.instance.user = request.user
                form.save()
        return redirect('/profile')
