from django.shortcuts import render
from django.utils import timezone
from .models import Post

# 쿼리셋
def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'blog/post_list.html', {'posts': posts})