from django.shortcuts import render, get_object_or_404, redirect
from .models import Job
from .forms import ApplicationForm
import PyPDF2


def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'jobs/job_list.html', {'jobs': jobs})


def apply_job(request, job_id):
    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":
        form = ApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            application = form.save(commit=False)
            application.job = job

            resume_file = request.FILES['resume']

            pdf_reader = PyPDF2.PdfReader(resume_file)
            resume_text = ""

            for page in pdf_reader.pages:
                resume_text += page.extract_text()

            application.calculate_match_score(resume_text)

            application.save()

            return render(request, 'jobs/application_success.html', {'application': application})

    else:
        form = ApplicationForm()

    return render(request, 'jobs/apply_job.html', {'form': form, 'job': job})