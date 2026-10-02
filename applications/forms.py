from django import forms

from .models import Application


class ApplicationForm(forms.ModelForm):

    class Meta:
        model = Application

        fields = [
            "full_name",
            "email",
            "phone",
            "education",
            "experience",
            "skills",
            "cover_letter",
            "resume",
        ]

        widgets = {
            "experience": forms.Textarea(attrs={"rows": 4}),
            "skills": forms.Textarea(attrs={"rows": 4}),
            "cover_letter": forms.Textarea(attrs={"rows": 6}),
        }

    def clean_resume(self):
        resume = self.cleaned_data["resume"]

        allowed_types = [
            "application/pdf",
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
        ]

        if resume.content_type not in allowed_types:
            raise forms.ValidationError(
                "Only PDF, DOC, and DOCX files are allowed."
            )

        return resume
