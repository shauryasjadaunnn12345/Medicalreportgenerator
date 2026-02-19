from django import forms

class YBOCSForm(forms.Form):
    # Obsession-related questions
    obsession_time = forms.ChoiceField(
        label="How much time do obsessive thoughts occupy your mind?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate amount'), (3, 'A lot'), (4, 'Most of the time')]
    )
    obsession_interference = forms.ChoiceField(
        label="How much do obsessive thoughts interfere with your daily activities?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate interference'), (3, 'Severe interference'), (4, 'Extremely interfering')]
    )
    obsession_distress = forms.ChoiceField(
        label="How much distress do obsessive thoughts cause?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate distress'), (3, 'Severe distress'), (4, 'Extreme distress')]
    )
    obsession_resistance = forms.ChoiceField(
        label="How much do you try to resist the obsessive thoughts?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate resistance'), (3, 'Severe resistance'), (4, 'Extreme resistance')]
    )
    obsession_control = forms.ChoiceField(
        label="How much control do you have over the obsessive thoughts?",
        choices=[(0, 'Complete control'), (1, 'Some control'), (2, 'Moderate control'), (3, 'Little control'), (4, 'No control')]
    )

    # Compulsion-related questions
    compulsion_time = forms.ChoiceField(
        label="How much time do compulsive behaviors occupy your time?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate amount'), (3, 'A lot'), (4, 'Most of the time')]
    )
    compulsion_interference = forms.ChoiceField(
        label="How much do compulsive behaviors interfere with your daily activities?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate interference'), (3, 'Severe interference'), (4, 'Extremely interfering')]
    )
    compulsion_distress = forms.ChoiceField(
        label="How much distress do compulsive behaviors cause?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate distress'), (3, 'Severe distress'), (4, 'Extreme distress')]
    )
    compulsion_resistance = forms.ChoiceField(
        label="How much do you try to resist the compulsive behaviors?",
        choices=[(0, 'None'), (1, 'A little'), (2, 'Moderate resistance'), (3, 'Severe resistance'), (4, 'Extreme resistance')]
    )
    compulsion_control = forms.ChoiceField(
        label="How much control do you have over the compulsive behaviors?",
        choices=[(0, 'Complete control'), (1, 'Some control'), (2, 'Moderate control'), (3, 'Little control'), (4, 'No control')]
    )
from django import forms

GAD_CHOICES = [
    (0, 'Not at all'),
    (1, 'Several days'),
    (2, 'More than half the days'),
    (3, 'Nearly every day'),
]

class GAD7Form(forms.Form):
    q1 = forms.ChoiceField(choices=GAD_CHOICES, label="Feeling nervous, anxious or on edge", widget=forms.Select())
    q2 = forms.ChoiceField(choices=GAD_CHOICES, label="Not being able to stop or control worrying", widget=forms.Select())
    q3 = forms.ChoiceField(choices=GAD_CHOICES, label="Worrying too much about different things", widget=forms.Select())
    q4 = forms.ChoiceField(choices=GAD_CHOICES, label="Trouble relaxing", widget=forms.Select())
    q5 = forms.ChoiceField(choices=GAD_CHOICES, label="Being so restless that it is hard to sit still", widget=forms.Select())
    q6 = forms.ChoiceField(choices=GAD_CHOICES, label="Becoming easily annoyed or irritable", widget=forms.Select())
    q7 = forms.ChoiceField(choices=GAD_CHOICES, label="Feeling afraid as if something awful might happen", widget=forms.Select())

from django import forms

from django import forms

PHQ9_CHOICES = [
    ("0", "Not at all"),
    ("1", "Several days"),
    ("2", "More than half the days"),
    ("3", "Nearly every day"),
]

