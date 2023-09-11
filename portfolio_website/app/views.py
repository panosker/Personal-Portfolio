from django.shortcuts import render, redirect
from .models import Myproject, Contribproject
from .forms import ContactForm
from .encryption import encrypt, decrypt


def about(request):
    return render(request, "about.html")


def myprojectView(request):
    projects = Myproject.objects.all()
    contribprojects = Contribproject.objects.all()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    else:
        form = ContactForm()
    context = {
        "projects": projects,
        "contribprojects": contribprojects,
        "contact_form": form,
    }
    return render(request, "main.html", context)


def action(request):
    if request.method == "POST":
        selected_action = request.POST.get("action")
        return render(
            request, "demo/encryption.html", {"selected_action": selected_action}
        )
    return render(request, "demo/encryption.html")


def encrypted(request):
    if request.method == "POST":
        text = request.POST.get("text")
        encrypted_text = encrypt(text)
        return render(
            request,
            "demo/encryption.html",
            {
                "text": text,
                "encrypted_text": encrypted_text,
                "selected_action": "encrypt",
            },
        )
    return render(request, "demo/encryption.html")


def decrypted(request):
    if request.method == "POST":
        text = request.POST.get("text")
        decrypted_text = decrypt(text)
        return render(
            request,
            "demo/encryption.html",
            {
                "text": text,
                "decrypted_text": decrypted_text,
                "selected_action": "decrypt",
            },
        )
    return render(request, "demo/encryption.html")
