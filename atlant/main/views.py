from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from content.models import AboutModel, BlogModel, ReviewsModel
from seo.models import CompanyModel, SEOModel, FirstPageNews, EmailSettings
from shelude.models import ScheduleModel, ClientModel
from django.core.mail import send_mail


# Функция для получения email из модели
def get_recipient_email():
    try:
        email_settings = EmailSettings.objects.first()
        return email_settings.email if email_settings else None
    except EmailSettings.DoesNotExist:
        return None


# Отправка формы клиента
def submit_client_form(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone = request.POST.get('phone')

        if not name or not phone:
            return JsonResponse({'status': 'error', 'message': 'Все поля обязательны для заполнения.'}, status=400)

        # Сохранение данных в базу
        client_request = ClientModel.objects.create(name=name, phone=phone)

        # Получение email и отправка письма
        recipient_email = get_recipient_email()
        if recipient_email:
            subject = 'Новая заявка от {}'.format(name)
            message = 'Имя: {}\nТелефон: {}'.format(name, phone)
            
            send_mail(
                subject,
                message,
                None,  # Отправитель (None, если от клиента не требуется)
                [recipient_email],
                fail_silently=False,
            )

        return JsonResponse({'status': 'success', 'message': 'Данные успешно отправлены!'})

    return JsonResponse({'status': 'error', 'message': 'Неправильный метод запроса'}, status=400)


# Отправка формы отзыва
def submit_review_form(request):
    if request.method == "POST" and request.is_ajax():
        name = request.POST.get('name-review')
        text = request.POST.get('text-review')

        if not name or not text:
            return JsonResponse({'status': 'error', 'message': 'Все поля обязательны для заполнения.'}, status=400)

        # Сохранение данных в базу
        review_request = ReviewsModel.objects.create(name=name, text=text)

        # Получение email и отправка письма
        recipient_email = get_recipient_email()
        if recipient_email:
            subject = 'Новый отзыв от {}'.format(name)
            message = 'Отзыв: {}\nИмя: {}'.format(text, name)
            
            send_mail(
                subject,
                message,
                None,  # Отправитель (None, если от клиента не требуется)
                [recipient_email],
                fail_silently=False,
            )

        return JsonResponse({'status': 'success', 'message': 'Данные успешно отправлены!'})

    return JsonResponse({'status': 'error', 'message': 'Неправильный метод запроса'}, status=400)


def index(request):
    seo = SEOModel.objects.all()
    company = CompanyModel.objects.all()
    firstNews = FirstPageNews.objects.all()
    abouts = AboutModel.objects.filter(publish=True)
    blogs = BlogModel.objects.filter(publish=True)
    reviews = ReviewsModel.objects.filter(publish=True)
    
    # Получаем расписание и группируем по дням недели
    schedule_data = ScheduleModel.objects.all().order_by('weekday')
    schedule_by_weekday = {day: [] for day in range(1, 8)}  # 1-7 для понедельника-воскресенья

    for schedule in schedule_data:
        schedule_by_weekday[schedule.weekday].append({
            'age': schedule.age,
            'start_time': schedule.start_time,
            'end_time': schedule.end_time,
        })

    return render(request, 'index.html', {
        'seo': seo,
        'company': company,
        'firstNews': firstNews,
        'abouts': abouts,
        'schedule_by_weekday': schedule_by_weekday,
        'blogs': blogs,
        'reviews': reviews,
    })


def blog_detail(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)


    data = {
        'title': blog.title,
        'text': blog.text,
        'img': blog.get_image_url(),
    }
    
    return JsonResponse(data)


def license(request):
    return render(request, 'license.html')

def politic(request):
    return render(request, 'politic.html')


def robots_txt(request):
    with open('robots.txt', 'r') as f:
        return HttpResponse(f.read(), content_type="text/plain")
    
    
def sitemap_xml(request):

    xml_content = ['<?xml version="1.0" encoding="UTF-8"?>']
    xml_content.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    urls = [
        {'loc': request.build_absolute_uri('/'), 'changefreq': 'daily'},
        {'loc': request.build_absolute_uri('/politic/'), 'changefreq': 'monthly'},
        {'loc': request.build_absolute_uri('/license/'), 'changefreq': 'monthly'},
    ]
    
    for url in urls:
        xml_content.append('<url>')
        xml_content.append(f'<loc>{url["loc"]}</loc>')
        xml_content.append(f'<changefreq>{url["changefreq"]}</changefreq>')
        xml_content.append('</url>')

    xml_content.append('</urlset>')

    return HttpResponse("\n".join(xml_content), content_type="application/xml")