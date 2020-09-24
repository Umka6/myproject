from django.db import models


class Portfolio(models.Model):
    title = models.CharField(max_length=20)
    img = models.ImageField(null=True, blank=True, upload_to='static/portfolio')
    describe = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class Meta:
    verbose_name = 'Портфолио'
    verbose_name_plural = 'Портфолио'


class Applications(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=30)
    mail = models.CharField(verbose_name='Почта', max_length=100)
    subject = models.CharField(verbose_name='Тема', max_length=200)
    comment = models.TextField(verbose_name='Комментарий')

    def __str__(self):
        return self.mail

