from django.shortcuts import render
from app.forms import PHQ9Form

# Create your views here.

def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")

def phq9_view(request):
    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():
            score = sum(int(form.cleaned_data[q]) for q in form.cleaned_data)
            # PHQ-9 Scoring Criteria
            if score >= 20:
                result = "Severe Depression"
            elif score >= 15:
                result = "Moderately Severe Depression"
            elif score >= 10:
                result = "Moderate Depression"
            elif score >= 5:
                result = "Mild Depression"
            else:
                result = "Minimal or No Depression"

            return render(request, 'app/result.html', {'score': score, 'result': result})
    else:
        form = PHQ9Form()

    return render(request, 'app/phq9_form.html', {'form': form})