from django import forms
from .models import Address, AuthDocument, BulkCSV, Contacts, Email, Interactions, ProfileDocument, Profiles, Student, Dependents, StudentDocuments, WorkAuthorizations


class StudentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    create_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    
    class Meta:
        model = Student
        fields = ['first_name', 'middle_name', 'last_name', 'cwid', 'sevis_id', 'date_of_birth', 'gender', 'phone_no',
                #   'profile_status',
                  'portal_access',
                  'sso',
                #   'stage_status',
                #   'profile_type',
                #   'profile_sub_type',
                  'country_of_citizenship',
                  'country_of_residence',
                  'country_of_birth',
                  'marital_status',
                  'city_of_birth',
                  'start_date',
                  'end_date',
                  'level_of_education',
                  'full_time_status',
                #   'academic_dept',
                #   'major',
                  'create_date',
                  'db_status',
                  'ssn']

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email_address', 'email_type']
        
class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['address_type', 'street', 'city', 'state', 'zip_code', 'country']
        
class DependentForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Dependents
        fields = ['first_name', 'middle_name', 'last_name', 'date_of_birth', 'country_of_birth', 'relationship', 'status']
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['contact_type', 'name', 'address', 'phone_no']
        
class ProfileForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Profiles
        fields = ['profile_type', 'profile_sub_type','profile_status','profile_sub_status','sponsorship','start_date','end_date','academic_dept','major',"current_profile"]

class ProfileDocumentForm(forms.ModelForm):
    doc_file = forms.FileField()
    doc_file.widget.attrs.update({"multiple":True,"required":False})
    class Meta:
        model = ProfileDocument
        fields = ['doc_file']
        
class WorkAuthForm(forms.ModelForm):
    start_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    end_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = WorkAuthorizations
        fields = ['auth_type','start_date','end_date','request_status','time_type','work_months']
        
class WorkAuthDocumentForm(forms.ModelForm):
    doc_file = forms.FileField()
    doc_file.widget.attrs.update({"multiple":True,"required":False})
    class Meta:
        model = AuthDocument
        fields = ['doc_file']
        
class StudentDocumentsForm(forms.ModelForm):
    doc_file = forms.FileField()
    doc_file.widget.attrs.update({"required":True})
    title = forms.CharField(max_length=200,label="Document Title",)
    class Meta:
        model = StudentDocuments
        fields = ['doc_file','title','keywords',"uploaded_by","context"]
        
class InteractionsForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    class Meta:
        model = Interactions
        fields = ['interaction_type','date','advisor','status','category','summary']
        
class BulkCSVForm(forms.ModelForm):
    csv_file = forms.FileField()
    csv_file.widget.attrs.update({"accept":".csv,.xlsx,.xls","required":True,"multiple":True})
    class Meta:
        model = BulkCSV
        fields = ["csv_file"]