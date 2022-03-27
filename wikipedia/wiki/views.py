from django.shortcuts import render, redirect
from .models import forum_post, Comments
from .forms import CommentForm, PostSearchForm
from django.views.generic import (CreateView,
                                  ListView,
                                  DetailView,
                                  View,
                                  DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.views import Profile
from django.contrib.auth.decorators import login_required
from django.contrib import messages


class PostCreateView(LoginRequiredMixin, CreateView):
    model = forum_post
    fields = ['title',
              'semestr',
              'category',
              'text']
    template_name = 'wikipedia/post_create.html'
    success_url = '/forum'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# TODO
# Wyszukiwanie
class ForumView(ListView):
    model = forum_post
    extra_context = {'form': PostSearchForm()}
    context_object_name = 'posts'
    template_name = 'wikipedia/forum.html'
    ordering = ['-creation_date']

    def post(self, request, **kwargs):
        form = PostSearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_word_text']
        return redirect(f'/forum/search/{search_text}')
        pass


# Temp search
class SearchView(View):
    def get(self, request):
        context = {'form': PostSearchForm(),
                   'title': 'Czemu to kurwa nie działa!!!'}
        return render(request, 'wikipedia/forum_search.html', context)

    def post(self, request):
        form = PostSearchForm(request.POST)
        if form.is_valid():
            search_text = form.cleaned_data['search_word_text']
        return redirect(f'/forum/search/{search_text}')


class SearchViewResult(View):
    def get(self, request, **kwargs):
        search_keyword = kwargs['str']
        search_results = forum_post.objects.filter(text__search=search_keyword)
        context = {'search_text': search_keyword,
                   'title': f'Search: {kwargs["str"]}',
                   'posts': search_results}
        return render(request, 'wikipedia/forum_search_result.html', context)


class PostView(DetailView):
    model = forum_post
    context_object_name = 'post'
    template_name = 'wikipedia/post.html'


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = forum_post
    template_name = 'wikipedia/post_delete.html'
    success_url = '/forum'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


class PostViewPk(LoginRequiredMixin, View):
    model = forum_post

    # @login_required(login_url='login')
    def get(self, request, pk):
        if forum_post.objects.filter(id=pk).exists():
            if Comments.objects.filter(post_reference_id=pk).exists():
                context = {
                    'post': forum_post.objects.get(id=pk),
                    'title': f'{forum_post.objects.get(id=pk).title}',
                    'comments': Comments.objects.filter(post_reference_id=pk),
                    'form': CommentForm(),
                }
            else:
                context = {
                    'post': forum_post.objects.get(id=pk),
                    'title': f'{forum_post.objects.get(id=pk).title}',
                    'form': CommentForm(),
                }
            return render(request, 'wikipedia/post.html', context)
        # return render(request,wiki)

    def post(self, request, pk):
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.author = request.user
            form.instance.post_reference = forum_post.objects.get(id=pk)
            form.save()
            message = messages.success(request, "Post commented")
            return redirect(f'/forum/{pk}')
        else:
            return redirect(f'/forum/{pk}')


class UserComments(LoginRequiredMixin, View):
    def get(self, request):
        if Comments.objects.filter(author_id=request.user.id).exists():
            a = Comments.objects.filter(author_id=request.user.id)
            # TODO
            # Tu jest do pizdy bo niewiem czzemu w html nie moge odniesc sie do elementu typu parent

            context = {
                'comments': Comments.objects.filter(author_id=request.user.id),
                'posts': forum_post.objects.all(),
                'title': f'{request.user.username} comments',
            }
            return render(request, 'wikipedia/user_comments.html', context)
        else:
            context = {
                'title': f'{request.user.username} comments',
            }
            return render(request, 'wikipedia/user_comments.html', context)


class UserCommentPrototype(LoginRequiredMixin, ListView):
    model = Comments
    context_object_name = None
    template_name = 'wikipedia/user_comments.html'
    ordering = ['-comment_date']


def home(request):
    # do usuniecia warunek po reprodukcji profili!!!!
    if Profile.objects.filter(user_id=request.user.id).exists():
        prof = Profile.objects.get(user_id=request.user.id)
        return render(request, 'wikipedia/home.html', {'profile': prof})
    else:
        return render(request, 'wikipedia/home.html')


def forum(request):
    context = {'posts': forum_post.objects.all(),
               'title': 'Elektro | Forum'}
    return render(request, 'wikipedia/forum.html', context)


@login_required(login_url='login')
def user_posts(request):
    if forum_post.objects.filter(author=request.user).exists():
        posts = forum_post.objects.filter(author=request.user)
        context = {
            'posts': posts,
            'title': f'{request.user.username} posts',
        }
        return render(request, 'wikipedia/user_post.html', context)
    else:
        return render(request, 'wikipedia/user_post.html', {'posts': False, 'title': f'{request.user.username} posts'})
