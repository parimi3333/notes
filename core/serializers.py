from rest_framework import serializers
from .models import Note, AudioNote, VideoNote

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = '__all__'

class AudioNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioNote
        fields = '__all__'

class VideoNoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoNote
        fields = '__all__'
