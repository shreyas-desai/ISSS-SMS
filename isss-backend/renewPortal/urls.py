from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", views.index, name="main_menu"),
    path('record-navigator/', views.record_navigator, name='record_navigator'),
    path('record-detail/<int:record_id>/', views.record_detail, name='record_detail'),
    path('task-manager/', views.task_manager, name='task_manager'),
    path('report-writer/', views.report_writer, name='report_writer'),
    path('campus-datalink/', views.campus_datalink, name='campus_datalink'),
    path('add-record/', views.add_record, name='add_record'),
    path('add-bulk-records/', views.add_bulk_records, name='add_bulk_records'),
    path('edit-address/<int:address_id>/', views.edit_address, name='edit_address'),
    path('add-address/<int:record_id>/', views.add_address, name='add_address'),
    path('add-dependent/<int:record_id>/', views.add_dependent, name='add_dependent'),
    path('add-contact/<int:record_id>/', views.add_contact, name='add_contact'),
    path('add-profile/<int:record_id>/', views.add_profile, name='add_profile'),
    path('add-work-auth/<int:record_id>/', views.add_work_auth, name='add_work_auth'),
    path('add-document/<int:record_id>/', views.add_document, name='add_document'),
    path('add-interactions/<int:record_id>/', views.add_interactions, name='add_interactions'),
    #API
    path('api/record-navigator/', views.record_navigator_api, name='record_navigator_api'),
    # static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
]
