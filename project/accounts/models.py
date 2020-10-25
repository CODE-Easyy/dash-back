import datetime

from django.contrib.auth.models import BaseUserManager
from django.db import models



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

class Profile(models.Model):
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

    level = models.CharField(
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
            date = ''.join(list(map(now.strftime, _CODE_TEMPLATE)))
            cc =  self.get_last_code(date)
            self.code = f'N{date}{cc}'

        if self.level == 'Администратор':
            self.is_admin = True
            self.is_super_admin = False
        elif self.level == 'Супер Администратор':
            self.is_super_admin = True

        
        self.email = self.email.lower()
        
        super(Profile, self).save(*args, **kwargs)


    def __str__(self):
        return f'Profile("{self.full_name}")'
    

    class Meta:
        ordering = ('code',)
