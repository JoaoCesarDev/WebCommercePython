from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.

class ProductListView(ListView):
    # traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    template_name = "products/list.html"

    # def get_context_data(self, *args, **kwargs):
    # context = super(ProductListView, self).get_context_data(*args, **kwargs)
    # print(context)
    # return context


# Function Based View
def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "products/list.html", context)


class ProductDetailView(DetailView):
    # traz todos os produtos do banco de dados sem filtrar nada
    queryset = Product.objects.all()
    template_name = "products/detail.html"


def get_context_data(self, *args, **kwargs):
    context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
    print(context)
    return context


# Function Based View
def product_detail_view(request, pk=None, *args, **kwargs):
    # instance = get_object_or_404(pk=pk)  # get the object id
    # try:
    # instance = Product.objects.get(id=pk)
    # except Product.DoesNotExist:
    # print('Nenhum produto encontrado aqui!')
    # raise Http404("Esse produto não existe!")
    qs = Product.objects.filter(id=pk)
    if qs.count() == 1:
        instance = qs.first()
    else:
        raise Http404("Esse produto não existe!")
    context = {
        'object_lis: instance'
    }
    return render(request, "products/detail.html", context)
