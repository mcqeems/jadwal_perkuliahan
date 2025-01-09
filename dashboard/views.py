from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from .models import mahasiswa, jadwal
from datetime import datetime
from .forms import jadwalForm

@login_required(login_url='login_user')
def index(request):
        if request.user.is_staff:
                return redirect('dosen')
        else:
                user_name = request.user.username
                first_name = request.user.first_name
                last_name = request.user.last_name
                hari = {
                        'Monday': 'Senin',
                        'Tuesday': 'Selasa',
                        'Wednesday': 'Rabu',
                        'Thursday': 'Kamis',
                        'Friday': 'Jumat',
                        'Saturday': 'Sabtu',
                        'Sunday': 'Minggu'
                } 
                hari_ini = hari[datetime.now().strftime('%A')]
                jadwal_dashboard = jadwal.objects.filter(hari__iexact=hari_ini)
                message = None
                if not jadwal_dashboard:
                        message = f"Hari ini {hari_ini}, tidak ada jadwal." 
                return render(request, 'dashboard/index.html', {'jadwal_dashboard': jadwal_dashboard, 'message': message, 'user_name': user_name, 'first_name': first_name, 'last_name': last_name}) 

def jadwal_kuliah(request):
        first_name = request.user.first_name
        last_name = request.user.last_name
        jadwal_perkuliahan = jadwal.objects.all()
        return render(request, 'dashboard/jadwal.html', {'jadwal_perkuliahan': jadwal_perkuliahan, 'first_name': first_name, 'last_name': last_name}) 

def logout_user(request):
        logout(request)
        return redirect('login_user')

def dosen(request):
        user_name = request.user.username
        first_name = request.user.first_name
        last_name = request.user.last_name
        hari = {
                'Monday': 'Senin',
                'Tuesday': 'Selasa',
                'Wednesday': 'Rabu',
                'Thursday': 'Kamis',
                'Friday': 'Jumat',
                'Saturday': 'Sabtu',
                'Sunday': 'Minggu'
        } 
        hari_ini = hari[datetime.now().strftime('%A')]
        jadwal_dashboard = jadwal.objects.filter(hari__iexact=hari_ini).filter(dosen__icontains=first_name)
        message = None
        if not jadwal_dashboard:
                message = f"Hari ini {hari_ini}, tidak ada jadwal Mengajar." 
        return render(request, 'dashboard/dashboard_dosen.html', {'jadwal_dashboard': jadwal_dashboard, 'message': message, 'user_name': user_name, 'first_name': first_name, 'last_name': last_name})

def jadwal_dosen(request):
        first_name = request.user.first_name
        last_name = request.user.last_name
        jadwal_perkuliahan = jadwal.objects.filter(dosen__icontains=first_name)
        return render(request, 'dashboard/jadwal_dosen.html', {'jadwal_perkuliahan': jadwal_perkuliahan, 'first_name': first_name, 'last_name': last_name}) 

def edit_jadwal(request, id):
        data = get_object_or_404(jadwal, id=id)
        if request.method == 'POST':
                form = jadwalForm(request.POST, instance=data)
                if form.is_valid():
                        form.save()
                        return redirect('jadwal_dosen')
        else:
                form = jadwalForm(instance=data)
        return render(request, 'dashboard/edit_jadwal.html', {'form': form})