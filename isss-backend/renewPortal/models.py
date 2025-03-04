from django.db import models
from django.core import serializers
genders = [("M", "Male"), ("F", "Female"), ("O", "Other")]
stages = [("check-in","Check In"),("continuing","Continuing"),("pre-arrival","Pre Arrival"),("post-grad","Postcompletion Graduated")]
marital_status = [('S',"Single"),("M","Married"),("W","Widowed")]
full_time_status = [('F',"Full Time"),("P","Part Time")]
academic_dept = [("sch","Scahefer"),("bus","Business")]
major = [("CS","Computer Science"),("MIS","Information Systems")]
address_types = [('P','Permanent'),('M',"Mailing"),('C',"Current")]
email_types = [('L','Local'),('P','Permanent')]
contact_types =[('P',"Personal"),('W',"Work"),("H","Home")]
current_profile = [('C',"Curernt"),("P","Past")]
authorization_types = [('C',"CPT"),("O","OPT")]
req_status = [('P',"Pending"),("A","Approved"),("R","Rejected"),("C","Cancelled")]
context_type = [('G',"General"),("S","Special")]


with open("D:\\personal-Shreyas\\ISSS SMS 1.0\\isss-project\\isss-backend\\renewPortal\\public\\data\\country.csv",'r') as file:
    countries = []
    lines = file.readlines()
    for i in range(1,len(lines)):
        data = lines[i].strip().split(',')
        countries.append((data[0],data[1]))
    

class Student(models.Model):
    first_name = models.CharField(max_length=200,null=True,blank=True)
    middle_name = models.CharField(max_length=200,null=True,blank=True)
    last_name = models.CharField(max_length=200,null=True,blank=True)
    
    preferred_first_name = models.CharField(max_length=200,null=True,blank=True)
    preferred_middle_name = models.CharField(max_length=200,null=True,blank=True)
    preferred_last_name = models.CharField(max_length=200,null=True,blank=True)
    preferred_name = models.CharField(max_length=200,null=True,blank=True)
    preferred_name_suffix = models.CharField(max_length=200,null=True,blank=True)
    
    
    passport_first_name = models.CharField(max_length=200,null=True,blank=True)
    passport_middle_name = models.CharField(max_length=200,null=True,blank=True)
    passport_last_name = models.CharField(max_length=200,null=True,blank=True)
    passport_name = models.CharField(max_length=200,null=True,blank=True)
    passport_name_suffix = models.CharField(max_length=200,null=True,blank=True)
    passport_primary_name = models.CharField(max_length=200,null=True,blank=True)
    passport_secondary_name = models.CharField(max_length=200,null=True,blank=True)
    
    
    cwid = models.IntegerField(blank=True, null=True)
    sevis_id = models.CharField(max_length=10,null=True,blank=True)
    # profile_type = models.CharField(max_length=10,)
    # profile_sub_type = models.CharField(max_length=10,)
    # profile_status = models.BooleanField()
    
    portal_access = models.BooleanField(null=True,blank=True)
    sso = models.BooleanField(null=True,blank=True)
    date_of_birth = models.DateField(null=True,blank=True)
    gender = models.CharField(max_length=10, choices=genders,null=True,blank=True)
    stage_status = models.CharField(max_length=30, choices=stages,null=True,blank=True)
    phone_no = models.CharField(max_length=20,null=True,blank=True)
    data_link = models.BooleanField(null=True,blank=True)
    email_alerts = models.BooleanField(null=True,blank=True)


    # email = models.EmailField(max_length=254)
    country_of_birth = models.CharField(max_length=10, choices=countries,null=True,blank=True)
    country_of_citizenship = models.CharField(max_length=10, choices=countries,null=True,blank=True)
    country_of_residence = models.CharField(max_length=10, choices=countries,null=True,blank=True)
    marital_status = models.CharField(max_length=10, choices=marital_status,null=True,blank=True)
    city_of_birth = models.CharField(max_length=64,null=True,blank=True)
    country_of_birth_reason = models.CharField(max_length=200,null=True,blank=True)
    citizenship_status = models.CharField(max_length=200,null=True,blank=True)
    
    # start_date = models.DateField()
    # end_date = models.DateField()
    level_of_education = models.CharField(max_length=10,null=True,blank=True)
    full_time_status = models.CharField(max_length=10,choices=full_time_status,null=True,blank=True)
    department = models.CharField(max_length=200,null=True,blank=True)
    # academic_dept = models.CharField(max_length=10,choices=academic_dept)
    # major = models.CharField(max_length=10,choices=major)
    create_date = models.DateField(null=True,blank=True)
    db_status = models.BooleanField(default=True,null=True,blank=True)
    ssn = models.CharField(max_length=9,null=True,blank=True)
    tax_id = models.CharField(max_length=200,null=True,blank=True)
    drivers_license_no = models.CharField(max_length=200,null=True,blank=True)
    drivers_license_state = models.CharField(max_length=200,null=True,blank=True)
    
    
    # def __str__(self):
    #     return str(self.first_name) + " " + str(self.last_name)

    def get_data_json(self):
        email = Email.objects.filter(student_emails=self).first()
        if email:
            email = email.email_address
        else:
            email = "N/A"
        # email = serializers.serialize('json',[email])
        student_data = {
            "id": self.id,
            "first_name": self.first_name,
            "middle_name": self.middle_name if self.middle_name else None,
            "last_name": self.last_name,
            "preferred_first_name": self.preferred_first_name,
            "preferred_middle_name": self.preferred_middle_name if self.preferred_middle_name else None,
            "preferred_last_name": self.preferred_last_name,
            "preferred_name":self.preferred_name,
            "preferred_name_suffix":self.preferred_name_suffix,
            "passport_first_name":self.passport_first_name,
            "passport_middle_name":self.passport_middle_name if self.passport_middle_name else None,
            "passport_last_name":self.passport_last_name,
            "passport_name":self.passport_name,
            "passport_name_suffix":self.passport_name_suffix,
            "passport_primary_name":self.passport_primary_name,
            "passport_secondary_name":self.passport_secondary_name,
            "full_name": str(self.first_name) + " " + str(self.last_name),
            "cwid": self.cwid,
            "sevis_id":self.sevis_id,
            "date_of_birth":self.date_of_birth,
            "gender":self.gender,
            "phone_no":self.phone_no,
            "email":email,
            "create_date":self.create_date,
            "sso":self.sso,
            "stage_status":self.stage_status,
            "tax_id":self.tax_id,
            "drivers_license_no":self.drivers_license_no,
            "drivers_license_state":self.drivers_license_state
        }
        return student_data


