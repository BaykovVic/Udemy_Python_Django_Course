from django.shortcuts import render
from .models import Order
from .forms import OrderForm
from cms.models import CmsSlider
from price.models import PriceCard, PriceTable

# Create your views here.
def first_page(request):
    slider_list = CmsSlider.objects.all()
    pc_1 = PriceCard.objects.get(pk=1)
    pc_2 = PriceCard.objects.get(pk=2)
    pc_3 = PriceCard.objects.get(pk=3)
    pt = PriceTable.objects.all()
    form = OrderForm()
    dict_obj = {'slider_list': slider_list,
                'pc_1': pc_1,
                'pc_2': pc_2,
                'pc_3': pc_3,
                'pt': pt,
                'form': form,}
    return render(request, './index.html', dict_obj)


def thanks_page(request):
    name = request.POST['name']
    phone = request.POST['phone']
    Order.objects.create(order_name=name, order_phone=phone)
    return render(request, "./thanks_page.html", {'name': name,
                                                  'phone': phone})
