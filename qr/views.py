# views.py
from django.shortcuts import render
from .forms import QRForm
from django.http import HttpResponse
import qrcode
from io import BytesIO

def home(request):
    return render(request,'index.html')

def generate_qr(request):
    if request.method == 'POST':
        form = QRForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data['data']

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=1,
            )
            qr.add_data(data)
            qr.make(fit=True)
            img = qr.make_image(fill_color="black", back_color="white")

            # Save the QR code image to a BytesIO buffer
            buffer = BytesIO()
            img.save(buffer)
            buffer.seek(0)

            # Return the image as an HTTP response
            return HttpResponse(buffer.getvalue(), content_type ="image/png")
    else:
        form = QRForm()

    return render(request, 'generate_qr.html', {'form': form})

import base64

def download_qr(request):
    # Retrieve the base64-encoded QR code from the session
    qr_code = request.session.get('qr_code')

    # Decode the base64 string into bytes
    qr_code_bytes = base64.b64decode(qr_code)

    # Return the QR code as a downloadable file
    response = HttpResponse(qr_code_bytes, content_type='image/png')
    response['Content-Disposition'] = 'attachment; filename="qrcode.png"'
    return response