from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from jobs.models import Job

from .forms import ApplicationForm
from .models import Application


@login_required
def apply_for_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if request.method == "POST":

        form = ApplicationForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            application = form.save(commit=False)

            application.user = request.user
            application.job = job

            application.save()

            return redirect(
                "application_success"
            )

    else:
        form = ApplicationForm()

    return render(
        request,
        "applications/apply.html",
        {
            "form": form,
            "job": job,
        }
    )

def application_success(request):

    return render(
        request,
        "applications/success.html"
    )

from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .models import Application


@login_required
def my_applications(request):

    applications = Application.objects.filter(
        user=request.user
    ).select_related("job").order_by("-created_at")

    return render(
        request,
        "applications/my_applications.html",
        {"applications": applications}
    )

