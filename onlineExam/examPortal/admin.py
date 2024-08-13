from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Subject, Question, Exam, UserRegistration
from django.contrib.auth.models import User

class UserRegistrationInline(admin.StackedInline):
    model = UserRegistration
    can_delete = False
    verbose_name_plural = 'User Registration Details'

class UserAdmin(BaseUserAdmin):
    inlines = (UserRegistrationInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Exam)
