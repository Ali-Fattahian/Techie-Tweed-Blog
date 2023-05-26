from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post

def paginate_posts(request, posts, results):
    page = request.GET.get('page')
    paginator = Paginator(posts, results)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        posts = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        posts = paginator.page(page)

    leftindex = (int(page) - 2)
    if leftindex < 1:
        leftindex = 1

    rightindex = (int(page) + 3)
    if rightindex > paginator.num_pages:
        rightindex = paginator.num_pages + 1

    custom_range = range(leftindex, rightindex)

    return custom_range, posts, paginator


def search_posts(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    posts = Post.objects.filter(Q(title__icontains = search_query) | Q(excerpt__icontains = search_query)).order_by('-date')

    return search_query, posts
