import os
from django.core.exceptions import ValidationError

def validate_yemeni_phone(value):
    # التحقق من أن رقم الهاتف يمني ويبدأ بـ 7 ويتكون من 9 أرقام
    if not value.isdigit():
        raise ValidationError('يجب أن يحتوي رقم الهاتف على أرقام فقط.')
    if len(value) != 9 or not value.startswith('7'):
        raise ValidationError('رقم الهاتف يجب أن يتكون من 9 أرقام ويبدأ بـ 7.')

def validate_image_size(value):
    # التحقق من أن حجم الصورة لا يتجاوز 2 ميجابايت
    max_size_mb = 2
    if value.size > max_size_mb * 1024 * 1024:
        raise ValidationError(f'حجم الصورة لا يمكن أن يتجاوز {max_size_mb} ميجابايت.')