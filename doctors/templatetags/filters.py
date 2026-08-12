from django import template

register = template.Library()

@register.filter(name='doctor_status')
def translate_status(value):
    """
    ياخذ الكلمة الانجليزية المدخلة من شريط البحث
    ويحولها إلى نص عربي مزين بالإيموجي
    """
    if not value:
        return ""
   
    clean_val = str(value).strip().lower()

    if clean_val == 'د.عذاري عصام':
        return "متاح للاستشارة 🟢"
    elif clean_val == 'د.خالد العمراني':
        return "غير متاح حالياً 🔴"
    else:
        return f"حالة غير معروفة: {value}"