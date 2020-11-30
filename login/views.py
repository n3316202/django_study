from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from answer.models import Member, LoginTime


def index(request):
    """
     adminInfo main 출력
    """
    return render(request, 'login/member_signup.html')


# 회원 가입
def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
    if request.method == 'POST':
        try:
            member = Member.objects.get(name=request.POST['name'])
        except Member.DoesNotExist:
            print("해당 이름이 존재하지 않습니다:" + request.POST['name'])

            member = Member(name=request.POST['name'], create_date=timezone.now(),login_date=timezone.now())
            member.save()

        # 로그인 한다
        # auth.login(request, user)
        # return redirect('/')

    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    # return render(request, 'signup.html')
    return redirect('/')


# 회원 로그인
def login(request):
    context = True
    if request.method == 'POST':
        try:
            member = Member.objects.get(name=request.POST['name'])
            request.session['id'] = request.POST['name']

            member.login_date = timezone.now()
            member.save()

            login_time = LoginTime(member=member, login_date=timezone.now())
            login_time.save()

            context = {'member': member}
        except Member.DoesNotExist:
            print("해당 이름이 존재하지 않습니다:" + request.POST['name'])
            return redirect('/')
    else:
        return redirect('/')

    return render(request, 'answer/answer_main.html', context)

