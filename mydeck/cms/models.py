from django.db import models

# Create your models here.
class Card(models.Model):
    """カード"""
    name = models.CharField('カード名', max_length=255)

    def __str__(self):
        return self.name

class Deck(models.Model):
    """デッキ"""
    name = models.CharField('デッキ名', max_length=255)
    card = models.ForeignKey(Card, verbose_name='カード', related_name='decks', on_delete=models.CASCADE)
    comment = models.TextField('コメント', blank=True)

    def __str__(self):
        return self.name