from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Profile, Project
from .forms import UpdateProfile, PostProjectForm, RatingsForm
from django.http import HttpResponseRedirect


def index(request):
    projects = Project.get_all()
    return render(request, 'index.html', {'projects': projects})


@login_required(login_url='/accounts/login/')
def profile(request):
    user = request.user
    projects = Project.get_by_user(user.id)
    profiles = Profile.get_user(user.id)
    if profiles:
        profile = profiles[len(profiles)-1]
    else:
        profile = profiles

    if request.method == 'POST':
        profile_form = UpdateProfile(request.POST, request.FILES)
        upload_form = PostProjectForm(request.POST, request.FILES)
        rating_form = RatingsForm(request.POST)
        if profile_form.is_valid():
            if Profile.get_user(user.id):
                deleter = Profile.get_user(user.id)
                deleter.delete()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save_profile()
            return HttpResponseRedirect('/profile')
        if upload_form.is_valid():
            project = upload_form.save(commit=False)
            project.user = user
            project.save_project()
    else:
        profile_form = UpdateProfile()
        upload_form = PostProjectForm()
        rating_form = RatingsForm
    return render(request, 'profile.html', {'user': user, 'profile': profile,"projects":projects,'profile_form': profile_form,
                                            'upload_form': upload_form, 'rating_form': rating_form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'search' in request.GET and request.GET['search']:
        search_term = request.GET.get('search')
        search_projects = Project.search_project(search_term)
        search_prof = Profile.search_profiles(search_term)
        message = f'{search_term}'

        return render(request, 'search.html', {'message': message, 'projects': search_projects, 'profiles': search_prof})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {'message': message})

@login_required(login_url='/accounts/login/')
def single_project(request, project):
    ratings = Ratings.get_by_project()
    project = Project.get_project_by_id(project)
    if request.method == 'POST':
        rating_form = RatingsForm(request.POST)
        if rating_form.is_valid():
            rating = rating_form.save(commit=False)
            rating.user = user
            rating.Project = picture
            rating.save()
            return redirect('project', project.id)
    else:
        rating_form = RatingsForm()

    return render(request, 'project.html', {'rating_form': rating_form, 'project': project, 'user': user, 'ratings': ratings})
