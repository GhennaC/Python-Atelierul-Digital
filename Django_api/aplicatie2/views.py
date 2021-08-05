from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
# Create your views here.
from aplicatie2.models import Companies


class CreateCompaniesView(LoginRequiredMixin, CreateView):
    model = Companies
    fields = '__all__'
    templates_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:adaugare')


class ListCompaniesView(LoginRequiredMixin, ListView):
    model = Companies
    template_name = 'aplicatie2/companies_index.html'


class UpdateCompaniesView(LoginRequiredMixin, UpdateView):
    model = Companies
    fields = '__all__'
    template_name = 'aplicatie2/companies_form.html'

    def get_success_url(self):
        return reverse('aplicatie2:listare')