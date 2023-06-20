from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.note_list_create_view, name='note-list-create'),
    path('notes/<int:pk>/', views.note_retrieve_update_destroy_view, name='note-retrieve-update-destroy'),
    path('audio-notes/', views.audio_note_create_view, name='audio-note-create'),
    path('video-notes/', views.video_note_create_view, name='video-note-create'),
]
