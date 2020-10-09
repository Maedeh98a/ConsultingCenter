from django.db import models
from account.models import Consultant, University


class UniversityComment(models.Model):
    University = models.ForeignKey(University, on_delete=models.CASCADE,
                                   null=True, blank=True, verbose_name='نام دانشگاه ')
    name = models.CharField(max_length=40, null=True, verbose_name='نام ')
    email = models.EmailField(null=True, blank=True, verbose_name='پست الکترونیکی')
    body = models.TextField(null=True, verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ تغییر')
    active = models.BooleanField(null=True, verbose_name='فعال')

    class Meta:
        db_table = 'university_comment'
        verbose_name = 'دیدگاه برای دانشگاه'
        verbose_name_plural = 'دیدگاه برای دانشگاه ها'

    def __str__(self):
        return f' دیدگاه {self.name} درباره {self.University}'


class ConsultantComment(models.Model):
    consultant = models.ForeignKey(Consultant, on_delete=models.CASCADE,
                                   null=True, blank=True, related_name='comments', verbose_name='نام مشاور ')
    name = models.CharField(max_length=40, null=True, verbose_name='نام ')
    email = models.EmailField(null=True, blank=True, verbose_name='پست الکترونیکی')
    body = models.TextField(null=True, verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ تغییر')
    active = models.BooleanField(null=True, verbose_name='فعال')

    class Meta:
        db_table = 'consultant_comment'
        verbose_name = 'دیدگاه برای مشاور'
        verbose_name_plural = 'دیدگاه برای مشاوران'

    def __str__(self):
        return f' دیدگاه {self.name} درباره {self.consultant}'


class AllComment(models.Model):
    name = models.CharField(max_length=40, null=True, verbose_name='نام ')
    email = models.EmailField(null=True, blank=True, verbose_name='پست الکترونیکی')
    body = models.TextField(null=True, verbose_name='متن')
    created = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ ایجاد')
    updated = models.DateTimeField(auto_now_add=True, null=True, verbose_name='تاریخ تغییر')
    active = models.BooleanField(null=True, verbose_name='فعال')

    class Meta:
        db_table = 'all_comment'
        verbose_name = 'دیدگاه '
        verbose_name_plural = ' همه دیدگاه ها'

    def __str__(self):
        return f' دیدگاه{self.name}'
