from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Album, Journal
from .forms import UserForm


class IndexView(generic.ListView):
    template_name = 'mainapp/add.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = "mainapp/album_detail.html"


class AlbumCreate(CreateView):
    model = Album
    fields = ['place', 'album_cover']


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['place', 'album_cover']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('index')


class JournalCreate(CreateView):
    model = Journal
    fields = ['journal', 'journal_title', 'journal_details', 'date', 'time', 'journal_image']


class JournalUpdate(UpdateView):
    model = Journal
    fields = ['journal', 'journal_title', 'journal_details', 'journal_image']


class JournalDelete(DeleteView):
    model = Journal
    success_url = reverse_lazy('index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'mainapp/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:

                if user.is_active:

                    login(request, user)
                    return redirect('index')

        return render(request, self.template_name, {'form': form})
