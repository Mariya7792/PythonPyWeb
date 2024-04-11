from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        max_articles = Entry.objects.values('author').annotate(max_articles=Count('id')).order_by('max_articles').last()
        max_age = Author.objects.aggregate(max_age=Max('age'))
        author_agreed = Author.objects.filter(status_rule=True).count()
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        self.answer2 = Author.objects.filter(id=max_articles['author'])
        self.answer3 = Entry.objects.filter(Q(tags__name__icontains='Кино') | Q(tags__name__icontains='Музыка')).distinct()
        self.answer4 = Author.objects.filter(gender='ж').count()
        self.answer2 = Entry.objects.values('author_id').aggregate(Count('id'))
        self.answer5 = round((author_agreed / Author.objects.count() * 100),)
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1, 5))
        self.answer7 = Author.objects.filter(age=max_age['max_age'])
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()
        self.answer9 = Author.objects.filter(age__lte=25)
        self.answer10 = Entry.objects.annotate(count_articles=Count('id')).values('author', 'count_articles')


        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1,11)}  # Создайте здесь запросы к БД

        return render(request, 'train_db/training_db.html', context=context)

