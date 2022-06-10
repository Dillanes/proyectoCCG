from django.shortcuts import render, redirect, get_object_or_404
from uniformat.models import UFTCategorias, UFTNivel2, UFTNivel3, UFTNivel4
from uniformat.forms import UFTCategoriaForm, UFTNivel2Form, UFTNivel3Form, UFTNivel4Form
from django.db.models import Q


# Create your views here.

def nivel1(request):
    queryset = request.GET.get('buscar')
    UFTCategoriasList = UFTCategorias.objects.all()
    if queryset:
        UFTCategoriasList = UFTCategorias.objects.filter(
                Q(Codigo__icontains = queryset) | Q(descriSpa__icontains = queryset)
        ).distinct()
    
    return render(request, "uniformat/nivel1.html", {"UFTCategorias": UFTCategoriasList})

def nivel2(request, nivel1_id):
    queryset = request.GET.get('buscar')
    nivels2 = UFTNivel2.objects.filter(fk_UftCat=nivel1_id)
    if queryset:
        nivels2 = UFTNivel2.objects.filter( 
            Q(Codigo__icontains = queryset) | Q(descriSpa__icontains = queryset), fk_UftCat=nivel1_id
        ).distinct()
    return render(request, "uniformat/nivel2.html", {"UFTNivels2":nivels2,"nivel2_id": nivel1_id})

def nivel3(request, nivel2_id, nivel_ant):
    queryset = request.GET.get('buscar')
    nivels3 = UFTNivel3.objects.filter(fk_UftN2=nivel2_id)
    if queryset:
        nivels3 = UFTNivel3.objects.filter( 
            Q(Codigo__icontains = queryset) | Q(descriSpa__icontains = queryset), fk_UftN2=nivel2_id
        ).distinct()
    return render(request, "uniformat/nivel3.html", {"UFTNivels3":nivels3,"nivel3_id": nivel2_id, "nivel_ant": nivel_ant})

def nivel4(request, nivel3_id, nivel_ant, nivel_ant_ant):
    queryset = request.GET.get('buscar')
    nivels4 = UFTNivel4.objects.filter(fk_UftN3=nivel3_id)
    if queryset:
        nivels4 = UFTNivel4.objects.filter( 
            Q(Codigo__icontains = queryset) | Q(descriSpa__icontains = queryset), fk_UftN3=nivel3_id
        )
    return render(request, "uniformat/nivel4.html", {"UFTNivels4":nivels4,"nivel4_id": nivel3_id, "nivel_ant": nivel_ant, "nivel_ant_ant": nivel_ant_ant})

def agregarCategoria(request):
    if request.method == 'POST':
        formaCategoria = UFTCategoriaForm(request.POST)
        if formaCategoria.is_valid():
            formaCategoria.save()
            return redirect('Uniformat')
    else:
        formaCategoria = UFTCategoriaForm()

    return render(request, 'uniformat/nuevoCategoria.html', {'formaCategoria': formaCategoria})

def editarCategoria(request, id):
    categoria = get_object_or_404(UFTCategorias, pk=id)
    if request.method == 'POST':
        formaCategoria = UFTCategoriaForm(request.POST, instance=categoria)
        if formaCategoria.is_valid():
            formaCategoria.save()
            return redirect('Uniformat')
    else:
        formaCategoria = UFTCategoriaForm(instance=categoria)

    return render(request, 'uniformat/editarCategoria.html', {'formaCategoria': formaCategoria})

def eliminarCategoria(request, id):
    categoria = get_object_or_404(UFTCategorias, pk=id)
    if categoria:
        categoria.delete()
    return redirect('Uniformat')

#CRUD PARA EL NIVEL 2

def agregarNivel2(request, nivel1_id):
    if request.method == 'POST':
        formaNivel2 = UFTNivel2Form(request.POST)
        if formaNivel2.is_valid():
            formaNivel2.save()
            return redirect('nivel2', nivel1_id)
    else:
        formaNivel2 = UFTNivel2Form()

    return render(request, 'uniformat/nuevoNivel2.html', {'formaNivel2': formaNivel2, "nivel1_id": nivel1_id})

