from django.shortcuts import render,get_object_or_404,redirect
from .models import Impression
from .forms import ImpressionBasicForm,ImpressionCreateForm1,ImpressionCreateForm2,ImpressionCreateForm3,ImpressionCreateForm4
#from django.views import generic

def get_next_by_pk(self):
    return type(self).objects.filter(pk__gt=self.pk).order_by('pk').first()

def thanks(request):
    return render(request,'impression/thanks.html')

def start(request):
    #latest_person=Impression.objects.filter().order_by('-id')[0]
    #print(latest_person)
    if request.method =='POST':
        latest_pk=Impression.objects.order_by("id").last()
        new_pk=latest_pk.pk+1
        latest_person,created=Impression.objects.get_or_create(pk=new_pk)
        url='/impression/create/' + str(latest_person.pk)
        return redirect(to=url)
    return render(request,'impression/start.html')
def impression_create(request,pk):
    person =Impression.objects.get(pk=pk)
    form = ImpressionBasicForm(request.POST or None,instance=person)
    if  request.method == 'POST'and form.is_valid():
        form.save()
        return redirect('impression:number1',pk=pk)

    context = {
        'form': form
    }
    #return redirect('impression:thanks')
    return render(request,'impression/impression_form.html',context)

def number1(request,pk):
    person =Impression.objects.get(pk=pk)
    form = ImpressionCreateForm1(request.POST or None,instance=person)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('impression:number2',pk=pk)

    context = {
        'form': form
    }
    #return redirect('impression:thanks')
    return render(request,'impression/form1.html',context)

def number2(request,pk):
    person =Impression.objects.get(pk=pk)
    form = ImpressionCreateForm2(request.POST or None,instance=person)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('impression:thanks')

    context = {
        'form': form
    }
    #return redirect('impression:thanks')
    return render(request,'impression/form2.html',context)

    