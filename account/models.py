from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse


class User(AbstractUser):
    is_student = models.BooleanField(default=False, verbose_name='دانش آموز')
    is_consultant = models.BooleanField(default=False, verbose_name='مشاور')
    show_fullname = models.BooleanField(default=True, null=True, verbose_name=' نمایش نام')
    phone = models.CharField(unique=True, max_length=11, null=True, verbose_name='تلفن همراه')
    photo = models.ImageField(upload_to='static/img', null=True, blank=True, verbose_name='عکس')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class University(models.Model):
    university_name = models.CharField(max_length=150, verbose_name="نام دانشگاه ", blank=True)
    university_city = models.CharField(max_length=100, verbose_name="شهر دانشگاه ", blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True, verbose_name='لینک یکتا')
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=12, blank=True)
    website = models.URLField(null=True, verbose_name='آدرس وب سایت')
    about_university = models.TextField(blank=True)
    photo = models.ImageField(null=True, blank=True, upload_to='static/img/', verbose_name='تصویر')

    class Meta:
        db_table = "university"
        verbose_name = 'دانشگاه'
        verbose_name_plural = 'دانشگاه ها'

    def __str__(self):
        return self.university_name

    def get_absolute_url(self):
        return reverse("bodies:university-detail", kwargs={'slug': self.slug})


class Major(models.Model):
    major_name = models.CharField(max_length=100, verbose_name="نام رشته ", blank=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True, verbose_name='لینک یکتا')
    photo = models.ImageField(null=True, blank=True, upload_to='static/img/major', verbose_name='تصویر')
    description = models.TextField(null=True, blank=True, verbose_name='توضیحات')
    university_major = models.ManyToManyField(University, blank=True, verbose_name='دانشگاه های شامل این رشته')

    class Meta:
        db_table = "major"
        verbose_name = 'رشته'
        verbose_name_plural = 'رشته ها'

    # def get_absolute_url(self):
    #     return reverse('profiles: university_name', kwargs={'slug', self.slug})

    def __str__(self):
        return self.major_name


class Consultant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    slug = models.SlugField(allow_unicode=True, unique=True, null=True, blank=True, verbose_name='لینک یکتا')
    bachelor_major = models.ManyToManyField(Major, blank=True, verbose_name='رشته کارشناسی')
    universities = models.ManyToManyField(University, blank=True, verbose_name='دانشگاه محل تحصیل کارشناسی')
    identity_code = models.CharField(unique=True, max_length=10, blank=True, null=True, verbose_name='کد ملی')
    rate_exam = models.CharField(max_length=40, blank=True, null=True, verbose_name='رتبه کنکور')
    show_rate = models.BooleanField(default=False, null=True, verbose_name=' نمایش رتبه کنکور')
    interest_major = models.CharField(max_length=60, null=True, blank=True, verbose_name='رشته های مورد علاقه')
    bachelor_average = models.FloatField(blank=True, null=True, verbose_name='معدل کارشناسی')
    master_tendency = models.CharField(max_length=50, verbose_name='گرایش ارشد', blank=True, null=True)
    phd_tendency = models.CharField(max_length=50, verbose_name='گرایش دکتری ', blank=True, null=True)
    description = models.TextField(default=None, null=True, blank=True, verbose_name='توضیحات')
    CONSULTING_TYPE = (
        ('CHAT', 'تماس متنی'),
        ('VOICE CALL', 'تماس صوتی'),
        ('VIDEO CALL', 'تماس تصویری'),
        ('ALL', 'هر نوع تماس'),
        ('CHAT_VOICE', 'متنی و صوتی'),
        ('CHAT_VIDEO', 'متنی و ویدیویی'),
        ('VOICE_VIDEO', 'صوتی و ویدیویی')
    )
    consulting_type = models.CharField(max_length=15, choices=CONSULTING_TYPE,
                                       blank=True, verbose_name="نوع مشاوره ")

    class Meta:
        db_table = "consultant"
        verbose_name = 'مشاور'
        verbose_name_plural = 'مشاوران'

    def __str__(self):
        return str(self.user)

    def get_absolute_url(self):
        return reverse("bodies:consultant-detail", kwargs={'slug': self.slug})


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                primary_key=True, verbose_name="نام دانش آموز ", blank=True)
    description = models.TextField(blank=True, null=True, verbose_name='درباره من ')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "student"
        verbose_name = 'دانش آموز'
        verbose_name_plural = 'دانش آموزان'

    def __str__(self):
        return str(self.user)

    # def get_edit_url(self):
    #     return reverse("account:update-student", kwargs={'pk': self.pk})

