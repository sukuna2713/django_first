from django.urls import path
from cms import views


app_name = 'cms'
urlpatterns = [
    #カード
    path('card/', views.card_list, name='card_list'), #一覧
    path('card/add', views.card_edit, name='card_add'), #登録
    path('card/mod/<int:card_id>/', views.card_edit, name='card_mod'), #修正
    path('card/del/<int:card_id>/', views.card_del, name='card_del'), #削除
]