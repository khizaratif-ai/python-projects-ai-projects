from django.shortcuts import render, redirect

from .forms import LeaveApplicationForm
from .email_utils import send_leave_emails


def home(request):
    return render(request, "home.html")


def apply_leave(request):
    if request.method == "POST":
        form = LeaveApplicationForm(request.POST)

        if form.is_valid():
            send_leave_emails(form.cleaned_data)
            return redirect("success")
    else:
        form = LeaveApplicationForm()

    return render(request, "apply_leave.html", {"form": form})


def success(request):
    return render(request, "success.html")