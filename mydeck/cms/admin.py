from django.contrib import admin
from cms.models import Card, Deck

# Register your models here.

class CardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',) #一覧に出したい名前
    list_display_links = ('id', 'name',) #修正リンクでクリックできる項目

admin.site.register(Card, CardAdmin)

class DeckAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',) #一覧に出したい名前
    list_display_links = ('id', 'comment',) #修正リンクでクリックできる項目
    raw_id_fields = ('card',) #外部キーをプルダウンにしない（データ件数が増加時のタイムアウトを予防）

admin.site.register(Deck, DeckAdmin)