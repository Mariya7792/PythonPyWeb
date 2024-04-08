from django.shortcuts import render
from django.views import View
from .models import Author, AuthorProfile, Entry, Tag
from django.db.models import Q, Max, Min, Avg, Count


class TrainView(View):
    def get(self, request):
        max_self_esteem = Author.objects.aggregate(max_self_esteem=Max('self_esteem'))
        # max_articles = Author.objects.aggregate(max_articles=Max(''))
        max_age = Author.objects.aggregate(mx=Max('age'))
        self.answer1 = Author.objects.filter(self_esteem=max_self_esteem['max_self_esteem'])
        # self.answer2 = Author.objects.filter(articles=max_articles['max_articles'])
        self.answer3 = Entry.objects.filter(Q(tags__name__contains='Кино') | Q(tags__name__contains='Музыка'))
        self.answer4 = Author.objects.filter(gender='ж').count()
        self.answer2 = None
        self.answer5 = None
        self.answer6 = Author.objects.filter(authorprofile__stage__range=(1, 5))
        self.answer7 = Author.objects.order_by().last()
        self.answer8 = Author.objects.filter(phone_number__isnull=False).count()
        self.answer9 = Author.objects.filter(age__lte=25)
        self.answer10 = None


        context = {f'answer{index}': self.__dict__[f'answer{index}'] for index in range(1,11)}  # Создайте здесь запросы к БД

        return render(request, 'train_db/training_db.html', context=context)

