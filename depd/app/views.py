from django.shortcuts import render,redirect
from app.forms import PHQ9Form, ProfileForm,  ConsultationBookingForm
from app.models import *
from django.contrib.auth.decorators import login_required
import cv2
from django.http import StreamingHttpResponse
from fer import FER
from collections import Counter

# Create your views here.

def home(request):
    return render(request, "app/home.html")


def about(request):
    return render(request, "app/about.html")


@login_required
def dashboard(request):
    profile = Profile.objects.get(email=request.user.email)
    results = TestResult.objects.filter(user=request.user).order_by('-date')

    context = {
        'profile': profile,
        'results': results,
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


# views.py
def submit_score(request):
    score = request.session.get('score', 0)
    emotions = request.session.get('emotions', [])  # Retrieve stored emotions
    if request.user.is_authenticated:
        TestResult.objects.create(user=request.user, phq9_score=score, emotions=emotions)
    request.session.flush()  # Reset the session after submitting
    return render(request, 'submit_score.html', {'score': score})


import cv2
from fer import FER
from django.http import StreamingHttpResponse
from django.shortcuts import render
from .forms import PHQ9Form

class VideoCamera:
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        self.emotion_detector = FER()
        self.is_running = False

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        emotions = self.emotion_detector.detect_emotions(image)

        for emotion in emotions:
            (x, y, w, h) = emotion['box']
            dominant_emotion = max(emotion['emotions'], key=emotion['emotions'].get)
            print(f"Detected Emotion: {dominant_emotion}")  # Log detected emotion for debugging

            cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(image, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def detect_emotions(self):
        if not self.is_running:
            return None
        success, image = self.video.read()
        emotions = self.emotion_detector.detect_emotions(image)
        if emotions:
            dominant_emotion = max(emotions[0]['emotions'], key=emotions[0]['emotions'].get)
            return dominant_emotion
        return None

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False

def gen(camera):
    while camera.is_running:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

def video_feed(request):
    camera = VideoCamera()
    camera.start()
    return StreamingHttpResponse(gen(camera),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

from django.contrib.auth.decorators import login_required
from collections import Counter
from .models import TestResult

@login_required
def phq9_view(request):
    video_camera = VideoCamera()
    video_camera.start()

    # Retrieve or create an EmotionSessionData entry for the current user
    session_data, created = EmotionSessionData.objects.get_or_create(user=request.user)

    print(f"Initial emotion_score: {session_data.emotion_score}")
    print(f"Initial emotion_counts: {session_data.emotion_counts}")

    if request.method == 'POST':
        form = PHQ9Form(request.POST)
        if form.is_valid():
            form_score = sum(int(form.cleaned_data[q]) for q in form.cleaned_data)
            total_score = form_score + session_data.emotion_score

            # Determine depression status based on total score
            if total_score >= 20:
                result = "Severe Depression"
            elif total_score >= 15:
                result = "Moderately Severe Depression"
            elif total_score >= 10:
                result = "Moderate Depression"
            elif total_score >= 5:
                result = "Mild Depression"
            else:
                result = "Minimal or No Depression"

            video_camera.stop()

            # Get the dominant emotion
            dominant_emotion = max(session_data.emotion_counts, key=session_data.emotion_counts.get)

            # Save the result and dominant emotion
            TestResult.objects.create(
                user=request.user,
                phq9_score=form_score,
                total_score=total_score,
                Status=result,
                emotion_score=session_data.emotion_score,  # Save the overall emotion score
                emotions=session_data.emotion_counts  # Store all detected emotions and their counts
            )

            print(f"Final emotion_score: {session_data.emotion_score}")
            # Clear the session data from the database after saving
            session_data.delete()

            return render(request, 'app/result.html', {
                'score': total_score,
                'result': result,
                'emotion_score': session_data.emotion_score,
                'dominant_emotion': dominant_emotion
            })
    else:
        form = PHQ9Form()

    # Detect emotions and update session data in the database
    dominant_emotion = video_camera.detect_emotions()
    if dominant_emotion in ['sad', 'angry', 'disgust', 'fear']:
        session_data.emotion_score += 1

    if dominant_emotion in session_data.emotion_counts:
        session_data.emotion_counts[dominant_emotion] += 1
    else:
        session_data.emotion_counts[dominant_emotion] = 1

    session_data.save()

    return render(request, 'app/phq9_form.html', {
        'form': form,
        'emotion_score': session_data.emotion_score
    })





def book_consultation(request):
    if request.method == 'POST':
        form = ConsultationBookingForm(request.POST)
        if form.is_valid():
            # Extract data from the form
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            message = form.cleaned_data['message']

            # Optionally, save the data to a database or send an email here

            # Prepare context for confirmation page
            confirmation_context = {
                'first_name': first_name,
                'last_name': last_name,
                'email': email,
                'phone': phone,
                'date': date,
                'time': time,
                'message': message,
            }

            return render(request, 'app/confirmation.html', confirmation_context)  # Render confirmation page with data
    else:
        form = ConsultationBookingForm()
    
    return render(request, 'app/book_consultation.html', {'form': form})