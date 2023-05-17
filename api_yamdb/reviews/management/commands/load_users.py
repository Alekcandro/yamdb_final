from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from users.models import User

DATA_EXISTS_IN_DATA_BASE = """
Данные уже есть/загружены в БД! Если нужно загрузить их снова:
1.Удалите файл db.sqlite3,
2.потом запустите команду 'python manage.py migrate'
Пустая база данных будет создана.
"""


class Command(BaseCommand):
    help = 'Загружает данные из users.csv'

    def handle(self, *args, **options):

        if User.objects.exists():
            print(DATA_EXISTS_IN_DATA_BASE)
            return

        users = DictReader(open(
            f'{settings.BASE_DIR}/static/data/users.csv',
            encoding='utf-8'
        ))

        for row in users:
            user = User(id=row['id'],
                        username=row['username'],
                        email=row['email'],
                        role=row['role'],
                        bio=row['bio'],
                        first_name=row['first_name'],
                        last_name=row['last_name'])
            user.save()

        print('Данные загружены')
