from django.db import models
from django.contrib import admin


class TeamInfo(models.Model):
	# 姓名
	numId = models.IntegerField()
	info = models.TextField()



# list_displays 为后台显示的字段（list 可以多个）
class TeamInfoAdmin(admin.ModelAdmin):
	list_display = ('numId','info')


# 注册到后台
admin.site.register(TeamInfo,TeamInfoAdmin)