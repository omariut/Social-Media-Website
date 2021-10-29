from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.serializers import serialize
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from profiles.models import Profile, Relationship, Notification
from posts.models import Post, Like, Comment
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from posts.mixins import OwnerOnlyMixin


class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/friends.html'

    def get_queryset(self):
        user_profile = self.request.user.profile
        friends=user_profile.get_friend_list()
        print(friends)
        return friends

class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = 'profile'
    template_name = 'profiles/profile.html'
class NotificationListView(ListView):
    model = Notification
    context_object_name = 'notification_list'
    template_name = 'profiles/notification-list.html'

class ProfileEditView( OwnerOnlyMixin, UpdateView):
    model = Profile
    fields = ['name', 'image']
    context_object_name = 'profile'
    template_name = 'profiles/profile-edit.html'
    owner = 'user'





def search(request):
    
    if request.method == 'GET':
        search_text = request.GET.get('text')
        print(search_text)
        people = Profile.objects.filter(name__icontains=search_text)
        return render(request, 'profiles/search.html', {'people': people})

@login_required
def friend_request(request):
    user_profile = request.user
    receiver_id = request.POST.get('id')
    receiver = User.objects.get(id=receiver_id)
    r=Relationship.objects.filter(
            sender=user_profile, receiver =  receiver)
    if r:
        r.delete()
    else:
        Relationship.objects.create(
            sender=user_profile,  receiver =  receiver )
    return redirect(request.META.get('HTTP_REFERER'))
    


# def add_comments(request):
#     if request.method == 'POST':
#         body=request.POST.get('cm-txt')
#         id=request.POST.get('cm-form')
#         post=Post.objects.get(id=id)
#         profile=Profile.objects.get(user=request.user)
#         new_comment=Comment.objects.create(body=body, profile= profile, post=post)
#         return redirect(request.META.get('HTTP_REFERER'))

@login_required
def add_remove_friend(request):
    if request.method == 'POST':

        id = request.POST.get('id')
        friend=Profile.objects.get(id=id)
        user_profile=request.user.profile
        if  friend in user_profile.friends.all():
            user_profile.friends.remove(friend)
        else:
            user_profile.friends.add(friend)
    return redirect(request.META.get('HTTP_REFERER'))

@login_required
def accept_reject_request(request):
    profile=Profile.objects.get(user=request.user)
    if request.method == 'GET' and request.GET.get('button') == 'accept':
        id = request.GET.get('id')
        sender=User.objects.get(id=id)
        profile.friends.add(sender.profile)        
    Relationship.objects.get(
           sender=sender,receiver=request.user).delete()
    return redirect(request.META.get('HTTP_REFERER'))

        



