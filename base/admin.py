from django.contrib import admin
from .models import User, Shanghai, THE, QS,Webometrics, WorkerFeedback, StudentFeedback
# Register your models here.
admin.site.register(User)
admin.site.register(Shanghai)
admin.site.register(Webometrics)
admin.site.register(QS)
admin.site.register(THE)
admin.site.register(WorkerFeedback)
admin.site.register(StudentFeedback)

