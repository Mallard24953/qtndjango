from django.db import models


class Paper(models.Model):
    name = models.CharField('Название', max_length=50, default='Бумага')
    density = models.PositiveSmallIntegerField('Грамматура', default=130)
    cost = models.PositiveSmallIntegerField('Цена', default=100)

    def __str__(self):
        return "Название: {}, Цена: {}".format(self.name, self.cost)

    class Meta():
        verbose_name = 'Бумагу'
        verbose_name_plural = 'Бумага'


class ContactForm(models.Model):
    name = models.CharField('Имя', max_length=50, default='Имя')

    def __str__(self):
        return "Имя: {}".format(self.name)
