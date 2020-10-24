import datetime

from django.contrib.auth.models import BaseUserManager
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    _POSITIONS = (
        ('Менеджер', 'Менеджер'),
        ('Backend-Developer', 'Backend-Developer'),
        ('Frontend-Developer', 'Frontend-Developer'),
        ('Fullstack-Developer', 'Fullstack-Developer'),
    )

    _ACCESS_LEVELS = (
        ('Администратор', 'Администратор'),
        ('Супер Администратор', 'Супер Администратор'),
        ('Пользователь', 'Пользователь'),
    )

    _CODE_TEMPLATE = ('%y', '%m', '%d', '%H',)

    code = models.CharField(
        max_length=20,
        unique=True,
        editable=False,

    )

    full_name = models.CharField(
        max_length=255,
    )

    position = models.CharField(
        max_length=255,
        choices=_POSITIONS,
        default='Менеджер',
    )

    phone = models.CharField(
        max_length=20,
        unique=True,
    )


    email = models.EmailField(
        max_length=255,
        unique=True,
    )

    access_level = models.CharField(
        max_length=100,
        choices=_ACCESS_LEVELS,
        default='Пользователь',
    )

    is_admin = models.BooleanField(
        default=False,
    )
    is_super_admin = models.BooleanField(
        default=False,
    )
    is_active = models.BooleanField(
        default=True,
    )
    def check_phone(phone) -> bool:
        test = Profile.objects.filter(phone=phone)
        if test.count() != 0:
            return False
        return True

    def check_email(email) -> bool:
        test = Profile.objects.filter(email=email.lower())
        if test.count() != 0:
            return False
        return True

    def create_profile(data:dict):
        profile = Profile(
            full_name=data['full_name'],
            position=data['position'],
            phone=data['phone'],
            email=data['email'],
            access_level=data['level'],
        )
        profile.save()

        return profile

    

    def get_last_code(self, date:str) -> str:
        same = Profile.objects.filter(code__contains=date).order_by('code')
        if same.count() == 0:
            return '000'
        else:
            last = same.last()
            return '{:03d}'.format(int(last.code[-3:]) + 1)


    def save(self, *args, **kwargs):
        if not self.code:
            now = datetime.datetime.now()
            date = ''.join(list(map(now.strftime, self._CODE_TEMPLATE)))
            cc =  self.get_last_code(date)
            self.code = f'N{date}{cc}'

        if self.access_level == 'Администратор':
            self.is_admin = True
        elif self.access_level == 'Супер Администратор':
            self.is_super_admin = True
        
        self.email = self.email.lower()
        
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return f'Profile("{self.full_name}")'
    

    class Meta:
        ordering = ('code',)
