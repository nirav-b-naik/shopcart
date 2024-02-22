from django.contrib import messages
from django.shortcuts import redirect, render
from electronics.form import MobileForm
from electronics.methods import check_offer
from electronics.models import Mobile


def home(request):
    return render(request, "layout/home.html")


def mobile_master(request):
    mobile = Mobile.objects.all()  # Correct the model name
    offered, not_offered = check_offer(mobile)
    offered_form, not_offered_form = MobileForm(), MobileForm()
    offered_form.instances = offered
    not_offered_form.instances = not_offered

    return render(
        request,
        "mobile/mobile-master.html",
        {"offered_form": offered_form, "not_offered_form": not_offered_form},
    )


def add_mobile(request):
    form = MobileForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mobile details saved.!")
        return redirect("/mobile-master")

    return render(request, "mobile/add-mobile.html", {"form": form})


def edit_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    form = MobileForm(request.POST or None, instance=mobile)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mobile details updated.!")
        return redirect("/mobile-master")

    return render(request, "mobile/add-mobile.html", {"form": form})


def delete_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    mobile.delete()
    messages.success(request, "Mobile details Deleted.!")
    return redirect("/mobile-master")
