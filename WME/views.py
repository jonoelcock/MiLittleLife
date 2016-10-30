from django.http import HttpResponse
from django.template import loader
from django.http import Http404
from django.utils import timezone
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

from .forms import NameForm
from .models import Policyholder, Child, Bank, PolicyholderForm, ChildForm, BankForm
import json

class IndexView(generic.ListView):
    template_name = 'WME/contact.html'

##class ChildView(generic.ChildView):
##    model = Policyholder
##    template_name = 'WME/child.html'

def get_contact(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': # create a form instance and populate it with data from the request:
        get_contact = PolicyholderForm(request.POST) # check whether it's valid:

        if get_contact.is_valid():
            form = get_contact
            instance = form.save(commit=False)
            #instance.project = Policyholder.objects.get(title=offset)
            instance.save()

            return HttpResponseRedirect(reverse('WME:get_child',args=(instance.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PolicyholderForm()

    return render(request, 'WME/contact.html', {'form': form})

def get_child(request, policyholder_id):

    policyholder = get_object_or_404(Policyholder, pk=policyholder_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST': # create a form instance and populate it with data from the request:

        get_child = ChildForm(request.POST) # check whether it's valid:

        if get_child.is_valid():
            form = get_child
            instance = form.save(commit=False)
            instance.policyholder = policyholder
            instance.save()

            if 'action1' in request.POST:
                return HttpResponseRedirect(reverse('WME:get_child',args=(policyholder.id,)))
            elif 'action2' in request.POST:
                return HttpResponseRedirect(reverse('WME:get_bank',args=(policyholder.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ChildForm(initial = {'lastname':policyholder.lastname})

    return render(request, 'WME/child.html', {'form': form})

def get_bank(request, policyholder_id):

    policyholder = get_object_or_404(Policyholder, pk=policyholder_id)

    # if this is a POST request we need to process the form data
    if request.method == 'POST': # create a form instance and populate it with data from the request:

        get_bank = BankForm(request.POST) # check whether it's valid:
        bank = get_bank.instance

        if get_bank.is_valid():
            form = get_bank
            instance = form.save(commit=False)
            instance.policyholder = policyholder

            if 'action1' in request.POST:
                instance.accept = False
                instance.save()
                return HttpResponseRedirect(reverse('WME:get_disclosures',args=(bank.id,)))
            elif 'action2' in request.POST:
                instance.accept = True
                instance.save()
                return HttpResponseRedirect(reverse('WME:get_disclosures',args=(bank.id,)))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BankForm(initial = {'startDate':'2016-11-30'})

    return render(request, 'WME/bank.html', {'form': form})


def get_disclosures(request, bank_id):

    bank = get_object_or_404(Bank, pk=bank_id)

    if request.method == 'POST': # create a form instance and populate it with data from the request:

        get_disclosures = BankForm(request.POST)
##
##        if get_disclosures.is_valid():
##            return HttpResponseRedirect('jonoelcock.pythonanywhere/WME/contact/')

    else:

        return render(request, 'WME/disclosures.html',{'bank': bank})
