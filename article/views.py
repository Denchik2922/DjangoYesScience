from django.views.generic import ListView, DetailView
from .models import Article
from django.db.models import Q


class ArticleListView(ListView):
    """Article view"""
    model = Article
    paginate_by = 6

    def get_queryset(self):
        queryset = self.model.objects.all()
        if self.request.GET.get('search'):
            search = self.request.GET.get('search')
            queryset = self.model.objects.filter(Q(title__icontains=search))
        return queryset


class ArticleDetailView(DetailView):
    """Article detail view"""
    model = Article
    slug_field = 'url'
