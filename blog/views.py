from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.urls import reverse_lazy
from django.views import generic, View
from .models import Post
from .forms import CommentForm
from django.forms import Form
from django.http import HttpResponseRedirect
from django.db.models import Q
from django.contrib import messages
from django.views.generic import CreateView, ListView, DeleteView


# CRUD Functionality
# Creating a Post
class CreatePostView(CreateView):
    """ If user is logged can create a new post """

    model = Post
    template_name = "post_form.html"
    fields = ['title', 'content', 'featured_image', 'excerpt']
    success_url = reverse_lazy('home')
    success_message = ("New post has been created - Waiting for approval")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


def search_articles(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        if not searched:
            return redirect("/")
        post_list = Post.objects.filter(
            Q(content__icontains=searched) |
            Q(title__icontains=searched) |
            Q(author__username__icontains=searched)).filter(status=1)

        return render(
            request, 'index.html',
            {'searched': searched, 'post_list': post_list})
    else:
        return render(request, 'index.html', {})


class PostLike(View):

    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class about(View):
    template_name = "about.html"


class UpdatePost(generic.UpdateView):
    model = Post
    template_name = 'post_update.html'
    success_message = "%(calculated_field)s was edited successfully"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        recipe = self.get_object()
        return recipe.author == self.request.user

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            calculated_field=self.object.title,
        )


class DeletePost(generic.DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_message = "Post deleted successfully"
    success_url = reverse_lazy('post_detail')

    def test_func(self):
        post = self.get_object()
        return post.author == self.request.user

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(DeletePost, self).delete(request, *args, **kwargs)
