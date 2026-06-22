from typing import Any
import time
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy
from app.models import Article
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin



class ArticleListView(LoginRequiredMixin,ListView):
    template_name = "app/home.html"
    model = Article
    context_object_name = "articles"
    paginate_by=5

    def get_queryset(self) -> QuerySet[Any]:
        time.sleep(2)
        search = self.request.GET.get("search")

        queryset = super().get_queryset().filter(
            creater=self.request.user
        )
    
        if search:
            queryset = queryset.filter(title__icontains=search)

        return queryset.order_by("-created_at")


class ArticleResultsView(ArticleListView):
    template_name = "app/article_results.html"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "app/article_create.html"
    model = Article
    fields=["title","status","content","twitter_post"]
    success_url = reverse_lazy("home")


    def form_valid(self, form):
        form.instance.creater = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "app/article_update.html"
    model = Article
    fields=["title","status","content","twitter_post"]
    success_url = reverse_lazy("home")
    context_object_name="article"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creater

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin,SuccessMessageMixin, DeleteView):
    template_name = "app/article_delete.html"
    model = Article
    success_url = reverse_lazy("home")
    success_message="Article Deleted Succussfully."
    context_object_name = "article"

    def test_func(self) -> bool | None:
        return self.request.user == self.get_object().creater


