from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import GenreTitle

DATA_EXISTS_IN_DATA_BASE = """
Данные уже есть/загружены в БД! Если нужно загрузить их снова:
1.Удалите файл db.sqlite3,
2.потом запустите команду 'python manage.py migrate'
Пустая база данных будет создана.
"""


class Command(BaseCommand):
    help = 'Загружает данные из title_genre.csv'

    def handle(self, *args, **options):

        if GenreTitle.objects.exists():
            print(DATA_EXISTS_IN_DATA_BASE)
            return

        title_genres = DictReader(
            open(
                f'{settings.BASE_DIR}/static/data/genre_title.csv',
                encoding='utf-8'
            )
        )

        for row in title_genres:
            title_genre = GenreTitle(id=row['id'],
                                     title_id=row['title_id'],
                                     genre_id=row['genre_id'])
            title_genre.save()

        print('Данные загружены')
