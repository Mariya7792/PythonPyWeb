from django.contrib import admin
from .models import Author
admin.site.register(Author)

from .models import AuthorProfile
admin.site.register(AuthorProfile)

from .models import Entry
admin.site.register(Entry)

from .models import Tag
admin.site.register(Tag)
# Зарегистрируйте свои модели в админ панели здесь
