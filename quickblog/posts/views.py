#from django.shortcuts import render
# Create your views here.
from django.views.generic import (ListView ,CreateView, UpdateView, DeleteView, DetailView)
from posts.models import Post
from django.core.urlresolvers import reverse
from posts.forms import UserForm, UserProfileForm

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.comments.forms import CommentForm


class ListPostView(ListView):

    model = Post
    template_name = 'posts_list.html'

class CreatePostView(CreateView):

    model = Post
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse('posts-list')

    def get_context_data(self, **kwargs):
        context = super(CreatePostView, self).get_context_data(**kwargs)
        context['action'] = reverse('post-new')
        return context


class UpdatePostView(UpdateView):

    model = Post
    template_name = 'edit_post.html'

    def get_success_url(self):
        return reverse('posts-list')

    def get_context_data(self, **kwargs):
        context = super(UpdatePostView, self).get_context_data(**kwargs)
        context['action'] = reverse('post-edit',kwargs={'pk': self.get_object().id})
        return context

class DeletePostView(DeleteView):

    model = Post
    template_name = 'delete_post.html'

    def get_success_url(self):
        return reverse('posts-list')

class PostDetailView(DetailView):
    model = Post
    template_name = 'post.html'

def index(request):
    return render_to_response('posts_list.html')

def managepostlist(request):
    return render_to_response('managepostlist.html')

def upvote(request, post_id):
    s = get_object_or_404(Post, pk=post_id)
    s.upvotes += 1
    s.save()
    return render_to_response("post.html")


# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/list/')

##function based view to handle login and registration
def register(request):
    context = RequestContext(request)
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            profile.save()
            registered = True

        else:
            pass
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render_to_response(
            'register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered},
            context)

def user_login(request):

    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:

                login(request, user)
                return HttpResponseRedirect('/managepostlist')

            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your quickblog account is disabled.")
        else:
            return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html', {}, context)
