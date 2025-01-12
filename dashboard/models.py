from django.db import models

hari = (
    ("Senin", "Senin"),
    ("Selasa", "Selasa"),
    ("Rabu", "Rabu"),
    ("Kamis", "Kamis"),
    ("Jumat", "Jumat"),
    ("Sabtu", "Sabtu"),
    ("Minggu", "Minggu"),
)

# Create your models here.
class mahasiswa(models.Model):
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)
    semester = models.CharField(max_length=4)
    
    def __str__(self):
        return self.nim + ' - ' + self.nama + ' - ' + self.prodi + ' - ' + self.semester

class jadwal(models.Model):
    hari = models.CharField(max_length=10, choices=hari)
    jam = models.TimeField()
    matkul = models.CharField(max_length=50)
    dosen = models.CharField(max_length=75)
    ruang = models.CharField(max_length=30)
    semester = models.IntegerField(blank=False, null=False, choices = [(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8')])
    
    def __str__(self):
        return self.matkul + ' - ' + f"semester {self.semester}" + ' - ' + self.dosen
    
class mahasiswa_baru(models.Model):
    nim = models.CharField(max_length=10)
    nama = models.CharField(max_length=50)
    prodi = models.CharField(max_length=50)
    semester = models.CharField(max_length=4)
    rencana_studi = models.BooleanField(default=False)
    
    def __str__(self):
        return self.nim + ' - ' + self.nama + ' - ' + self.prodi + ' - ' + self.semester + ' - ' + self.rencana_studi