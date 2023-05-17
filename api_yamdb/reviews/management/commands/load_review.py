from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Review

DATA_EXISTS_IN_DATA_BASE = """
Данные уже есть/загружены в БД! Если нужно загрузить их снова:
1.Удалите файл db.sqlite3,
2.потом запустите команду 'python manage.py migrate'
Пустая база данных будет создана.
"""


class Command(BaseCommand):
    help = 'Загружает данные из review.csv'

    def handle(self, *args, **options):

        if Review.objects.exists():
            print(DATA_EXISTS_IN_DATA_BASE)
            return

        reviews = DictReader(open(
            f'{settings.BASE_DIR}/static/data/review.csv',
            encoding='utf-8'
        ))

        for row in reviews:
            review = Review(id=row['id'],
                            title_id=row['title_id'],
                            text=row['text'],
                            author_id=row['author'],
                            score=row['score'],
                            pub_date=row['pub_date'])
            review.save()

        print('Данные загружены')
