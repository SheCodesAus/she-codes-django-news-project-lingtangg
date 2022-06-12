from django.views import generic
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import DeleteView
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

class StoryDelete(DeleteView):
    model = NewsStory
    success_url = reverse_lazy('news:index')

@login_required
# UpdateView can also be used
def edit_story(request, *args, **kwargs):
    id = kwargs['pk']
    story_contents = NewsStory.objects.get(id=id)
    initial = {
        'title': story_contents.title, 
        'pub_date': story_contents.pub_date, 
        'content': story_contents.content, 
        'img_url': story_contents.img_url
        }
    form = StoryForm(initial=initial)
    if request.method == 'POST':
        update_form = StoryForm(request.POST, instance=story_contents)
        if update_form.is_valid():
            update_form.save()
            return redirect('/news')
    return render(request, 'news/editStory.html', {
        'form': form,
        'story_contents': story_contents
    })

