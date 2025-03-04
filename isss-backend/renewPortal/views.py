from datetime import datetime
import math
import re

from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from django.views.decorators.csrf import csrf_exempt
from bs4 import BeautifulSoup

from rest_framework.response import Response

from .models import Address, AuthDocument, BulkCSV, Email, ProfileDocument, Student, StudentDocuments, WorkAuthorizations
from django.template import loader
from django.shortcuts import get_object_or_404, redirect, render
from .forms import AddressForm, BulkCSVForm, ContactForm, EmailForm, InteractionsForm, ProfileDocumentForm, ProfileForm, StudentDocumentsForm, StudentForm, DependentForm, WorkAuthDocumentForm, WorkAuthForm
from .serializer import AddressSerializer
from .models import address_types,countries

# Create your views here.
def index(request):
    template = loader.get_template("renewPortal/mainMenu.html")
    return HttpResponse(template.render(context={}, request=request))

def paginate_queryset(queryset, page=1, limit=10):
    if not queryset:
        return [], 0, None, None, None, None

    total_items = queryset.count()

    if not total_items:
        return [], 0, None, None, None, None

    total_pages = math.ceil(total_items / limit)
    start = (page - 1) * limit
    end = start + limit if start + limit < total_items else total_items

    prev_page = page - 1 if page > 1 else None
    next_page = page + 1 if page < total_pages else None

    return queryset[start:end], total_items, prev_page, next_page, total_pages, limit


@api_view(["GET"])
@permission_classes((permissions.AllowAny,))
def record_navigator_api(request):
    query = request.GET.get('query', '')
    field = request.GET.get('field', 'first_name')
    page = int(request.GET.get('page', 1))
    limit = int(request.GET.get('limit', 10))
    if query:
        filter_kwargs = {f"{field}__icontains": query}
        results = Student.objects.filter(**filter_kwargs)
    else:
        results = Student.objects.all()

    student_list, student_count, prev_page, next_page, total_pages, limit = paginate_queryset(results, page, limit)


    if student_list:
        student_json_list = []

        for m in student_list:
            student = m.get_data_json()
            student_json_list.append(student)

        data = {
            'data': student_json_list,
            'prev_page': prev_page,
            'next_page': next_page,
            'count': student_count,
            "total_pages":total_pages,
            "limit":limit
        }
        return Response(data, status=status.HTTP_200_OK)
    return Response({'data': [], 'message': "No Student Found!"}, status=status.HTTP_200_OK)


def record_navigator(request):
    return render(request,"renewPortal/recordNavigator.html")

def record_detail(request, record_id):
    record = get_object_or_404(Student, id=record_id)
    contacts = record.contacts.all()
    emails = record.emails.all()
    addresses = record.addresses.all()
    dependents = record.dependent.all()
    profiles = record.profiles.all()
    work_auths = record.authorizations.all()
    stud_docs = record.documents.all()
    interactions = record.interactions.all()
    # for doc in stud_docs:
    #     print(doc.documents)
    if profiles:
        ind_profile = profiles[0]
    else:
        ind_profile = None

    for address in addresses:
        address.form = AddressForm(instance=address)
    add_address_form = AddressForm()
    add_dependent_form = DependentForm()
    add_contact_form =ContactForm()
    add_profile_form = ProfileForm()
    add_document_form = ProfileDocumentForm()
    add_work_auth_form = WorkAuthForm()
    add_work_auth_doc_form = WorkAuthDocumentForm()
    add_student_document_form = StudentDocumentsForm()
    add_interactions_form = InteractionsForm()

    
    template = loader.get_template("renewPortal/recordDetail.html")
    context = {
        'record': record,
        #lits
        'addresses': addresses,
        'dependents':dependents,
        'emails':emails,
        'contacts':contacts,
        'profiles':profiles,
        'profile':ind_profile,
        'countries':countries,
        'address_types':address_types,
        'work_auths':work_auths,
        "stud_docs":stud_docs,
        "interactions":interactions,
        #forms
        'add_work_auth_form':add_work_auth_form,
        'add_work_auth_doc_form':add_work_auth_doc_form,
        'add_address_form': add_address_form,
        'add_dependent_form':add_dependent_form,
        "add_contact_form":add_contact_form,
        'add_profile_form':add_profile_form,
        "add_document_form":add_document_form,
        "add_student_document_form":add_student_document_form,
        "add_interactions_form":add_interactions_form,
    }
    template = loader.get_template("renewPortal/recordDetail.html")
    return HttpResponse(template.render(context, request))

