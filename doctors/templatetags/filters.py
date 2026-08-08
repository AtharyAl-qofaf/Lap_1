from django import template

register = template.Library()

@register.filter(name='doctor_status')
def doctor_status(value):
    """فلتر يحول حالة الطبيب إلى نص عربي مع إيموجي"""
    val = str(value).lower().strip()
   
    if val in ['available', 'متاح', 'true']:
        return "🟢 متاح للاستشارة"
    elif val in ['busy', 'مشغول']:
        return "🔴 غير متاح حالياً"
    else:
        return f"🩺 الحالة: {value}"