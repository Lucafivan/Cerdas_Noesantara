from django.contrib import admin
from .models import SubscriptionPlan, Transaction

admin.site.register(SubscriptionPlan)
admin.site.register(Transaction)