@api_view(["PUT"])
@permission_classes((permissions.AllowAny,))
def edit_address(request, address_id):
    address = get_object_or_404(Address, id=address_id)
    if request.method == "PUT":
        # print(address)
        data = request.data.dict()
        data["student"] = address.student_address.id
        # print(data)
        form = AddressSerializer(instance=address, data=data)
        if form.is_valid():
            xyz = form.save()
            data['address_type'] = xyz.get_address_type_display()
            data['country'] = xyz.get_country_display()
            return Response(data, status=status.HTTP_200_OK)
        else:
            return Response(form.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({},status=status.HTTP_400_BAD_REQUEST)

def add_address(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    if request.method == "POST":
        form = AddressForm(request.POST)
        if form.is_valid():
            # Assign the student to the new address
            address = form.save(commit=False)
            address.student_address = student
            address.save()
            return redirect('record_detail', record_id=record_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('record_detail', kwargs={'record_id': record_id})))

def add_dependent(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    if request.method == "POST":
        form = DependentForm(request.POST)
        if form.is_valid():
            # Assign the student to the new dependent
            dependent = form.save(commit=False)
            dependent.student_dependent = student
            dependent.save()
            return redirect('record_detail', record_id=record_id)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('record_detail', kwargs={'record_id': record_id})))

