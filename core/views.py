from django.shortcuts import render, get_object_or_404
from .models import Post
from .models import Question
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm
from django.db.models import Q


def index(request):
    return render(request, 'core/index.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'core/post_list.html', {'posts': posts})

def question_list(request):
    if not request.user.is_authenticated:
        return render(request, 'core/login.html')
    else:
        question_results = Question.objects.all()
        questions = Question.objects.all()
        query = request.GET.get("q")
        if query:
            question_results = question_results.filter(
                Q(topic__icontains=query) |
                Q(difficulty__icontains=query) |
                Q(year__icontains=query) |
                Q(grade__icontains=query)
            ).distinct()
            return render(request, 'core/question_list.html', {
                'questions': questions,
                'question_results': question_results,
            })
        else:
            return render(request, 'core/question_list.html', {'questions': questions})
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'core/question_detail.html', {'question': question})



class UserFormView(View):
    form_class = UserForm
    template_name = 'core/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'core/homepage_logged_in.html', {})
        return render(request, 'core/registration_form.html', {'form': form, 'error_message': 'your username or email may already be registered. please choose another one'})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'core/login.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                questions = Question.objects.all()
                return render(request, 'core/homepage_logged_in.html', {'questions': questions})
            else:
                return render(request, 'core/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'core/login.html', {'error_message': 'Invalid login'})
    return render(request, 'core/login.html')

def homepage(request):
    return render(request, 'core/homepage_logged_in.html', {})
def questions(request, filter_by):
    if not request.user.is_authenticated():
        return render(request, 'core/login.html')
    else:
        try:
            question_ids = []
            for question in Question.objects.filter(user=request.user):
                question_ids.append(question.pk)
            users_questions = Question.objects.filter(pk__in=question_ids)
        except Question.DoesNotExist:
            users_questions = []
        return render(request, 'core/questions.html', {
            'question_list': users_songs,
            'filter_by': filter_by,
        })
