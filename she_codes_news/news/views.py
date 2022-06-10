from audioop import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render
from .models import NewsStory
from .forms import StoryForm
from users.models import CustomUser

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    
    def get_queryset(self):
        '''Return all news stories.'''
        return NewsStory.objects.all().order_by('-pub_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        selectedAuthor = self.request.GET.get('author', None)
        if selectedAuthor is not None:
            authorID = CustomUser.objects.get(username=selectedAuthor).id
            query = NewsStory.objects.filter(author_id=authorID).order_by('-pub_date')
        else:
            query = NewsStory.objects.all().order_by('-pub_date')
        context['latest_stories'] = query[:4]
        context['all_stories'] = query
        context['authors'] = CustomUser.objects.order_by().values_list('username', flat=True).distinct()
        return context

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

class AddStoryView(generic.CreateView):
    form_class = StoryForm
    context_object_name = 'storyForm'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
