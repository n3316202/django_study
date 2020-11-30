from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from answer.models import Member, Answer, Choice


def index(request):
    """
     answer main 출력
    """
    return redirect('/')


def answer_code(request):
    """
     answer main 출력
    """
    # IP 얻어 오기
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    #print(ip)
    #member_create(ip)

    user_id = request.session.get('id')
    code = request.POST['code']
    answer_create(user_id, code)

    print(code)
    return render(request, 'answer/sample_ace.html')


def answer_choice(request):
    """
     answer main 출력
    """
    # IP 얻어 오기
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    #print(ip)
    #member_create(ip)

    user_id = request.session.get('id')

    choice = request.POST['choice']
    choice_create(user_id, choice)

    print(choice)
    return render(request, 'answer/sample_ace.html')


def member_create(ip):
    """
    멤버 생성
    """
    try:
        member = Member.objects.get(ip=ip)
    except Member.DoesNotExist:
        print("해당 IP가 존재 하지 않습니다.:" + ip)
        member = Member(name="", ip=ip, create_date=timezone.now())
        member.save()


def answer_create(user_id, code):
    """
    답변 생성
    """
    member = get_object_or_404(Member, name=user_id)
    answer = Answer(member=member, content=code, create_date=timezone.now())
    answer.save()


def choice_create(user_id, content):
    """
    객관식 답변 생성
    """
    member = get_object_or_404(Member, name=user_id)
    print("멤버이름:" + member.name)

    choice = Choice.objects.filter(member_id=member.id)

    print("초이스 갯수" + str(choice.count()))

    if choice.count() == 0:
        print("초이스 갯수" + str(choice.count()))
        choice = Choice(member=member, content=content, create_date=timezone.now())
        choice.save()
    else:
        print("초이스 삭제후 입력")
        choice.delete()
        choice = Choice(member=member, content=content, create_date=timezone.now())
        choice.save()