class PHQ9Form(forms.Form):
    q1 = forms.ChoiceField(
        label="Little interest or pleasure in doing things?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q2 = forms.ChoiceField(
        label="Feeling down, depressed, or hopeless?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q3 = forms.ChoiceField(
        label="Trouble falling or staying asleep, or sleeping too much?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q4 = forms.ChoiceField(
        label="Feeling tired or having little energy?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q5 = forms.ChoiceField(
        label="Poor appetite or overeating?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q6 = forms.ChoiceField(
        label="Feeling bad about yourself — or that you are a failure or have let yourself or your family down?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q7 = forms.ChoiceField(
        label="Trouble concentrating on things, such as reading the newspaper or watching television?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q8 = forms.ChoiceField(
        label="Moving or speaking so slowly that other people could have noticed? Or the opposite — being so fidgety or restless that you have been moving around a lot more than usual?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
    q9 = forms.ChoiceField(
        label="Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?",
        choices=PHQ9_CHOICES,
        widget=forms.Select()
    )
from django import forms

YES_NO_CHOICES = [('yes', 'Yes'), ('no', 'No')]
SEVERITY_CHOICES = [
    ('no', 'No problems'),
    ('minor', 'Minor problems'),
    ('moderate', 'Moderate problems'),
    ('serious', 'Serious problems')
]

class MDQForm(forms.Form):
    # 13 symptom questions
    q1 = forms.ChoiceField(label="Have there ever been times when you felt so good or hyper that others thought you were not your normal self?", choices=YES_NO_CHOICES, widget=forms.Select())
    q2 = forms.ChoiceField(label="Have there ever been times when you were so irritable that you shouted at people or started fights or arguments?", choices=YES_NO_CHOICES, widget=forms.Select())
    q3 = forms.ChoiceField(label="Have there ever been times when you felt much more self-confident than usual?", choices=YES_NO_CHOICES, widget=forms.Select())
    q4 = forms.ChoiceField(label="Have there ever been times when you got much less sleep than usual and found you didn't really miss it?", choices=YES_NO_CHOICES, widget=forms.Select())
    q5 = forms.ChoiceField(label="Have there ever been times when you were much more talkative or spoke faster than usual?", choices=YES_NO_CHOICES, widget=forms.Select())
    q6 = forms.ChoiceField(label="Have there ever been times when thoughts raced through your head or you couldn’t slow your mind down?", choices=YES_NO_CHOICES, widget=forms.Select())
    q7 = forms.ChoiceField(label="Have there ever been times when you were so easily distracted by things around you that you had trouble concentrating or staying on track?", choices=YES_NO_CHOICES, widget=forms.Select())
    q8 = forms.ChoiceField(label="Have there ever been times when you had much more energy than usual?", choices=YES_NO_CHOICES, widget=forms.Select())
    q9 = forms.ChoiceField(label="Have there ever been times when you were much more active or did many more things than usual?", choices=YES_NO_CHOICES, widget=forms.Select())
    q10 = forms.ChoiceField(label="Have there ever been times when you were much more social or outgoing than usual?", choices=YES_NO_CHOICES, widget=forms.Select())
    q11 = forms.ChoiceField(label="Have there ever been times when you were much more interested in sex than usual?", choices=YES_NO_CHOICES, widget=forms.Select())
    q12 = forms.ChoiceField(label="Have there ever been times when you did things that were unusual for you or that other people might have thought were excessive, foolish, or risky?", choices=YES_NO_CHOICES, widget=forms.Select())
    q13 = forms.ChoiceField(label="Have there ever been times when spending money got you or your family into trouble?", choices=YES_NO_CHOICES, widget=forms.Select())

    # Symptom overlap and impairment
    symptoms_occurred_together = forms.ChoiceField(
        label="If you checked YES to more than one of the above, have several of these ever happened during the same period of time?",
        choices=YES_NO_CHOICES,
        widget=forms.Select()
    )

    severity = forms.ChoiceField(
        label="How much of a problem did any of these cause you? (e.g., unable to work, made family or social life difficult)",
        choices=SEVERITY_CHOICES,
        widget=forms.Select()
    )
from django import forms

class PCL5Form(forms.Form):
    # 20 questions for PTSD based on the DSM-5 criteria using Select for dropdowns
    q1 = forms.ChoiceField(
        label="1. In the past month, how often have you been bothered by repeated, disturbing, and unwanted memories of the stressful experience?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q2 = forms.ChoiceField(
        label="2. In the past month, how often have you been bothered by repeated, disturbing dreams of the stressful experience?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q3 = forms.ChoiceField(
        label="3. In the past month, how often have you been bothered by suddenly feeling or acting as if the stressful experience were happening again (flashbacks)?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q4 = forms.ChoiceField(
        label="4. In the past month, how often have you been bothered by feeling upset or having physical reactions (e.g., heart racing, sweating) when something reminded you of the stressful experience?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q5 = forms.ChoiceField(
        label="5. In the past month, how often have you avoided thinking about or talking about the stressful experience, or avoided having feelings related to it?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q6 = forms.ChoiceField(
        label="6. In the past month, how often have you avoided activities or situations because they reminded you of the stressful experience?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q7 = forms.ChoiceField(
        label="7. In the past month, how often have you had trouble remembering important parts of the stressful experience?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q8 = forms.ChoiceField(
        label="8. In the past month, how often have you had negative thoughts about yourself, other people, or the world?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q9 = forms.ChoiceField(
        label="9. In the past month, how often have you blamed yourself or others for the stressful experience or what happened after it?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q10 = forms.ChoiceField(
        label="10. In the past month, how often have you had strong negative feelings such as fear, horror, anger, guilt, or shame?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q11 = forms.ChoiceField(
        label="11. In the past month, how often have you felt distant or cut off from other people?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q12 = forms.ChoiceField(
        label="12. In the past month, how often have you felt emotionally numb or detached from your surroundings?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q13 = forms.ChoiceField(
        label="13. In the past month, how often have you felt hopeless about the future?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q14 = forms.ChoiceField(
        label="14. In the past month, how often have you had trouble concentrating?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q15 = forms.ChoiceField(
        label="15. In the past month, how often have you been easily startled or frightened?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q16 = forms.ChoiceField(
        label="16. In the past month, how often have you felt tense or “on edge”?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q17 = forms.ChoiceField(
        label="17. In the past month, how often have you had difficulty falling or staying asleep?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q18 = forms.ChoiceField(
        label="18. In the past month, how often have you had angry outbursts or irritability?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q19 = forms.ChoiceField(
        label="19. In the past month, how often have you engaged in reckless or self-destructive behavior?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )

    q20 = forms.ChoiceField(
        label="20. In the past month, how often have you had trouble experiencing positive emotions?",
        choices=[(0, "Not at all"), (1, "A little bit"), (2, "Moderately"), (3, "Quite a bit"), (4, "Extremely")],
        widget=forms.Select,
    )
from django import forms

CHOICES = [
    ('0', 'Not at all'),
    ('1', 'A little'),
    ('2', 'Moderately'),
    ('3', 'Quite a bit'),
    ('4', 'Extremely'),
]

class SchizophreniaTestForm(forms.Form):
    q1 = forms.ChoiceField(
        label="Do you hear voices when no one is around?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q2 = forms.ChoiceField(
        label="Do you believe people are plotting against you?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q3 = forms.ChoiceField(
        label="Do you feel like your thoughts are being controlled?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q4 = forms.ChoiceField(
        label="Do you see things that others do not?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q5 = forms.ChoiceField(
        label="Do you find it difficult to organize your thoughts?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q6 = forms.ChoiceField(
        label="Do you avoid social interactions or isolate yourself?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q7 = forms.ChoiceField(
        label="Do you feel emotionally numb or detached?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q8 = forms.ChoiceField(
        label="Do you have trouble concentrating or remembering things?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q9 = forms.ChoiceField(
        label="Do you believe in unusual or magical ideas?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    q10 = forms.ChoiceField(
        label="Do you feel that your thoughts are being broadcast to others?",
        choices=CHOICES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
from django import forms

from django import forms

# ASRS Choices for Radio Buttons
ASRS_CHOICES = [
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('sometimes', 'Sometimes'),
    ('often', 'Often'),
    ('very_often', 'Very Often'),
]

# ASRS Form with Part A and Part B questions
class ASRSForm(forms.Form):
    # Part A: 6 Questions
    q1 = forms.ChoiceField(label="1. How often do you have trouble wrapping up the final details of a project?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(label="2. How often do you have difficulty getting things in order when you have to do a task that requires organization?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(label="3. How often do you have problems remembering appointments or obligations?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(label="4. When you have a task that requires a lot of thought, how often do you avoid or delay getting started?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(label="5. How often do you fidget or squirm with your hands or feet when you have to sit down for a long time?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(label="6. How often do you feel overly active and compelled to do things, like you were driven by a motor?", choices=ASRS_CHOICES, widget=forms.RadioSelect)

    # Part B: 12 Additional Questions (can be made optional)
    q7 = forms.ChoiceField(label="7. How often do you make careless mistakes when you have to work on a boring or difficult project?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(label="8. How often do you have difficulty concentrating on what people are saying to you, even when they are speaking to you directly?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(label="9. How often do you leave your seat in meetings or other situations in which you are expected to remain seated?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(label="10. How often do you feel restless or fidgety?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q11 = forms.ChoiceField(label="11. How often do you have difficulty relaxing?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q12 = forms.ChoiceField(label="12. How often do you talk excessively?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q13 = forms.ChoiceField(label="13. How often do you interrupt others when they are busy?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q14 = forms.ChoiceField(label="14. How often do you have difficulty waiting your turn?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q15 = forms.ChoiceField(label="15. How often do you feel like you are ‘on the go’ or ‘driven by a motor’?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q16 = forms.ChoiceField(label="16. How often do you blurt out answers before the question has been completed?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q17 = forms.ChoiceField(label="17. How often do you have difficulty following through with instructions and failing to finish activities?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q18 = forms.ChoiceField(label="18. How often do you avoid or dislike tasks that require sustained mental effort?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q19 = forms.ChoiceField(label="19. How often do you lose things necessary for tasks and activities (e.g., keys, glasses, paperwork, etc.)?", choices=ASRS_CHOICES, widget=forms.RadioSelect)
    q20 = forms.ChoiceField(label="20. How often do you get easily distracted by extraneous stimuli?", choices=ASRS_CHOICES, widget=forms.RadioSelect)

from django import forms

# AQ Test Choices
AQ_CHOICES = [
    ('0', 'Definitely Agree'),
    ('1', 'Slightly Agree'),
    ('2', 'Neither Agree nor Disagree'),
    ('3', 'Slightly Disagree'),
    ('4', 'Definitely Disagree'),
]

class AQTestForm(forms.Form):
    q1 = forms.ChoiceField(label="1. I prefer to do things the same way over and over again.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(label="2. I find it hard to make new friends.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(label="3. I enjoy doing things in a particular way, even if they are repetitive.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(label="4. I find it easy to read people’s facial expressions.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(label="5. I am not very good at understanding jokes.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(label="6. I prefer to stay at home rather than going out and meeting people.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(label="7. I enjoy social gatherings.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q8 = forms.ChoiceField(label="8. I find it difficult to understand the rules of social games.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q9 = forms.ChoiceField(label="9. I enjoy puzzles and problems.", choices=AQ_CHOICES, widget=forms.RadioSelect)
    q10 = forms.ChoiceField(label="10. I prefer activities that involve little social interaction.", choices=AQ_CHOICES, widget=forms.RadioSelect)

    # You can continue adding more questions as needed, up to 50 in total.
from django import forms

PANIC_CHOICES = [
    ('never', 'Never'),
    ('rarely', 'Rarely'),
    ('sometimes', 'Sometimes'),
    ('often', 'Often'),
    ('very_often', 'Very Often'),
]

class PanicDisorderForm(forms.Form):
    q1 = forms.ChoiceField(label="1. Do you experience sudden attacks of intense fear or discomfort?", choices=PANIC_CHOICES, widget=forms.RadioSelect)
    q2 = forms.ChoiceField(label="2. During a panic attack, do you experience a racing heart, sweating, trembling, or shortness of breath?", choices=PANIC_CHOICES, widget=forms.RadioSelect)
    q3 = forms.ChoiceField(label="3. Do you avoid certain places or situations for fear of triggering a panic attack?", choices=PANIC_CHOICES, widget=forms.RadioSelect)
    q4 = forms.ChoiceField(label="4. Do you feel a loss of control or a fear of dying during panic episodes?", choices=PANIC_CHOICES, widget=forms.RadioSelect)
    q5 = forms.ChoiceField(label="5. Do you worry about when your next panic attack might happen?", choices=PANIC_CHOICES, widget=forms.RadioSelect)
    q6 = forms.ChoiceField(label="6. Do panic attacks affect your ability to work or socialize?", choices=PANIC_CHOICES, widget=forms.RadioSelect)
    q7 = forms.ChoiceField(label="7. Do you feel anxious or afraid most of the time, even when not having a panic attack?", choices=PANIC_CHOICES, widget=forms.RadioSelect)

from django import forms

CHOICES = [
    ('Never', 'Never'),
    ('Rarely', 'Rarely'),
    ('Sometimes', 'Sometimes'),
    ('Often', 'Often'),
    ('Always', 'Always'),
]

class SleepDisorderForm(forms.Form):
    q1 = forms.ChoiceField(
        label="Do you have trouble falling asleep at night?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q2 = forms.ChoiceField(
        label="Do you wake up frequently during the night?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q3 = forms.ChoiceField(
        label="Do you feel tired or sleepy during the day?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q4 = forms.ChoiceField(
        label="Has anyone told you that you snore loudly or stop breathing while sleeping?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q5 = forms.ChoiceField(
        label="Do you wake up feeling unrefreshed despite a full night’s sleep?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q6 = forms.ChoiceField(
        label="Do you experience restless or twitching legs when trying to sleep?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q7 = forms.ChoiceField(
        label="Do you find it hard to concentrate due to lack of sleep?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q8 = forms.ChoiceField(
        label="Do you rely on caffeine or naps to get through the day?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q9 = forms.ChoiceField(
        label="Do you experience anxiety or dread around bedtime?",
        choices=CHOICES, widget=forms.RadioSelect
    )
    q10 = forms.ChoiceField(
        label="Do you feel that your sleep issues affect your daily life or mental health?",
        choices=CHOICES, widget=forms.RadioSelect
    )
from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms

class OTPVerificationForm(forms.Form):
    email = forms.EmailField(label="Email")
    otp = forms.CharField(label="OTP", max_length=6)

class CustomSignupForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, min_length=8)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        p1 = cleaned_data.get("password1")
        p2 = cleaned_data.get("password2")

        if p1 and p2 and p1 != p2:
            raise ValidationError("Passwords do not match.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 6}),
        }
