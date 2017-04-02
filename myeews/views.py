from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta


def index(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "index.html", context)


def past_hour_four_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_hour_four_plus.html", context)


def past_hour_two_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_hour_two_plus.html", context)


def past_hour_one_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_hour_one_plus.html", context)


def past_hour_all(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_hour_all.html", context)


def past_day_four_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_day_four_plus.html", context)


def past_day_two_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_day_two_plus.html", context)


def past_day_one_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_day_one_plus.html", context)


def past_day_all(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(1))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_day_all.html", context)


def past_seven_day_four_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(7))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_seven_day_four_plus.html", context)


def past_seven_day_two_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(7))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_seven_day_two_plus.html", context)


def past_seven_day_one_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(7))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_seven_day_one_plus.html", context)


def past_seven_day_all(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(7))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_seven_day_all.html", context)


def past_thirty_day_four_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(30))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_thirty_day_four_plus.html", context)


def past_thirty_day_two_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(30))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_thirty_day_two_plus.html", context)


def past_thirty_day_one_plus(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(30))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_thirty_day_one_plus.html", context)


def past_thirty_day_all(request):
    today = str(timezone.localtime(timezone.now()).date())
    finaldate = str(timezone.now().date() - timedelta(30))
    context = {
        'time_now': today,
        'past_day': finaldate
    }
    return render(request, "past_thirty_day_all.html", context)