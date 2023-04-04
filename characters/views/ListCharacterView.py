from django.views.generic.list import ListView
from characters.models import Character
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponseForbidden, HttpResponseNotAllowed

# list all characters, can also support searching by tags
class ListCharacterView(LoginRequiredMixin, ListView):
    login_url = reverse_lazy("accounts:login")
    template_name = "characters/list.html"
    context_object_name = "characters"
    model = Character

    def get_queryset(self):
        return self.request.user.character_set.all()
    
    def post(self, request, pk):
        return HttpResponseNotAllowed(("GET"))