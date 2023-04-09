from django.shortcuts import render,redirect
from django.views.generic import CreateView
from .forms import RegisterCreateForm,ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

class RegisterView(CreateView):
    form_class =RegisterCreateForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        login(self.request,self.object)
        return reverse_lazy('list')
@login_required
def edit_profile(request):
    if request.method== 'POST':
        form=ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            redirect('profile')
    form = ProfileForm(instance=request.user)
    return render(request,'profile.html',{
        'form':form
    })


