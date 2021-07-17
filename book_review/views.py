from django.shortcuts import render,redirect
from django.views.generic.list import ListView
#from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

#from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Review
#from .forms import PositionForm

# Create your views here.
class CustomLoginView(LoginView):
	template_name = 'book_review/login.html'
	fields = '__all__'
	redirect_authenticated_user = True

	def get_success_url(self):
		return reverse_lazy('list')
	

class RegisterPage(FormView):
    template_name = 'book_review/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('list')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('list')
        return super(RegisterPage, self).get(*args, **kwargs)    

class ReviewList(LoginRequiredMixin, ListView):
    model = Review
    context_object_name = 'reviews'
    #template_name = 'book_review/books.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = context['reviews'].filter(user=self.request.user)


        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['reviews'] = context['reviews'].filter(
                book_name__contains=search_input)

        context['search_input'] = search_input

        return context   

class ReviewCreate(LoginRequiredMixin, CreateView):
	model = Review
	fields = '__all__'
	success_url = reverse_lazy('list')


class ReviewUpdate(LoginRequiredMixin, UpdateView):
	model = Review
	fields = '__all__'
	success_url = reverse_lazy('list')

class ReviewDelete(LoginRequiredMixin, DeleteView):
	model = Review
	context_object_name = 'review'
	success_url = reverse_lazy('list')