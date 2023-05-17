from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Title

DATA_EXISTS_IN_DATA_BASE = """
Данные уже есть/загружены в БД! Если нужно загрузить их снова:
1.Удалите файл db.sqlite3,
2.потом запустите команду 'python manage.py migrate'
Пустая база данных будет создана.
"""


class Command(BaseCommand):
    help = 'Загружает данные из titles.csv'

    def handle(self, *args, **options):

        if Title.objects.exists():
            print(DATA_EXISTS_IN_DATA_BASE)
            return

        titles = DictReader(
            open(
                f'{settings.BASE_DIR}/static/data/titles.csv',
                encoding='utf-8'
            )
        )

        for row in titles:
            title = Title(id=row['id'],
                          name=row['name'],
                          year=row['year'],
                          category_id=row['category'])
            title.save()

        print('Данные загружены!')
