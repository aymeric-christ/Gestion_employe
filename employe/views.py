from django.shortcuts import render , redirect , get_object_or_404
from .models import Employe
from .forms import EmployeForm
# Create your views here.

def list_employe(request):
    employe = Employe.objects.all()
    return render(request, "employe/list_employe.html", {"employes" : employe})

def ajouter_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_employe')
    return render(request, 'employe/formulaire.html',{'form': form})

def modifier_employe(request, id):
    employe = get_object_or_404(Employe, id=id)
    form = EmployeForm(request.POST or None, instance=employe)
    if form.is_valid():
        form.save()
        return redirect('liste_employe')
    return render(request, 'employe/formulaire.html',{'form': form})

def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id) 
    if request.method == "POST":
        employe.delete()
        return redirect('liste_employe')
    return render(request, 'employe/confirmer_suppression.html', {'employe' : employe})

