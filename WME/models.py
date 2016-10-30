import datetime

from django.db import models
from django.forms import ModelForm
from django.utils.encoding import python_2_unicode_compatible
from django.utils import timezone

RELATION = (
('Mother', 'Mother'),
('Father', 'Father'),
)

BANK = (
('', ''),
('ABSA', 'ABSA'),
('Bidvest', 'Bidvest'),
('Capitec', 'Capitec'),
('FNB', 'FNB'),
('Investec', 'Investec'),
('Nedbank', 'Nedbank'),
('Standard', 'Standard'),
('Other', 'Other'),
)

#Models

class Policyholder (models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    DOB = models.DateField(max_length=30)
    relation = models.CharField(max_length=20, default = 'Mother', choices=RELATION)
    cell = models.CharField(max_length=30, default = '0')
    email = models.CharField(max_length=100, default = '')
    def __int__(self):
        return self.firstname

class Child (models.Model):
    policyholder = models.ForeignKey(Policyholder, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    DOB = models.DateField(max_length=30)
    UW = models.BooleanField(max_length=30)
    def __str__(self):
        return self.firstname

class Bank (models.Model):
    policyholder = models.ForeignKey(Policyholder, on_delete=models.CASCADE)
    bankname = models.CharField(max_length=30, default = '', choices=BANK)
    accno = models.DecimalField(max_digits=15, decimal_places=0)
    branch = models.DecimalField(max_digits=6, decimal_places=0)
    startDate = models.DateField(max_length=30)
    accept = models.BooleanField(max_length=3, default = False)
    def __str__(self):
        return self.accno

#Forms

class PolicyholderForm(ModelForm):
    class Meta:
        model = Policyholder
        exclude = ()
        #fields = ['firstname', 'lastname', 'DOB','relation']

class ChildForm(ModelForm):
    class Meta:
        model = Child
        exclude = ('policyholder',)

class BankForm(ModelForm):
    class Meta:
        model = Bank
        exclude = ('policyholder','accept')

# Create your models here.
