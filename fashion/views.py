from django.contrib import messages
from django.shortcuts import redirect, render
from django.views import View
from fashion.form import ShirtForm
from fashion.models import Shirt


class ShirtView(View):
    template_name = "shirt/shirt-master.html"

    def get(self, request):
        shirts = Shirt.objects.all()
        form = ShirtForm()
        form.instances = shirts
        return render(request, self.template_name, {"form": form})


class AddShirt(View):
    template_name = "shirt/add-shirt.html"

    def get(self, request):
        form = ShirtForm()
        return render(request, self.template_name, {"form": form})

    def post(self, request):
        form = ShirtForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Shirt added Successfully.")
            return redirect("/shirt-master")
        return render(request, self.template_name, {"form": form})


class EditShirt(View):
    template_name = "shirt/add-shirt.html"

    def get(self, request, id):
        shirt = Shirt.objects.get(id=id)
        form = ShirtForm(instance=shirt)
        return render(request, self.template_name, {"form": form, "shirt": shirt})

    def post(self, request, id):
        shirt = Shirt.objects.get(id=id)
        form = ShirtForm(request.POST, instance=shirt)
        if form.is_valid():
            form.save()
            messages.success(request, "Shirt updated Successfully.")
            return redirect("/shirt-master")
        return render(request, self.template_name, {"form": form, "shirt": shirt})


class DeleteShirt(View):
    def post(self, request, id):
        shirt = Shirt.objects.get(id=id)
        shirt.delete()
        messages.success(request, "Shirt deleted Successfully.")
        return redirect("/shirt-master")
