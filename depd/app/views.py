from django.shortcuts import render,redirect
from app.forms import PHQ9Form, ProfileForm
from app.models import *
from django.contrib.auth.decorators import login_required


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


@login_required
def dashboard(request):
    profile = Profile.objects.get(email=request.user.email)

    context = {
        'profile': profile
    }

    return render(request, "app/dashboard.html",context)

@login_required
def complete_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            profile = form.save(commit=False)
            profile.email = request.user.email 
            profile.save()
            return redirect('dashboard') 
        else:
            print(form.errors) 
    else:
        form = ProfileForm()

    return render(request, 'app/complete-profile.html', {'form': form})



def howtouse(request):
    return render(request, "app/howtouse.html")



# OpenCV Video Streaming
import cv2
from django.http import StreamingHttpResponse

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

from fer import FER

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.emotion_detector = FER()

    def get_frame(self):
        success, image = self.video.read()
        emotions = self.emotion_detector.detect_emotions(image)

        # Draw the detected emotions on the frame
        for emotion in emotions:
            (x, y, w, h) = emotion['box']
            cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
            cv2.putText(image, max(emotion['emotions'], key=emotion['emotions'].get), 
                        (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()


def video_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# views.py
def submit_score(request):
    score = request.session.get('score', 0)
    emotions = request.session.get('emotions', [])  # Retrieve stored emotions
    if request.user.is_authenticated:
        TestResult.objects.create(user=request.user, phq9_score=score, emotions=emotions)
    request.session.flush()  # Reset the session after submitting
    return render(request, 'submit_score.html', {'score': score})