def eliminarNivel2(request, id, nivel1_id):
    nivel2 = get_object_or_404(UFTNivel2, pk=id)
    if nivel2:
        nivel2.delete()
    return redirect('nivel2', nivel1_id)

def editarNivel2(request, id, nivel1_id):
    nivel2 = get_object_or_404(UFTNivel2, pk=id)
    if request.method == 'POST':
        formaNivel2 = UFTNivel2Form(request.POST, instance=nivel2)
        if formaNivel2.is_valid():
            formaNivel2.save()
            return redirect('nivel2', nivel1_id)
    else:
        formaNivel2 = UFTNivel2Form(instance=nivel2)

    return render(request, 'uniformat/editarNivel2.html', {'formaNivel2': formaNivel2, "nivel1_id": nivel1_id})

#CRUD PARA EL NIVEL 3

def agregarNivel3(request, nivel2_id, nivel1_id):
    if request.method == 'POST':
        formaNivel3 = UFTNivel3Form(request.POST)
        if formaNivel3.is_valid():
            formaNivel3.save()
            return redirect('nivel3', nivel2_id, nivel1_id)
    else:
        formaNivel3 = UFTNivel3Form()

    return render(request, 'uniformat/nuevoNivel3.html', {'formaNivel3': formaNivel3, "nivel2_id": nivel2_id, "nivel1_id": nivel1_id})

def eliminarNivel3(request, id, nivel2_id, nivel1_id):
    nivel3 = get_object_or_404(UFTNivel3, pk=id)
    if nivel3:
        nivel3.delete()
    return redirect('nivel3', nivel2_id, nivel1_id)

def editarNivel3(request, id, nivel2_id, nivel1_id):
    nivel3 = get_object_or_404(UFTNivel3, pk=id)
    if request.method == 'POST':
        formaNivel3 = UFTNivel3Form(request.POST, instance=nivel3)
        if formaNivel3.is_valid():
            formaNivel3.save()
            return redirect('nivel3', nivel2_id, nivel1_id)
    else:
        formaNivel3 = UFTNivel3Form(instance=nivel3)

    return render(request, 'uniformat/editarNivel3.html', {'formaNivel3': formaNivel3, "nivel2_id": nivel2_id, "nivel1_id": nivel1_id})

    #CRUD PARA EL NIVEL 4

def agregarNivel4(request, nivel3_id, nivel2_id, nivel1_id):
    if request.method == 'POST':
        formaNivel4 = UFTNivel4Form(request.POST)
        if formaNivel4.is_valid():
            formaNivel4.save()
            return redirect('nivel4', nivel3_id, nivel2_id, nivel1_id)
    else:
        formaNivel4 = UFTNivel4Form()

    return render(request, 'uniformat/nuevoNivel4.html', {'formaNivel4': formaNivel4, "nivel3_id": nivel3_id,"nivel2_id": nivel2_id, "nivel1_id": nivel1_id})

def eliminarNivel4(request, id, nivel3_id, nivel2_id, nivel1_id):
    nivel4 = get_object_or_404(UFTNivel4, pk=id)
    if nivel4:
        nivel4.delete()
    return redirect('nivel4', nivel3_id, nivel2_id, nivel1_id)

def editarNivel4(request, id, nivel3_id, nivel2_id, nivel1_id):
    nivel4 = get_object_or_404(UFTNivel4, pk=id)
    if request.method == 'POST':
        formaNivel4 = UFTNivel4Form(request.POST, instance=nivel4)
        if formaNivel4.is_valid():
            formaNivel4.save()
            return redirect('nivel4', nivel3_id, nivel2_id, nivel1_id)
    else:
        formaNivel4 = UFTNivel4Form(instance=nivel4)

    return render(request, 'uniformat/editarNivel4.html', {'formaNivel4': formaNivel4, "nivel3_id": nivel3_id,"nivel2_id": nivel2_id, "nivel1_id": nivel1_id})