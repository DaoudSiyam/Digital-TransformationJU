from django.contrib import admin
from .models import User, Ranking, WorkerFeedback, StudentFeedback
# Register your models here.
admin.site.register(User)
admin.site.register(Ranking)
admin.site.register(WorkerFeedback)
admin.site.register(StudentFeedback)