def add_contact(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.student_contact = student
            contact.save()
            return redirect('record_detail', record_id=record_id)

def add_email(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    if request.method == "POST":
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            email.student_emails = student
            email.save()
            return redirect('record_detail', record_id=record_id)
        
@csrf_exempt
def add_profile(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    try:
        if request.method == "POST":
            profile_form = ProfileForm(request.POST)
            doc_form = ProfileDocumentForm(request.POST, request.FILES)
            if profile_form.is_valid() and doc_form.is_valid():
                profile = profile_form.save(commit=False)
                profile.student_profile = student
                profile.save()
                if request.FILES["doc_file"]:
                    for file in request.FILES.getlist('doc_file'):
                        ProfileDocument.objects.create(profile = profile, doc_file=file, name=file)
                return redirect('record_detail', record_id=record_id)
            else:
                print(profile_form.errors)
                print(doc_form.errors)
    except Exception as e:
        print(e)
        
@csrf_exempt
def add_work_auth(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    try:
        if request.method == "POST":
            work_auth = WorkAuthForm(request.POST)
            doc_form = WorkAuthDocumentForm(request.POST, request.FILES)
            if work_auth.is_valid() and doc_form.is_valid():
                work_auth = work_auth.save(commit=False)
                work_auth.student_auth = student
                work_auth.save()
                if request.FILES["doc_file"]:
                    for file in request.FILES.getlist('doc_file'):
                        AuthDocument.objects.create(work_auth = work_auth, doc_file=file, name=file)
                return redirect('record_detail', record_id=record_id)
            else:
                print(work_auth.errors)
                print(doc_form.errors)
    except Exception as e:
        print(e)
        
@csrf_exempt
def add_document(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    try:
        if request.method == "POST":
            doc_form = StudentDocumentsForm(request.POST, request.FILES)
            req_body = request.POST
            # print(req_body, request.FILES["doc_file"])
            if doc_form.is_valid():
                if request.FILES["doc_file"]:
                    for doc_file in request.FILES.getlist('doc_file'):
                        StudentDocuments.objects.create(student_docs=student,doc_file=doc_file,title=req_body["title"], keywords=req_body["keywords"],uploaded_by=req_body["uploaded_by"], context=req_body["context"])
                return redirect('record_detail', record_id=record_id)
            else:
                print(doc_form.errors)
    except Exception as e:
        print(e)
        
@csrf_exempt
def add_interactions(request, record_id):
    student = get_object_or_404(Student, id=record_id)
    try:
        if request.method == "POST":
            interactions_form = InteractionsForm(request.POST)
            req_body = request.POST
            # print(req_body)
            if interactions_form.is_valid():
                interactions = interactions_form.save(commit=False)
                interactions.student_interactions = student
                interactions.save()
                # if request.FILES["doc_file"]:
                #     for doc_file in request.FILES.getlist('doc_file'):
                #         StudentDocuments.objects.create(student_docs=student,doc_file=doc_file,title=req_body["title"], keywords=req_body["keywords"],uploaded_by=req_body["uploaded_by"], context=req_body["context"])
                return redirect('record_detail', record_id=record_id)
            else:
                # print(work_auth.errors)
                print(interactions_form.errors)
    except Exception as e:
        print(e)
        
@csrf_exempt
def add_record(request):
    if request.method == 'POST':
        student_form = StudentForm(request.POST)
        if student_form.is_valid():
            student = student_form.save()
            emails = request.POST.getlist('emails')
            email_types = request.POST.getlist('email_types')
            for email, email_type in zip(emails, email_types):
                if email:  
                    Email.objects.create(
                        student_emails=student,
                        email_address=email,
                        email_type=email_type
                    )
            return redirect('record_detail', record_id=student.id)
    else:
        student_form = StudentForm()
    template = loader.get_template("renewPortal/addRecord.html")
    return HttpResponse(template.render({'student_form': student_form}, request))


def reformat_date(date_str):
    if date_str=="":
        date_str="9/30/2022"
    try:
        return datetime.strptime(date_str, '%m/%d/%Y').strftime('%Y-%m-%d')
    except ValueError:
        return date_str
        

def extract_cwid(value):
    try:
        # Replace non-breaking spaces and strip extra whitespace
        if '\xa0' in value:
            cleaned_value = value.replace('\xa0', ' ').strip()
            return cleaned_value.split(" ")[0]
        elif '-' in value:
            cleaned_value = value.replace('-', '').strip()
            return cleaned_value.split(" ")[0]
    except Exception as e:
        print(f"Error processing CWID: {value}. Details: {e}")
        return None


@csrf_exempt
def add_bulk_records(request):
    shreyas_record = Student.objects.get(pk=1)
    rest = Student.objects.exclude(pk=shreyas_record.pk)
    rest.delete()
    table_data = []  # List to hold extracted table data

    if request.method == 'POST':
        file_form = BulkCSVForm(request.POST, request.FILES)
        
        if file_form.is_valid():
            for file in request.FILES.getlist('csv_file'):
                # Read the uploaded file as plain text
                file_content = file.read().decode('utf-8')

                # Parse the file content using BeautifulSoup
                soup = BeautifulSoup(file_content, 'html.parser')

                # Extract table data from the HTML
                tables = soup.find_all('table')  # Adjust if needed
                if tables:
                    data_table = tables[1]  # Assuming the second table contains the data
                    rows = data_table.find_all('tr')

                    # Extract rows and cells
                    for row in rows[1:]:
                        cells = row.find_all(['td', 'th'])
                        row_data = [cell.get_text(strip=True) for cell in cells]
                        # print(row_data)
                        table_data.append(row_data)
                        
                        cwid = extract_cwid(row_data[16])
                        # .split(" ")[0]
                        try:
                            Student.objects.create(passport_name=row_data[0],passport_last_name=row_data[1],passport_first_name=row_data[2],last_name=row_data[1],first_name=row_data[2],passport_middle_name=row_data[3],passport_name_suffix=row_data[5],passport_primary_name=row_data[7],passport_secondary_name=row_data[8],preferred_name=row_data[9],preferred_last_name=row_data[10],preferred_first_name=row_data[11],preferred_middle_name=row_data[12],preferred_name_suffix=row_data[14],sevis_id = row_data[15],cwid=cwid,db_status=True if row_data[19]=='Active' else False, department=row_data[20],data_link = True if row_data[21]=='TRUE' else False, email_alerts=True if row_data[22]=='TRUE' else False,date_of_birth=reformat_date(row_data[23]) if row_data[23]!="" else None, city_of_birth=row_data[24], country_of_birth=row_data[26], citizenship_status=row_data[28],country_of_birth_reason=row_data[30],gender='M' if row_data[32]=='Male' else 'F',country_of_citizenship = row_data[34], marital_status=row_data[36],country_of_residence=row_data[38],tax_id=row_data[39],ssn=row_data[40],drivers_license_no=row_data[41],drivers_license_state=row_data[43],create_date=reformat_date(row_data[45]) if row_data[45]!="" else None)
                        except Exception as e:
                            print(row_data)
                            print(e)
            return redirect('record_navigator')

            # Optionally, process or store `table_data` as needed
            # e.g., save records to the database or pass them to the template
    else:
        file_form = BulkCSVForm()
    
    # template = loader.get_template("renewPortal/addBulkRecords.html")
    context = {
        'file_form': file_form,
        'table_data': table_data,
    }
    return render(request, 'renewPortal/addBulkRecords.html', context)
# def add_bulk_records(request):
#     if request.method == 'POST':
#         file_form = BulkCSVForm(request.POST,request.FILES)
#         print(request.FILES)
#         if file_form.is_valid():
#             if request.FILES["csv_file"]:
#                 for csv in request.FILES.getlist('csv_file'):
#                     BulkCSV.objects.create(csv_file=csv)
#     else:       
#         file_form = BulkCSVForm()
#     template = loader.get_template("renewPortal/addBulkRecords.html")
#     return HttpResponse(template.render({'file_form': file_form}, request))





def custom_404_view(request, exception):
    return render(request, 'renewPortal/404.html', status=404)

def task_manager(request):
    return render(request, 'renewPortal/taskManager.html')

def report_writer(request):
    return render(request, 'renewPortal/reportWriter.html')

def campus_datalink(request):
    return render(request, 'renewPortal/campusDatalink.html')


