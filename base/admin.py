from django.contrib import admin
from .models import User, Feedback, UniversityRanking

# Register your models here.
admin.site.register(User)
admin.site.register(Feedback)
admin.site.register(UniversityRanking)
