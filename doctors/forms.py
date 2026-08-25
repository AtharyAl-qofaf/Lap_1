from django import forms

from .models import DoctorProfile


class DoctorProfileForm(forms.ModelForm):
    class Meta:
        model = DoctorProfile
        fields = [
            "user",
            "specialty",
            "rating",
            "reviews_count",
            "experience_years",
            "age",
            "degree",
            "schedule",
            "location",
            "available",
            "services",
        ]
        widgets = {
            "specialty": forms.TextInput(
                attrs={"placeholder": "مثال: استشاري أمراض القلب"}
            ),
            "rating": forms.NumberInput(
                attrs={"min": "0", "max": "5", "step": "0.1"}
            ),
            "reviews_count": forms.NumberInput(attrs={"min": "0"}),
            "experience_years": forms.NumberInput(attrs={"min": "0"}),
            "age": forms.NumberInput(attrs={"min": "1"}),
            "degree": forms.TextInput(
                attrs={"placeholder": "المؤهل العلمي"}
            ),
            "schedule": forms.TextInput(
                attrs={"placeholder": "أوقات الدوام"}
            ),
            "location": forms.TextInput(
                attrs={"placeholder": "موقع العيادة"}
            ),
            "services": forms.SelectMultiple(),
        }
        labels = {
            "user": "حساب الطبيب",
            "specialty": "التخصص الطبي",
            "rating": "التقييم",
            "reviews_count": "عدد التقييمات",
            "experience_years": "سنوات الخبرة",
            "age": "العمر",
            "degree": "المؤهل العلمي",
            "schedule": "مواعيد الدوام",
            "location": "موقع العيادة",
            "available": "متاح للحجز",
            "services": "الخدمات التي يقدمها الطبيب",
        }