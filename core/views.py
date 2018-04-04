from django.shortcuts import render
from .models import Post
from django.http import Http404
from .models import Question
from django.utils import timezone
from django.http import HttpResponse

def index(request):
    return render(request, 'core/index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'core/post_list.html', {'posts': posts})

def question_list(request):
    questions = Question.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'core/question_list.html', {'questions': questions})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'core/question_detail.html', {'question': question})
