from django.conf import settings
from django.views.generic import TemplateView
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.shortcuts import redirect

from .models import Logo, SliderHome, GalleryHome, SocialNetwork, Videos, Statistic, Us, Contact
from apps.productos.models import Brand


class HomeView(TemplateView):
    template_name = 'front/home.html'

    def get_context_data(self, **kwargs):
        try:
            logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
            logo = None
        sliderHomeDesktop = SliderHome.objects.filter(active=True, mobile=False)
        sliderHomeMobile = SliderHome.objects.filter(active=True, mobile=True)
        brands = Brand.objects.filter(active=True)
        try:
            galleryHome = GalleryHome.objects.get(active=True)
        except GalleryHome.DoesNotExist:
            galleryHome = None
        videos = Videos.objects.filter(active=True)
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'sliderHomeDesktop': sliderHomeDesktop,
            'sliderHomeMobile': sliderHomeMobile,
            'brands': brands,
            'galleryHome': galleryHome,
            'videos': videos,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context


class UsView(TemplateView):
    template_name = 'front/nosotros.html'

    def get_context_data(self, **kwargs):
        try:
            logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
            logo = None
        items = Us.objects.filter(active=True)
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'items': items,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context


class ContactView(TemplateView):
    template_name = 'front/contacto.html'

    def get_context_data(self, **kwargs):
        try:
            logo = Logo.objects.get(active=True)
        except Logo.DoesNotExist:
            logo = None
        try:
            dataContact = Contact.objects.get(active=True)
        except Contact.DoesNotExist:
            dataContact = None
        statistics = Statistic.objects.filter(active=True)
        socialNetworks = SocialNetwork.objects.filter(active=True)
        context = {
            'logo': logo,
            'dataContact': dataContact,
            'statistics': statistics,
            'socialNetworks': socialNetworks,
        }
        return context


def MailContact(request):
    if request.method == "POST":
        full_name = request.POST['full_name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        template = render_to_string('front/mail-contact.html', {
            'full_name': full_name,
            'email': email,
            'subject': subject,
            'message': message
        })

        email = EmailMultiAlternatives(
            'Contacto desde IsakitoWeb',
            template,
            settings.EMAIL_HOST_USER,
            [settings.EMAIL_CONTACT_ISAKITO]
        )

        email.attach_alternative(template, 'text/html')
        email.send()

        messages.success(request, 'Correo enviado exitosamente')

        return redirect('generales_app:contacto')
