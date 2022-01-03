from django.views.generic import ListView
from django.shortcuts import render
from  django.http import HttpResponse
from articles.models import Article, Scope




def articles_list(request):
    template = 'articles/news.html'
    context = {'object_list': Article.objects.all()}

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # ordering = '-published_at'

    return render(request, template, context)


