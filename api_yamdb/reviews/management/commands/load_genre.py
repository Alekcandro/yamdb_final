from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Genre

DATA_EXISTS_IN_DATA_BASE = """
Данные уже есть/загружены в БД! Если нужно загрузить их снова:
1.Удалите файл db.sqlite3,
2.потом запустите команду 'python manage.py migrate'
Пустая база данных будет создана.
"""


class Command(BaseCommand):
    help = 'Загружает данные из genre.csv'

    def handle(self, *args, **options):

        if Genre.objects.exists():
            print(DATA_EXISTS_IN_DATA_BASE)
            return

        genres = DictReader(open(
            f'{settings.BASE_DIR}/static/data/genre.csv',
            encoding='utf-8'
        ))

        for row in genres:
            genre = Genre(id=row['id'],
                          name=row['name'],
                          slug=row['slug'])
            genre.save()

        print('Данные загружены')
