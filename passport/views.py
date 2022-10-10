from django.shortcuts import render
from django.views import generic


class HomePage(generic.TemplateView):
    """
    Displays instructional video and links on landing page
    """

    template_name = 'index.html'
