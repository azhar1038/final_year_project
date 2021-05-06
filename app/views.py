import io
from app.utils import load_and_generate
from django.shortcuts import render
from django.http import HttpResponse
import base64

# Create your views here.
def pred_view(request):
    if request.method == "POST":
        op = load_and_generate(request.FILES.get("image").file.name, resize=False)
        response = io.BytesIO()
        op.save(response, "gif")
        # return response
        return render(
            request,
            "index.html",
            context={
                "inp": base64.b64encode(
                    open(request.FILES.get("image").file.name, "rb").read()
                ).decode("utf-8"),
                "out": base64.b64encode(response.getvalue()).decode("utf-8"),
            },
        )
    else:
        return render(request, "index.html")
