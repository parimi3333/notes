from django.contrib import admin
from .models import Note, AudioNote, VideoNote

admin.site.register(Note)
admin.site.register(AudioNote)
admin.site.register(VideoNote)
# Register your models here.
