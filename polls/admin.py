from django.contrib import admin

from polls.models import Answer, Question

# Register your models here.
admin.site.register(Answer)
admin.site.register(Question)
