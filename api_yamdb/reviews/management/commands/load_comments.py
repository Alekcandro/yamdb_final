from csv import DictReader

from django.conf import settings
from django.core.management import BaseCommand

from reviews.models import Comment

DATA_EXISTS_IN_DATA_BASE = """
Данные уже есть/загружены в БД! Если нужно загрузить их снова:
1.Удалите файл db.sqlite3,
2.потом запустите команду 'python manage.py migrate'
Пустая база данных будет создана.
"""


class Command(BaseCommand):
    help = 'Загружает данные из comments.csv'

    def handle(self, *args, **options):

        if Comment.objects.exists():
            print(DATA_EXISTS_IN_DATA_BASE)
            return

        comments = DictReader(open(
            f'{settings.BASE_DIR}/static/data/comments.csv',
            encoding='utf-8'
        ))

        for row in comments:
            comment = Comment(
                id=row['id'],
                review_id=row['review_id'],
                text=row['text'],
                author_id=row['author'],
                pub_date=row['pub_date']
            )
            comment.save()

        print('Данные загружены!')
