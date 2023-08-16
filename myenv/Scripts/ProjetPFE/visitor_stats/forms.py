from django import forms

class VisitorStatsForm(forms.Form):
    date = forms.DateField()
    time = forms.TimeField()
    duration = forms.IntegerField()
    location = forms.CharField(max_length=100)
    purpose = forms.ChoiceField(choices=(
      ('event', 'Participation in a specific event'),
      ('event', 'Visiting an exhibition'),
      ('conference', 'Participation in a conference'),
      ('other', 'Other'),  
    ))
    other_purpose = forms.CharField(required=False)
    source = forms.MultipleChoiceField(choices=(
        ('online', 'Online advertisement'),
        ('social_media', 'Social media'),
        ('recommendation', 'Recommendation from a friend or colleague'),
        ('physical_ad', 'Physical signage/advertisement'),
        ('other_source', 'Other'),
    ))
    other_source_text = forms.CharField(required=False)