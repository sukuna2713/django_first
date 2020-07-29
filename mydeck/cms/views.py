from django.shortcuts import render
from django.http import HttpResponse

from cms.models import Card

# Create your views here.
def card_list(request):
    """カードの一覧"""
    #return HttpResponse('カードの一覧')
    cards = Card.objects.all().order_by('id')
    return reader(request,'cms/card_list.html',{'cards': cards})


def card_edit(request, card_id = None):
    """カードの編集"""
    return HttpResponse('カードの編集')


def card_del(request, card_id):
    """カードの削除"""
    return HttpResponse('カードの削除')