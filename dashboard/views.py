from django.shortcuts import render, redirect
from main import models

def index(request):
    contacts = models.Contact.objects.filter(is_show=False).count()

    context = {
        'contacts':contacts
    }
    return render(request, 'dashboard/index.html', context)


def create_banner(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        models.Banner.objects.create(
            title=title,
            body=body,
        )
    return render(request, 'dashboard/banner/create.html')


def list_banner(request):
    banners = models.Banner.objects.all()
    context = {
        'banners':banners
    }
    return render(request, 'dashboard/banner/list.html', context)


def banner_detail(request, id):
    banner = models.Banner.objects.get(id=id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/detail.html', context)


def banner_edit(request, id):
    banner = models.Banner.objects.get(id=id)
    if request.method == 'POST':
        banner.title = request.POST['title']
        banner.body = request.POST['body']
        banner.save()
        return redirect('banner_detail', banner.id)
    context = {
        'banner':banner
    }
    return render(request, 'dashboard/banner/edit.html', context)


def banner_delete(request, id):
    models.Banner.objects.get(id=id).delete()
    return redirect('list_banner')


def create_service(request):
    if request.method == 'POST':
        name = request.POST['name']
        body = request.POST['body']
        icon = request.POST['icon']
        models.Service.objects.create(
            name = name,
            body = body,
            icon = icon
        )
    return render(request, 'dashboard/service/create.html')

def list_service(request):
    service = models.Service.objects.all()
    context = {
        'servie':service
    }
    return render(request, 'dashboard/service/list.html', context)


def service_detail(request, id):
    service = models.Service.objects.get(id=id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/detail.html', context)


def service_edit(request, id):
    service = models.Service.objects.get(id=id)
    if request.method == 'POST':
        service.title = request.POST['title']
        service.body = request.POST['body']
        service.icon = request.POST['icon']
        service.save()
        return redirect('banner_detail', service.id)
    context = {
        'service':service
    }
    return render(request, 'dashboard/service/edit.html', context)


def service_delete(request, id):
    models.Service.objects.get(id=id).delete()
    return redirect('list_service')


def create_aboutus(request):
    if request.method == "POST":
        body = request.POST['body']
        models.AboutUs.objects.create(
            body=body,
        )
    return render(request, 'dashboard/aboutus/create.html')


def list_aboutus(request):
    aboutus = models.AboutUs.objects.all()
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/list.html', context)


def aboutus_detail(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/detail.html', context)


def aboutus_edit(request, id):
    aboutus = models.AboutUs.objects.get(id=id)
    if request.method == 'POST':
        aboutus.body = request.POST['body']
        aboutus.save()
        return redirect('banner_detail', aboutus.id)
    context = {
        'aboutus':aboutus
    }
    return render(request, 'dashboard/aboutus/edit.html', context)


def aboutus_delete(request, id):
    models.AboutUs.objects.get(id=id).delete()
    return redirect('list_aboutus')


def create_price(request):
    if request.method == 'POST':
        title = request.POST['name']
        body = request.POST['body']
        price = request.POST['icon']
        models.Price.objects.create(
            title = title,
            body = body,
            price = price
        )
    return render(request, 'dashboard/price/create.html')

def list_price(request):
    price = models.Price.objects.all()
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/list.html', context)


def price_detail(request, id):
    price = models.Price.objects.get(id=id)
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/detail.html', context)


def price_edit(request, id):
    price = models.Price.objects.get(id=id)
    if request.method == 'POST':
        price.title = request.POST['title']
        price.body = request.POST['body']
        price.price = request.POST['price']
        price.save()
        return redirect('banner_detail', price.id)
    context = {
        'price':price
    }
    return render(request, 'dashboard/price/edit.html', context)


def price_delete(request, id):
    models.Price.objects.get(id=id).delete()
    return redirect('list_price')


def contact_detail(request, id):
    contact = models.Contact.objects.get(id=id)
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/detail.html', context)


def list_contact(request):
    contact = models.Contact.objects.all()
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/list.html', context)


def contact_edit(request, id):
    contact = models.Contact.objects.get(id=id)
    if request.method == 'POST':
        contact.name = request.POST['name']
        contact.email = request.POST['email']
        contact.phone = request.POST['phone']
        contact.body = request.POST['body']
        contact.save()
        return redirect('contact_detail', contact.id)
    context = {
        'contact':contact
    }
    return render(request, 'dashboard/contact/edit.html', context)