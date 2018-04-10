from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from smfreal.forms import UserForm, UserProfileInfoForm,PostForm, CommentForm,myuserdb_form
from smfreal.models import fundlist, Post,Comment,Myuserdb
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

class AboutView(TemplateView):
    template_name = 'smfreal/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

class PostDetailView(DetailView):
    model = Post


class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'smfreal/post_detail.html'

    form_class = PostForm

    model = Post


class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'smfreal/post_detail.html'

    form_class = PostForm

    model = Post


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'smfreal/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

#######################################
## Functions that require a pk match ##
#######################################

@login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'smfreal/comment_form.html', {'form': form})


@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)


@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail', pk=post_pk)


def listf(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/list.html',context=fundd)


def recoma(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/recommendation.html',context=fundd)


def index(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/index.html',context=fundd)


def user_page(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/fundlist.html',context=fundd)



def navbarfunction(request):
    return render(request,'smfreal/navigation.html')

def register(request):
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfo

        if user_form.is_valid() and profile_form.is_valid():
            user = user-user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=false)
            profile.user = user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()
            registered = True

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()


    return render(request,'smfreal/register.html',{'user_form':user_form,'profile_form':profile_form,'registered':registered})


def equity(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/equity.html',context=fundd)

def debt(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/debt.html',context=fundd)

def hybrid(request):
    funddetail = fundlist.objects.order_by('fundno')
    fundd = {'fundl': funddetail }
    return render(request,'smfreal/hybrid.html',context=fundd)


def buy(request,pk='default'):
    funddetail = fundlist.objects.order_by('pk')
    fundd = {'fundl':funddetail}
    return render(request,'smfreal/buy.html',context=fundd)
