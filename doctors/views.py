from django.contrib.auth.decorators import login_required
#from django.shortcuts import get_object_or_404, render
from django.shortcuts import get_object_or_404, redirect, render
from .models import DoctorProfile
from .forms import DoctorProfileForm

@login_required(login_url="login")
def home(request):
    search_query = request.GET.get("q", "").strip()

    # QuerySet 1: all() جلب جميع الأطباء من PostgreSQL./    
    doctors = DoctorProfile.objects.all()

    # QuerySet 2: filter() البحث في التخصص.
    if search_query:
        doctors = doctors.filter(specialty__icontains=search_query)

    # QuerySet 3: exclude() استبعاد الحسابات غير النشطة.
    doctors = doctors.exclude(user__is_active=False)

    # QuerySet 4: order_by() ترتيب النتائج حسب التقييم ثم الاسم.
    doctors = doctors.order_by("-rating", "user__last_name")

    # QuerySet 5: exists() التحقق هل توجد نتائج.
    has_doctors = doctors.exists()

    # QuerySet 6: count() حساب عدد النتائج.
    doctors_count = doctors.count()

    # QuerySet 7: first() اختيار أول طبيب ليكون الطبيب الرئيسي.
    main_doctor = doctors.first()

    context = {
        "hospital_name": "Care Medical",
        "lab_number": 3,
        "instructor": "Eng. Rim Taher",
        "clinic_open": True,
        "description": None,
        "doctors": doctors,
        "main_doctor": main_doctor,
        "status_text": "available",
        "search_query": search_query,
        "has_doctors": has_doctors,
        "doctors_count": doctors_count,
    }

    return render(request, "doctors/home.html", context)


def about(request):
    return render(request, "doctors/about.html")


def detail(request, doctor_id):
    # get_object_or_404 يستخدم QuerySet get() داخليًا.
    doctor = get_object_or_404(
        DoctorProfile.objects.select_related("user"),
        pk=doctor_id,
    )






    # QuerySet إضافي: values() لجلب بيانات محددة للاختبار والشرح.
    doctor_summary = DoctorProfile.objects.filter(pk=doctor_id).values(
        "id",
        "specialty",
        "rating",
        "available",
    ).first()

    context = {
        "doctor": doctor,
        "doctor_id": doctor_id,
        "doctor_summary": doctor_summary,
    }

    return render(request, "doctors/detail.html", context)


@login_required(login_url="login")
def doctor_create(request):
    if request.method == "POST":
        form = DoctorProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("doctors:home")
    else:
        form = DoctorProfileForm()

    context = {
        "form": form,
        "title": "إضافة طبيب جديد",
    }
    return render(request, "doctors/doctor_form.html", context)



@login_required(login_url="login")
def doctor_update(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, pk=doctor_id)

    if request.method == "POST":
        form = DoctorProfileForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect("doctors:home")
    else:
        form = DoctorProfileForm(instance=doctor)

    context = {
        "form": form,
        "title": "تعديل بيانات الطبيب",
        "doctor": doctor,
    }
    return render(request, "doctors/doctor_form.html", context)


@login_required(login_url="login")
def doctor_delete(request, doctor_id):
    doctor = get_object_or_404(DoctorProfile, pk=doctor_id)

    if request.method == "POST":
        doctor.delete()
        return redirect("doctors:home")

    context = {
        "doctor": doctor,
        "title": "تأكيد حذف الطبيب",
    }
    return render(request, "doctors/doctor_confirm_delete.html", context)