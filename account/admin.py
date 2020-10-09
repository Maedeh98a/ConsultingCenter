from django.contrib import admin
from django.contrib.admin.options import InlineModelAdmin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from .models import User, University, Major, Consultant, Student

UserAdmin.fieldsets[1][1]['fields'] = ('first_name', 'last_name', 'email', 'phone', 'photo')
UserAdmin.fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'phone', 'photo')}),
        (_('Permissions'), {
            'fields': ('is_student', 'is_consultant', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

admin.site.register(User, UserAdmin)


@admin.register(University)
class UniAdmin(admin.ModelAdmin):
    list_display = ['university_name', 'university_city', 'phone']
    search_fields = ['university_name', 'university_city']


@admin.register(Major)
class MajorAdmin(admin.ModelAdmin):
    list_display = ['major_name']
    search_fields = ['major_name']


admin.site.register(Student)

#
# class ConsultantInline(admin.StackedInline):
#     model = Consultant
#     can_delete = True
#     verbose_name_plural = 'مشاوران'
#     fk_name = 'user'
#
#
# class CustomConsultantAdmin(UserAdmin):
#     inlines = (ConsultantInline, )
#
#     def get_inline_instances(self, request, obj=None):
#         if not obj:
#             return list()
#         return super(CustomConsultantAdmin, self).get_inline_instances(request, obj)
#

admin.site.register(Consultant)




