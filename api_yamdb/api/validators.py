import re

from django.core.exceptions import ValidationError

USERNAME = re.compile(r'^[\w.@+-]+')


def validate_username(name):
    if name == 'me':
        raise ValidationError('Имя пользователя "me" зарезервировано!')
    if not USERNAME.fullmatch(name):
        raise ValidationError('Можно использовать только буквы, цифры')
