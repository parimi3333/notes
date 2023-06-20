from django.urls import path
from core.views import (
    NoteListCreateView,
    NoteRetrieveUpdateDestroyView,
    AudioNoteCreateView,
    VideoNoteCreateView
)

urlpatterns = [
    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteRetrieveUpdateDestroyView.as_view(), name='note-retrieve-update-destroy'),
    path('audio-notes/', AudioNoteCreateView.as_view(), name='audio-note-create'),
    path('video-notes/', VideoNoteCreateView.as_view(), name='video-note-create'),
]
