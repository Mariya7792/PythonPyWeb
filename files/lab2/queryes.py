import django
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag
    from django.db.models import Count

    # Запрос, аннотирующий количество статей для каждого блога,
    # при этом добавляется новая колонка number_of_entries для вывода
    entry = Entry.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
    print(entry)
    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)













