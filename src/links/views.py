from django.shortcuts import render
from .models import Link
from django.views.generic import DetailView
from .forms import AddLinkForm
from .utils import get_link_data


def home_view(request):
    form = AddLinkForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            name, price, image = get_link_data(form.cleaned_data['url'])
            Link.objects.create(name=name, price=price, image=image)

    form = AddLinkForm()
    qs = Link.objects.all()
    items_no = qs.count()

    context = {
        'qs': qs,
        'items_no': items_no,
        'form': form,
    }

    return render(request, 'links/main.html', context)


class ProductDetailView(DetailView):
    model = Link
    template_name = 'links/details.html'
