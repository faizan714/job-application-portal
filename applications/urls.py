from django.urls import path

from .views import (
    apply_for_job,
    application_success,
    my_applications,
)


urlpatterns = [
    path(
        "apply/<int:job_id>/",
        apply_for_job,
        name="apply_for_job",
    ),

    path(
        "success/",
        application_success,
        name="application_success",
    ),

    path(
        "my-applications/",
        my_applications,
        name="my_applications",
    ),
]