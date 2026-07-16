from django import forms


class LeaveApplicationForm(forms.Form):
    LEAVE_CHOICES = [
        ("Casual Leave", "Casual Leave"),
        ("Sick Leave", "Sick Leave"),
        ("Annual Leave", "Annual Leave"),
        ("Emergency Leave", "Emergency Leave"),
    ]

    employee_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your full name"
        })
    )

    employee_id = forms.CharField(
        max_length=20,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter employee ID"
        })
    )

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "Enter your email"
        })
    )

    department = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Enter department"
        })
    )

    leave_type = forms.ChoiceField(
        choices=LEAVE_CHOICES,
        widget=forms.Select(attrs={
            "class": "form-control"
        })
    )

    start_date = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        })
    )

    end_date = forms.DateField(
        widget=forms.DateInput(attrs={
            "class": "form-control",
            "type": "date"
        })
    )

    reason = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 5,
            "placeholder": "Reason for leave"
        })
    )

    def clean(self):
        cleaned_data = super().clean()

        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and end_date < start_date:
            raise forms.ValidationError(
                "End date cannot be earlier than start date."
            )

        return cleaned_data