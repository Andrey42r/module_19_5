from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

# Create your views here.

paginate_by = 1

def index(request):
    global paginate_by
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    paginate_by = request.GET.get('paginate_by') or paginate_by
    page_number = request.GET.get('page') or 1
    page_posts = paginator.get_page(page_number)
    return render(request, 'index.html', {'page_posts': page_posts})



