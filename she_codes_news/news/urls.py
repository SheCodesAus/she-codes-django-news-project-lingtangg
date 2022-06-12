from django.urls import path
from .views import IndexView, StoryView, AddStoryView, edit_story

app_name = 'news'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', StoryView.as_view(), name='story'),
    path('add-story/', AddStoryView.as_view(), name='newStory'),
    path('edit-story/<int:pk>', edit_story, name='editStory'),
]
