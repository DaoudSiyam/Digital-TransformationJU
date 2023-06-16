from django.contrib import admin
from .models import User, ShanghaiRanking, WebometricsRanking, QSRanking, THERanking , WorkerFeedback, StudentFeedback

# Register your models here.
admin.site.register(User)
admin.site.register(ShanghaiRanking)
admin.site.register(WebometricsRanking)
admin.site.register(QSRanking)
admin.site.register(THERanking)
admin.site.register(WorkerFeedback)
admin.site.register(StudentFeedback)

