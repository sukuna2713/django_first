from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def card_list(request):
    """カードの一覧"""
    return HttpResponse('カードの一覧')


def card_edit(request, card_id = None):
    """カードの編集"""
    return HttpResponse('カードの編集')


def card_del(request, card_id):
    """カードの削除"""
    return HttpResponse('カードの削除')