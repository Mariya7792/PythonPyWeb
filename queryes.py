import django
import os
import datetime
from django.db.models import Count
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

if __name__ == "__main__":
    from apps.db_train_alternative.models import Blog, Author, AuthorProfile, Entry, Tag

    # TODO Сделайте здесь запросы

    # obj = Entry.objects.filter(author__name__contains='author')
    # print(obj)
    #
    # obj = Entry.objects.filter(author__authorprofile__city=None)
    # print(obj)
    # print(Entry.objects.get(id__exact=4))
    # print(Entry.objects.get(id=4))
    # print(Blog.objects.get(name__iexact="Путешествия по миру"))
    # print(Entry.objects.filter(headline__contains='мод'))
    # print(Entry.objects.filter(id__in=[1,3,4]))
    # print(Entry.objects.filter(number_of_comments__in='123'))
    # inner_gs = Blog.objects.filter(name__contains='Путешествия')
    # print(inner_gs)
    # entries = Entry.objects.filter(blog__in=inner_gs)
    # print(entries)
    # print(Entry.objects.filter(number_of_comments__gt=10))
    # #print(Entry.objects.filter(pub_date__gte=datetime.date(2023, 6, 1)))
    # print(Entry.objects.filter(number_of_comments__gt=10).filter(rating__lt=4))
    # print(Entry.objects.filter(headline__lte="Зя"))
    # print(Entry.objects.filter(headline__startswith="Как"))
    # print(Entry.objects.filter(headline__endswith='ния'))
    # print(Entry.objects.filter(pub_date__year=2023))
    # print(Entry.objects.filter(pub_date__year__lt=2022))
    # print(Entry.objects.filter(pub_date__month=2).values('blog__name', 'pub_date', 'headline'))
    # print(Entry.objects.filter(pub_date__year=2023).filter(pub_date__day__gte=1).filter(pub_date__day__lte=15).values_list("author__name").distinct())
    # print(Entry.objects.filter(pub_date__week_day=2).values('blog__name', 'pub_date', 'headline'))
    # print(AuthorProfile.objects.filter(city__isnull=True))
    # print(Entry.objects.filter(body_text__regex=r'\w*стран\w*'))
    # print(Entry.objects.filter(author__email__iregex=r'\w+(@gmail.com|@mail.ru)').distinct())

    all_obj = Blog.objects.all()
    #print('Вывод всех значений в таблице Blog\n', all_obj)
    # print(Blog.objects.first())
    # for idx, value in enumerate(all_obj):
    #     print(f"idx = {idx}, value = {value}")
    # print(all_obj[0])
    # print(all_obj[2:4])
    # print(Blog.objects.latest('id'))
    # print(Blog.objects.get(id=1))
    # print(Blog.objects.filter(id__gte=2))
    # print(Blog.objects.exclude(id__gte=2))
    # print(Blog.objects.filter(id=2, name='Путешествия по миру').exists())
    # print(Blog.objects.count())
    # print(Blog.objects.filter(id__gte=2).order_by('-id'))
    entry = Blog.objects.annotate(number_of_entries=Count('entries')).values('name', 'number_of_entries')
    print(entry)
    blogs = Blog.objects.alias(number_of_entries=Count('entries')).filter(number_of_entries__gt=4)
    print(blogs)
    print(Blog.objects.get(id=3))



