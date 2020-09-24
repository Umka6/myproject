from django.shortcuts import render, redirect
import telebot
from .forms import ApplicationsForm
from .models import Portfolio
from django.core.mail import send_mail
from django.views import View

# bot = telebot.TeleBot("1148924698:AAGA3K3MW0GQowVZ-0_MR6zIoy-tupWsvRQ")
bot = telebot.TeleBot('1116291257:AAFuY9YASfUnBJ6nwwLyvwJiLJykcepzgLI')

def index(request):
    portfolio = Portfolio.objects.all()
    form = ApplicationsForm()
    return render(request, 'mainapp/index.html', {'port': portfolio, 'form': form})


# def indexinner(request):
#     return render(request, 'mainapp/inner-page.html')

class ApplicationsView(View):
    def post(self, request):
        if request.method == 'POST':
            form = ApplicationsForm(request.POST)
            # print(request.POST)
            if form.is_valid():
                form.save()
                mail = form.cleaned_data['mail']
                name = form.cleaned_data['name']
                comment = form.cleaned_data['comment']
                subject = 'Новая заявка на подписку!'
                from_email = 'umutmarishbekova@gmail.com'
                to_email = ['umutmamyrgazieva@gmail.com', 'ymyt.91@mail.ru']
                message = 'Новая заявка!' + '\r\n' + '\r\n' + 'Почта: ' + mail + '\r\n' + '\r\n' + 'Имя:' + name + '\r\n' + 'Коммент' + comment
                send_mail(subject, message, from_email, to_email, fail_silently=False)
                bot.send_message(569589994, message)
        return redirect('home')



