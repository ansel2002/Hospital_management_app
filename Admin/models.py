from django.db import models
from django.db import models
from django.contrib.auth.models import User

from django.db import models
from django.contrib.auth.models import User

departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

lab_work_required=[('Complete Blood Count', 'Complete Blood Count'),
          ('Basic Metabolic Panel', 'Basic Metabolic Panel'),
          ('Comprehensive Metabolic Panel','Comprehensive Metabolic Panel'),
          ('Lipid Panel', 'Lipid Panel'),
          ('Thyroid Stimulating Hormone', 'Thyroid Stimulating Hormone'),
          ('Hemoglobin', 'Hemoglobin'),
          ('Urinalysis', 'Urinalysis'),
          ('Cultures', 'Cultures')]

company=[('Aetna','Aetna'),
('Cigna','Cigna'),
('Anthem','Anthem'),
('UHG','UHG'),
('Humana','Humana')
]

class Doctor(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
    status=models.BooleanField(default=False)
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)

    remaining=models.PositiveIntegerField(null=False)


