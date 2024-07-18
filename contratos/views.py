from django.shortcuts import render, redirect
from django.views.generic import ListView,CreateView,UpdateView, DeleteView
from typing import Any
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import *
from .forms import *
# Create your views here.

class listContrato(CreateView):
    pass

