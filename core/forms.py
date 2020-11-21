from django import forms
from core.models import Habit, Record


class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = [
            'name',
            'metric',
            'target',
        ]


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = [
            'text',
            'completed',
        ]
