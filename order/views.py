from django.views import generic
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import Http404

from accounts.models import User
from .models import Order
from .forms import OrderCreateForm


class OrderCreateView(generic.CreateView):
    model = Order
    form_class = OrderCreateForm
    success_url = reverse_lazy('order:list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        print(form.cleaned_data)
        form.save()

        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class OrderListView(generic.ListView):

    def get_queryset(self):
        query = Order.objects.filter(user=self.request.user)
        return query


class OrderDeleteView(generic.DeleteView):
    model = Order
    success_url = reverse_lazy('order:list')

    def get_object(self, queryset=None):
        obj = super().get_object()
        if not obj.user == self.request.user:
            raise Http404()

        return obj
