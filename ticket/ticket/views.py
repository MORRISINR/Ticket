# from django.shortcuts import render

# from django.conf import settings
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

# def home(request):
# 	return render(request, 'home_page.html')



# # Envía un correo electrónico utilizando smtplib.
# def enviar_correo(subject, body, to_email, 
#                   html_body=None, from_name=None, content_type='plain'):
#     """
#     :param subject: Asunto del correo
#     :param body: Cuerpo del correo en texto plano
#     :param to_email: Dirección(es) de correo del destinatario
#     :param html_body: Cuerpo del correo en HTML (opcional)
#     :param from_name: Nombre del remitente (opcional)
#     :param content_type: Tipo de contenido ('plain' o 'html')
#     """

#     # Crear el mensaje de correo
#     msg = MIMEMultipart("alternative")
#     from_email = settings.DEFAULT_FROM_EMAIL  # Usar la dirección por defecto
#     msg["From"] = f"{from_name} <{from_email}>" if from_name else from_email
#     msg["To"] = to_email
#     msg["Subject"] = subject

#     # Validar el content_type
#     if content_type not in ['plain', 'html']:
#         raise ValueError("content_type debe ser 'plain' o 'html'")

#     # Adjuntar cuerpo en texto plano o HTML según el content_type
#     if content_type == 'plain':
#         msg.attach(MIMEText(body, 'plain'))
#     else:
#         msg.attach(MIMEText(html_body, 'html') if html_body else MIMEText(body, 'html'))

#     try:
#         # Conectar y enviar el correo
#         with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
#             server.starttls()  # Conexión segura
#             server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
#             server.sendmail(from_email, to_email, msg.as_string())
#     except Exception:
#         raise EmailError(f"Error sending email: {e}")
from django.shortcuts import render
from django.conf import settings
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def home(request):
    return render(request, 'home_page.html')


# Envía un correo electrónico utilizando smtplib.
def enviar_correo(subject, body, to_email,
                   html_body=None, from_name=None, content_type='plain'):
    """
    :param subject: Asunto del correo
    :param body: Cuerpo del correo en texto plano
    :param to_email: Dirección(es) de correo del destinatario
    :param html_body: Cuerpo del correo en HTML (opcional)
    :param from_name: Nombre del remitente (opcional)
    :param content_type: 'plain' o 'html'
    """

    msg = MIMEMultipart("alternative")

    from_email = settings.DEFAULT_FROM_EMAIL

    msg["From"] = f"{from_name} <{from_email}>" if from_name else from_email
    msg["To"] = to_email
    msg["Subject"] = subject

    # Validación
    if content_type not in ['plain', 'html']:
        raise ValueError("content_type debe ser 'plain' o 'html'")

    # Cuerpo del mensaje
    if content_type == 'plain':
        msg.attach(MIMEText(body, 'plain'))
    else:
        msg.attach(MIMEText(html_body if html_body else body, 'html'))

    try:
        print("📨 Enviando correo a:", to_email)

        with smtplib.SMTP(settings.EMAIL_HOST, settings.EMAIL_PORT) as server:
            server.set_debuglevel(1)  # 👈 muestra todo el proceso SMTP
            server.starttls()

            print("🔐 Iniciando login SMTP...")
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

            print("📤 Enviando mensaje...")
            response = server.sendmail(
                from_email,
                [to_email] if isinstance(to_email, str) else to_email,
                msg.as_string()
            )

            print("📬 Respuesta SMTP:", response)

        print("✅ Correo enviado correctamente")

    except Exception as e:
        raise Exception(f"❌ Error sending email: {e}")