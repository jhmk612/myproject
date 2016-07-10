from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Candidate, Poll, Choice
import datetime
from django.db.models import Sum
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import LoginForm, JoinForm
from django.core.context_processors import csrf
# Create your views here.

def home(request):
    return render(request, 'elections/home.html')

def index(request):
    candidates = Candidate.objects.all()
    context = {'candidates': candidates}

    return render(request, 'elections/index.html', context)

"""def vote(request):
    polls= Poll.objects.all()
    context = {'polls': polls}
    return render(request, 'elections/vote.html', context)"""

def vote(request):
    today= datetime.datetime.now()
    poll = Poll.objects.get(start_date__lte=today, end_date__gte=today)
    candidates = Candidate.objects.all()
    context = {'candidates': candidates, 'poll': poll}
    return render(request, 'elections/vote.html', context)

def polls(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    selection = request.POST['choice']

    try:
        choice=Choice.objects.get(poll_id=poll_id, candidate_id = selection)
        choice.votes +=1
        choice.save()
    except:
        choice=Choice(poll_id=poll_id, candidate_id = selection, votes=1)

        choice.save()

    return HttpResponseRedirect("./results".format(poll_id))

def results(request):
    candidates= Candidate.objects.all()
    polls = Poll.objects.all()
    poll_results=[]
    for poll in polls:
        result={}
        result['start_date']=poll.start_date
        result['end_date']=poll.end_date
        total_votes=Choice.objects.filter(poll_id=poll.id).aggregate(Sum('votes'))
        result['total_votes']=total_votes['votes__sum']
        rates=[]
        for candidate in candidates:
            try:
                choice=Choice.objects.get(poll_id=poll.id, candidate_id=candidate.id)
                rates.append(round(choice.votes*100/result['total_votes'],1))
            except:
                rates.append(0)
        result['rates']=rates
        poll_results.append(result)
    context={'candidates': candidates, 'poll_results': poll_results}
    return render(request, 'elections/result.html', context)

def signup(request):
    if request.method =='POST':
        form_data = JoinForm(request.POST)

        if form_data.is_valid():
            username = form_data.cleaned_data['id']
            password = form_data.cleaned_data['password']
            User.objects.create_user(username=username, password=password)

            return HttpResponseRedirect('/login')
    else:
        form_data=JoinForm()

    context={'join_form':JoinForm()}
    context.update(csrf(request))

    return render(request, 'elections/signup.html', context)

def login(request):




    return render(request,'elections/login.html')

def login_validate(request):
    login_form_data=LoginForm(request.POST)
    if login_form_data.is_valid():
        user= authenticate(username=login_form_data.cleaned_data['id'], password=login_form_data.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/home')
        else:
            return HttpResponse('사용자가 없거나 비밀번호를 잘못 누르셨습니다.')
    else:
        return HttpResponse('로그인 폼이 비정상적입니다.')

def after_login(request):
    user=User()
    if request.user.is_authenticated():

        return render(request,'elections/after.html')
    else:
        return render(request, 'elections/home.html')