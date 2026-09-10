from django.core.mail import send_mail

def send_welcome_email(user_email, username):
    subject = "مرحباً بك في المنظومة"
    message = f"أهلاً بك يا {username}، تم تسجيل حسابك بنجاح!"
    send_mail(subject, message, 'yemen_app@example.com', [user_email, 'engreemalwaeel@gmail.com'])