class Email(models.Model):
    student_emails = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='emails')
    email_address = models.EmailField(max_length=200)
    email_type =  models.CharField(max_length=10, choices=email_types, null=True)
    

class Address(models.Model):
    student_address = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='addresses')
    address_type = models.CharField(max_length=10, choices=address_types, null=True)
    street = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=10, null=True)
    country = models.CharField(max_length=100, choices=countries, null=True)
    
    # def __str__(self):
    #     return f"{self.address_type.capitalize()} Address for {self.student.first_name}"

class Dependents(models.Model):
    student_dependent = models.ForeignKey('Student', on_delete=models.CASCADE, related_name='dependent')
    first_name = models.CharField(max_length=200)
    middle_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    country_of_birth = models.CharField(max_length=10, choices=countries)
    relationship = models.CharField(max_length=10)
    status = models.BooleanField(default=True)
    
class Contacts(models.Model):
    student_contact = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='contacts')
    contact_type = models.CharField(max_length=10, choices=contact_types)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=20)
    
class Profiles(models.Model):
    student_profile = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='profiles')
    profile_type = models.CharField(max_length=10)
    profile_sub_type = models.CharField(max_length=10)
    profile_status = models.BooleanField()
    profile_sub_status = models.CharField(max_length=10)
    sponsorship = models.CharField(max_length=10)
    start_date = models.DateField()
    end_date = models.DateField()
    academic_dept = models.CharField(max_length=10,choices=academic_dept)
    major = models.CharField(max_length=10,choices=major)
    current_profile = models.CharField(max_length=10,choices=current_profile)
    # document = models.FileField(upload_to='documents/profiles/', blank=True, null=True)
    
class ProfileDocument(models.Model):
    profile = models.ForeignKey("Profiles", on_delete=models.CASCADE, related_name="documents")
    doc_file = models.FileField(upload_to='documents/profiles/')
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class WorkAuthorizations(models.Model):
    student_auth = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='authorizations')
    auth_type = models.CharField(max_length=10,choices=authorization_types)
    start_date = models.DateField()
    end_date = models.DateField()
    request_status = models.CharField(max_length=10,choices=req_status)
    time_type = models.CharField(max_length=10, choices=full_time_status)
    work_months = models.IntegerField()
    
class AuthDocument(models.Model):
    work_auth = models.ForeignKey("WorkAuthorizations", on_delete=models.CASCADE, related_name="auth_documents")
    doc_file = models.FileField(upload_to='documents/authorizations/')
    name = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    
class Custom(models.Model):
    sem_of_entry = models.CharField(max_length=10)
    registration = models.CharField(max_length=10)
    
class StudentDocuments(models.Model):
    student_docs = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='documents')
    doc_file = models.FileField(upload_to='documents/student_docs/')
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.CharField(max_length=200)
    context = models.CharField(max_length=10, choices=context_type)
    
class Interactions(models.Model):
    student_interactions = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='interactions')
    interaction_type = models.CharField(max_length=20)
    date = models.DateField()
    advisor = models.CharField(max_length=50)
    status = models.CharField(max_length=20)
    category = models.CharField(max_length=50)
    summary = models.CharField(max_length=200) 
    
# class Notes(models.Model):
#     student_notes = models.ForeignKey("Student", on_delete=models.CASCADE, related_name='notes')
      
class BulkCSV(models.Model):
    csv_file = models.FileField(upload_to='bulk/csv/')
    # title = models.CharField(max_length=200)
    