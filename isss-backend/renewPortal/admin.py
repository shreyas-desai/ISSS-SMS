from django.contrib import admin
from django.apps import apps
# Register your models here.
app = apps.get_app_config('renewPortal')

custom_models = []
for model_name, model in app.models.items():
    # print(model_name)
    if not model_name in custom_models:
        admin.site.register(model)
