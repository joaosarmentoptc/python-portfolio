from django.shortcuts import render, redirect

from .forms import DweetForm
from .models import Profile, Dweet


# Create your views here.
def dashboard(request):
    form = DweetForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            dweet = form.save(commit=False)
            dweet.user = request.user
            dweet.save()
            return redirect("dwitter:dashboard")

    followed_tweets = Dweet.objects.filter(
        user__profile__in=request.user.profile.follows.all()
    ).order_by('-created_at')

    context = {
        'form': form,
        'dweets': followed_tweets
    }

    return render(request, 'dwitter/dashboard.html', context)


def profile_list(request):
    profiles = Profile.objects.exclude(user=request.user)
    context = {
        'profiles': profiles
    }
    return render(request, 'dwitter/profile_list.html', context)


def profile(request, pk):
    if not hasattr(request.user, 'profile'):
        missing_profile = Profile(user=request.user)
        missing_profile.save()

    profile = Profile.objects.get(pk=pk)
    context = {
        'profile': profile
    }

    if request.method == 'POST':
        current_user_profile = request.user.profile
        data = request.POST
        action = data.get("follow")
        if action == 'follow':
            current_user_profile.follows.add(profile)
        elif action == 'unfollow':
            current_user_profile.follows.remove(profile)
        current_user_profile.save()
        return redirect(request.META['HTTP_REFERER'])

    return render(request, 'dwitter/profile.html', context)