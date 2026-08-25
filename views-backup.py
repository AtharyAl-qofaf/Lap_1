from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def home(request):
    search_query = request.GET.get('q', '')

    hospital_name = "Care Medical"
    lab_number = 3
    instructor = "Eng. Rim Taher"
    clinic_open = True
    description = None

    doctors_list = [
        {
            "id": 1,
            "name": "د. خالد العمراني",
            "specialty": "استشاري طب الأطفال",
            "rating": "4.8 / 5.0",
            "reviews_count": 150,
            "experience_years": 12,
            "age": 42,
            "degree": "دكتوراة في طب وجراحة الأطفال - جامعة القاهرة",
            "schedule": "يومياً (8 AM - 8 PM)",
            "available": True,
        },
        {
            "id": 2,
            "name": "د. عذاري القفاف",
            "specialty": "استشارية المخ والأعصاب", 
            "rating": "5.0 / 5.0",
            "reviews_count": 98,
            "experience_years": 8,
            "age": 38,
            "degree": "زمالة جراحة المخ والأعصاب - البورد العربي",
            "schedule": "الأحد - الخميس (10 AM - 4 PM)",
            "available": True,
        },
        {
            "id": 3,
            "name": "د. القفاف",
            "specialty": "استشاري أمراض القلب",
            "rating": "4.9 / 5.0",
            "reviews_count": 120,
            "experience_years": 15,
            "age": 50,
            "degree": "دكتوراة أمراض وجراحة القلب والأوعية الدموية",
            "schedule": "الخميس - السبت (4 PM - 9 PM)",
            "available": False,
        },
    ]

    main_doctor = doctors_list[0]

    context = {
        "hospital_name": hospital_name,
        "lab_number": lab_number,
        "instructor": instructor,
        "clinic_open": clinic_open,
        "description": description,
        "doctors": doctors_list,
        "main_doctor": main_doctor,
        "status_text": "available",
        "search_query": search_query,
    }
    return render(request, "doctors/home.html", context)


def about(request):
    return render(request, "doctors/about.html")


def detail(request, doctor_id):
    doctors_list = [
        {
            "id": 1,
            "name": "د. خالد العمراني",
            "specialty": "استشاري طب الأطفال",
            "rating": "4.8 / 5.0 (150 تقييم)",
            "experience_years": 12,
            "age": 42,
            "degree": "دكتوراة في طب وجراحة الأطفال - جامعة القاهرة",
            "schedule": "يومياً (8 AM - 8 PM)",
            "available": True,
            "location": "العيادة الرئيسية - الدور الثاني",
        },
        {
            "id": 2,
            "name": "د. عذاري القفاف",
            "specialty": "استشارية المخ والأعصاب",
            "rating": "5.0 / 5.0 (98 تقييم)",
            "experience_years": 8,
            "age": 38,
            "degree": "زمالة جراحة المخ والأعصاب - البورد العربي",
            "schedule": "الأحد - الخميس (10 AM - 4 PM)",
            "available": True,
            "location": "عيادة الأعصاب - الدور الثالث",
        },
        {
            "id": 3,
            "name": "د. القفاف",
            "specialty": "استشاري أمراض القلب",
            "rating": "4.9 / 5.0 (120 تقييم)",
            "experience_years": 15,
            "age": 50,
            "degree": "دكتوراة أمراض وجراحة القلب والأوعية الدموية",
            "schedule": "الخميس - السبت (4 PM - 9 PM)",
            "available": False,
            "location": "مركز القلب - الدور الأول",
        },
    ]

    selected_doctor = None
    for doc in doctors_list:
        if doc["id"] == doctor_id:
            selected_doctor = doc
            break

    context = {
        "doctor": selected_doctor,
        "doctor_id": doctor_id,
    }
    return render(request, "doctors/detail.html", context)