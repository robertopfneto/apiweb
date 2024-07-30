from django.http import HttpResponseBadRequest
from django.shortcuts import get_object_or_404, redirect, render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProfessionSerializer, PersonSerializer
from .models import Profession, Person
from .forms import PersonForm, ProfessionForm  

#HOME PAGE

def api_home(request):
    return render(request, 'index.html')

def person_form(request):
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save()
            return redirect('person_list')
        else:
            return HttpResponseBadRequest("Invalid form data")
    else:
        professions = Profession.objects.all()
        return render(request, 'person_form.html', {'professions': professions})
    
def profession_form(request):
    if request.method == 'POST':
        form = ProfessionForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'profession_list.html', {'professions': Profession.objects.all()})
    else:
        form = ProfessionForm()
    return render(request, 'profession_form.html', {'form': form})

# Render HTML Templates
def profession_list_html(request):
    professions = Profession.objects.all()
    return render(request, 'profession_list.html', {'professions': professions})

def person_list_html(request):
    people = Person.objects.all()

    if not people:  # Verifica se não há pessoas cadastradas
        return render(request, 'error.html')
    
    return render(request, 'person_list.html', {'people': people})

def person_detail_html(request, pk):
    person = get_object_or_404(Person, pk=pk)
    profession_name = person.fk_profession.name if person.fk_profession else "N/A"
    return render(request, 'person_detail.html', {'person': person, 'profession_name': profession_name})

#Profession view for list

# Profession List and Create View
@api_view(['GET', 'POST'])
@permission_classes(())
def profession_list(request):
    if request.method == 'GET':
        professions = Profession.objects.all()
        serializer = ProfessionSerializer(professions, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProfessionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Profession Detail, Update, and Delete View
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes(())
def profession_detail(request, pk):
    profession = get_object_or_404(Profession, pk=pk)
    if request.method == 'GET':
        serializer = ProfessionSerializer(profession)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProfessionSerializer(profession, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        profession.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Person List and Create View
@api_view(['GET', 'POST'])
@permission_classes(())
def person_list(request):
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Person Detail, Update, and Delete View
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes(())
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    profession_name = person.fk_profession.name if person.fk_profession else "N/A"
    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

