from django.shortcuts import render
from .forms import PersonaForm


# Create your views here.
def persona_form(request):
    if request.method == 'POST':
        form = PersonaForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = PersonaForm()
    return render(request, 'form_persona.html', {'form': form})