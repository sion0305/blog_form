from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import Blog
from .forms import NewBlog

# Create your views here.
def welcome(request):
    return render(request, 'blog/index.html')

def home(request):
    blogs = Blog.objects.all()
    #블로그 모든 글들을 대상으로
    blog_list = Blog.objects.all()
    #블로그 객체 세 개를 한 페이지로 자르기
    paginator = Paginator(blog_list, 3)
    #request된 페이지가 뭔지를 알아내고 (request페이지를 변수에 담아내고)
    page = request.GET.get('page')
    #request된 페이지를 얻어온 뒤 return 해 준다
    posts = paginator.get_page(page)
    return render(request, 'blog/home.html',{'blogs':blogs, 'posts':posts})

def create(request):
    #새로운 데이터 새로운 블로그 글 저장하는 역할 == POST
    if request.method == "POST":
        #입력된 블로그 글들을 저장해라
        form = NewBlog(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit = False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('home')
    else:
        form = NewBlog()
        return render(request,'blog/new.html', {'form':form})
    

def update(request, pk):
    #어떤 블로그를 수정할지 블로그 객체를 갖고오기
    blog = get_object_or_404(Blog, pk = pk)

    form = NewBlog(request.POST, instance = blog)

    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'blog/new.html', {'form':form})

def delete(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    blog.delete()
    return redirect('home')

def detail(request, pk):
    blog = get_object_or_404(Blog, pk = pk)
    #이용자가 원하는 몇번 객체
    
    return render(request, 'blog/detail.html', {'blog':blog})