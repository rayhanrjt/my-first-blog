from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.shortcuts import redirect
from .forms import studentForm
from django.shortcuts import get_object_or_404


from .models import Post
from .models import Classs
from .models import student
@login_required
def index(request):
    return render(request, 'blog/index.html', {})

def studentlist(request):
    studentlists = student.objects.all();
    return render(request, 'blog/studentlist.html', {'studentlists': studentlists})
    
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_new(request):
    if request.method == "POST":
        form = studentForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('blog/index.html', pk=post.pk)
    else:
        form = studentForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def student_detail(request, pk):
    post = get_object_or_404(student, pk=pk)
    return render(request, 'blog/student_detail.html', {'post': post})

def contact(request):
    return render(request,'blog/contact.html')
def scholarship(request):
    return render(request,'blog/scholarship.html')
def course(request):
    return render(request,'blog/course.html')
def gallery(request):
    return render(request,'blog/gallery.html')
def blog(request):
    return render(request,'blog/blog.html')
# Create your views here.
