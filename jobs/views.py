from django.shortcuts import render
from .models import Jobs, OcrData

# Create your views here.
def job_list(request):
    jobs = Jobs.objects.all().select_related('job_id', )

    return render(request, 'jobs/jobs.html', {'jobs': jobs})