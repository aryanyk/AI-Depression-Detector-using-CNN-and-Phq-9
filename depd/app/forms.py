
from django import forms
from .models import Profile
PHQ_CHOICES = [
    (0, 'Not at all'),
    (1, 'Several days'),
    (2, 'More than half the days'),
    (3, 'Nearly every day'),
]

class PHQ9Form(forms.Form):
    q1 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Little interest or pleasure in doing things?")
    q2 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Feeling down, depressed, or hopeless?")
    q3 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Trouble falling or staying asleep, or sleeping too much?")
    q4 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Feeling tired or having little energy?")
    q5 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Poor appetite or overeating?")
    q6 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Feeling bad about yourself or that you are a failure?")
    q7 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Trouble concentrating on things?")
    q8 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Moving or speaking so slowly that others could have noticed?")
    q9 = forms.ChoiceField(choices=PHQ_CHOICES, widget=forms.RadioSelect, label="Thoughts that you would be better off dead?")


# forms.py


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'first_name', 
            'last_name', 
            'image', 
            'email', 
            'date_of_birth', 
            'height', 
            'weight'
        ]
        


class ConsultationBookingForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=True)
    date = forms.DateField(widget=forms.SelectDateWidget(), required=True)
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}), required=True)
    message = forms.CharField(widget=forms.Textarea, required=False)
