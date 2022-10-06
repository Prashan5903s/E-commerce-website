from django.shortcuts import render
from datetime import datetime
from home.models import Contact

def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, "index.html", context)
def contact(request):
    return render(request, "contact.html")

def about(request):
    return render(request, "about.html")

def services(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        issue = request.POST.get("issue")
        contact = Contact(name=name, email=email, phone=phone, issue=issue, date=datetime.today())
        contact.save()
    def _str_(self):
        return self.name