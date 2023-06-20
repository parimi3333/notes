from django.db import models
from django.contrib.auth.models import User

class Note(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class AudioNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    audio_file = models.FileField(upload_to='audio_notes/')

    def __str__(self):
        return f"AudioNote: {self.note.title}"

class VideoNote(models.Model):
    note = models.ForeignKey(Note, on_delete=models.CASCADE)
    video_file = models.FileField(upload_to='video_notes/')

    def __str__(self):
        return f"VideoNote: {self.note.title}"
