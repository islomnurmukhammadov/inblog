from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import BlogModel, SolutionModel,LinksModel,AboutMeModel
# Create your views here.

class homeView(TemplateView):
    template_name='home.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['links']=LinksModel.load()
        return context

class aboutView(TemplateView):
    template_name='about.html'

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['text']=AboutMeModel.load()
        return context


class blogView(ListView):
    model=BlogModel
    template_name='blog.html'
    context_object_name='postlar'

class solutionsView(ListView):
    model=SolutionModel
    template_name='solutions.html'
    context_object_name='yechimlar'


class oneBlogPostView(DetailView):
    model=BlogModel
    template_name='blogpost.html'
    context_object_name='post_malumoti'

class oneSolutionPostView(DetailView):
    model=SolutionModel
    template_name='solutionpost.html'
    context_object_name='yechim_malumoti'
