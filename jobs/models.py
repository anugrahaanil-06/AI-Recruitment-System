from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    skills_required = models.CharField(max_length=200)
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    match_score = models.FloatField(null=True, blank=True)

    def calculate_match_score(self, resume_text):
        job_skills = self.job.skills_required.lower().split(',')
        resume_text = resume_text.lower()

        matched = 0

        for skill in job_skills:
            if skill.strip() in resume_text:
                matched += 1

        if len(job_skills) > 0:
            self.match_score = (matched / len(job_skills)) * 100
        else:
            self.match_score = 0

    def __str__(self):
        return self.name