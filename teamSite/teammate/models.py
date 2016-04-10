from django.db import models
from django.contrib import admin

# Create your models here.
class TeamMate(models.Model):
	# 姓名
	name = models.CharField(max_length = 100)
	# 性别
	gender = models.CharField(max_length = 100)
	# 擅长
	master = models.CharField(max_length = 100)


class TeamMateAdmin(admin.ModelAdmin):
	list_display = ('name','master')


# 注册到后台
admin.site.register(TeamMate,TeamMateAdmin)