from django.contrib import admin
from .models import Registration
import csv
from django.http import HttpResponse

def export_all_csv(modeladmin, request, queryset):
    response = HttpResponse(content_type="text/csv")
    response["Content-Disposition"] = 'attachment; filename="registrations.csv"'

    writer = csv.writer(response)

    writer.writerow([
        "Full Name",
        "Date of Birth",
        "Gender",
        "Address",
        "Pincode",
        "District",
        "State",
        "Aadhaar Number",
        "Educational Qualification",
        "Phone Number",
        "Email",
        "Facebook ID",
        "Instagram ID",
        "UTR Number",
        "Payment Status",
        "Created At",
    ])

    # Ignore queryset and export ALL registrations
    for reg in Registration.objects.all().order_by("-created_at"):
        writer.writerow([
            reg.full_name,
            reg.date_of_birth,
            reg.gender,
            reg.address,
            reg.pincode,
            reg.district,
            reg.state,
            reg.aadhaar_number,
            reg.educational_qualification,
            reg.phone_number,
            reg.email,
            reg.facebook_id,
            reg.instagram_id,
            reg.utr_number,
            reg.payment_status,
            reg.created_at,
        ])

    return response


export_all_csv.short_description = "Export ALL registrations as CSV"


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = (
        "full_name",
        "phone_number",
        "email",
        "district",
        "payment_status",
        "created_at",
    )

    search_fields = (
        "full_name",
        "phone_number",
        "email",
    )

    list_filter = (
        "payment_status",
        "district",
        "state",
        "educational_qualification",
    )

    actions = [export_all_csv]

