from django.shortcuts import render
from datetime import datetime, timezone
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template.context_processors import csrf
from .models import User, Wish

