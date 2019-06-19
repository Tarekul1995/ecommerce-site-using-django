from django.views.generic import TemplateView,DetailView
from django.shortcuts import render
from .models import Product



class Home_page(TemplateView):
    template_name = 'Product/Home.html'

    def get(self, request, *args, **kwargs):
        product = Product.objects.order_by('name')[0:9]
        if 'username' in request.session:
            username = request.session['username']
            return render(request, self.template_name, {'username': username, 'range': range(3),'products':product})

        return render(request, self.template_name, {'username': None, 'range': range(3),'products':product})


class product_detail(DetailView):
    template_name='Product/Product_detail.html'
    model=Product

    def get_context_data(self, **kwargs):
        context = super(product_detail, self).get_context_data(**kwargs)
        if 'username' in self.request.session:
            username = self.request.session['username']
        else:
            username = None
        context['username'] = username
        context['product'] = Product.objects.get(pk=self.object.pk)
        return context
