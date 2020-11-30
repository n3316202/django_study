from django.shortcuts import render, redirect

# Create your views here.
from django.utils import timezone

from answer.models import Member


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

            member = Member(name=request.POST['name'], create_date=timezone.now())
            member.save()

        # 로그인 한다
        # auth.login(request, user)
        # return redirect('/')

    # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
    # return render(request, 'signup.html')
    return redirect('/')
