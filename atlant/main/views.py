from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from content.models import AboutModel, BlogModel, ReviewsModel
from seo.models import CompanyModel, SEOModel, FirstPageNews
from shelude.models import ScheduleModel, ClientModel
from django.views.decorators.csrf import csrf_exempt



def submit_client_form(request):
    if request.method == "POST":
        print("POST запрос получен")
        print(request.POST)

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')

        print(f"Name: {name}, Phone: {phone}, Email: {email}")

        if not name or not phone or not email:
            return JsonResponse({'status': 'error', 'message': 'Все поля обязательны для заполнения.'}, status=400)

        client_request = ClientModel.objects.create(
            name=name,
            phone=phone,
            email=email,
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
        'blogs' : blogs,
        'reviews' : reviews,
    })


def blog_detail(request, pk):
    blog = get_object_or_404(BlogModel, pk=pk)
    
    # Отладочный вывод
    print(f"Blog: {blog}")
    print(f"Title: {blog.title}, Text: {blog.text}, Theme: {blog.theme}, Img: {blog.get_image_url()}")

    data = {
        'title': blog.title,
        'text': blog.text,
        'img': blog.get_image_url(),
    }
    
    return JsonResponse(data)

