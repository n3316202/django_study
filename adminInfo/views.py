from django.core import serializers
from django.core.serializers import json, serialize
from django.db import connections
from django.db.models import Max
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import simplejson as json
# Create your views here.
from answer.models import Member, Answer

#n3316202 ##nn6729##
def index(request):
    """
     adminInfo main 출력
    """
    members = Member.objects.all()

    print("멤버총갯수:" + str(Member.objects.count()))
    context = {'members': members}

    return render(request, 'adminInfo/adminInfo_main.html', context)


def getAnswerOne(request, member_id):
    """
    가장최근의 대답을 얻어서 넘김
    """

    # with connections["default"].cursor() as cursor:
    #    cursor.execute("select * from answer_answer WHERE answer_answer.create_date = (SELECT max(answer_answer.create_date) from answer_answer INNER join answer_member on answer_answer.member_id = answer_member.id)")
    #    row = cursor.fetchall()
    #    print(row)

    answer = Answer.objects.filter(member_id=member_id).order_by('-create_date').first()
    print(answer)

    # answer = Answer.objects.filter(member_id=member_id).aggregate(Max('create_date'))
    # print(answer)
    context = {'answer': answer}

    return render(request, 'adminInfo/adminInfo_main.html', context)


def ajax_adminInfoMain(request, member_id):
    """
    가장최근의 대답을 얻어서 넘김
    """
    # 참조사이트
    # https://engineertodeveloper.com/how-to-return-a-json-response-in-django/

    answer = Answer.objects.filter(member_id=member_id).order_by('-create_date').first()
    data = serialize("json", [answer], fields=('member', 'content', 'create_date'))
    return HttpResponse(data, content_type="application/json")


def ajax_adminInfoContent(request, member_id, content_num, page_label):
    """
    컨텐츠 하나씩 넘기기
    """
    # 참조사이트
    # https://engineertodeveloper.com/how-to-return-a-json-response-in-django/

    print("멤버번호:" + str(member_id))
    print("컨테츠 넘버:" + str(content_num))
    print("페이지이전이후:" + str(page_label))

    # answer = Answer.objects.filter(member_id=member_id, id__lt = content_num ).order_by('-create_date').first()

    if page_label == "pre":
        answer = Answer.objects.filter(member_id=member_id, id__lt=content_num).last()
    else:
        answer = Answer.objects.filter(member_id=member_id, id__gt=content_num).first()

    if answer is None:
        print("None 입니다.")
        print(type(answer))
    else:
        data = serialize("json", [answer], fields=('member', 'content', 'create_date'))
        return HttpResponse(data, content_type="application/json")
