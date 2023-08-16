from django.shortcuts import render
from .forms import VisitorStatsForm

def collect_visitor_stats(request):
    if request.method == 'POST':
        form = VisitorStatsForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data['date']
            time = form.cleaned_data['time']
            duration = form.cleaned_data['duration']
            location = form.cleaned_data['location']
            purpose = form.cleaned_data['purpose']
            other_purpose = form.cleaned_data['other_purpose']
            source = form.cleaned_data['source']
            other_source_text = form.cleaned_data['other_source_text']
            return render(request, 'visitor_stats/success.html', {
                'date': date,
                'time': time,
                'duration': duration,
                'location': location,
                'purpose': purpose,
                'other_purpose': other_purpose,
                'source': source,
                'other_source_text': other_source_text,
            })
            
    else:
        form = VisitorStatsForm()
    return render(request, 'visitor_stats/collect_stats.html', {'form': form})

# Create your views here.
