from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .forms import IrisForm
from .services import predict_iris
def home(request):
    return render(request, "predictor/predict_form.html", {"form": IrisForm()})


@csrf_exempt
@api_view(["POST"])
def predict_form(request):
    form = IrisForm(request.data)
    if not form.is_valid():
        return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    data = form.cleaned_data
    features = [
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"],
    ]
    result = predict_iris(features)

    return Response({"result": result, "submitted": True}, status=status.HTTP_200_OK)

@csrf_exempt
@api_view(["POST"])
def predict_api(request):
    required = ["sepal_length", "sepal_width", "petal_length", "petal_width"]
    payload = request.data
    missing = [k for k in required if k not in payload]
    if missing:
        return Response({"error": f"Missing: {', '.join(missing)}"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        features = [float(payload[k]) for k in required]
    except ValueError:
        return Response({"error": "All features must be numeric."}, status=status.HTTP_400_BAD_REQUEST)
    result = predict_iris(features)
    return Response({"result": result}, status=status.HTTP_200_OK)