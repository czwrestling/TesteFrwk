from django.shortcuts import render
from .models import AlbunsPost
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.db.models import Sum, F
from django import forms
from .forms import AlbunsForm

# Create your views here.
@login_required
def albuns_lista(request):
    form1 = AlbunsPost.objects.all()
    return render(request, 'albuns.html', {'form1': form1})


def album_atualizacao(request,id):
    form1 = get_object_or_404(AlbunsPost, pk=id)
    form = AlbunsForm(request.POST or None, request.FILES or None,instance=form1)


    if form.is_valid():
        form.save()
        return redirect('albuns_lista')

    return render(request, 'albuns_edit.html', {'form':form})



def album_novo(request):

    form = AlbunsForm(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        form.save()
        return redirect('albuns_lista')

    return render(request,'album_novo.html', {'form':form})
