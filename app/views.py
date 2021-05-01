from app.utils import load_and_generate
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def pred_view(request):
    if request.method == "POST":
        op = load_and_generate(request.FILES.get("image").file.name, False)
        response = HttpResponse(content_type="image/jpg")
        op.save(response, "JPEG")
        return response
    else:
        return render(request, "home.html")
