from django.db import models


class Registration(models.Model):

    GENDER_CHOICES = [
        ("Male", "Male"),
        ("Female", "Female"),
        ("Other", "Other"),
    ]

    QUALIFICATION_CHOICES = [
        ("Intermediate", "Intermediate"),
        ("Diploma", "Diploma"),
        ("Degree", "Degree"),
        ("B.Tech", "B.Tech"),
        ("M.Tech", "M.Tech"),
        ("MBA", "MBA"),
        ("MCA", "MCA"),
        ("Other", "Other"),
    ]

    PAYMENT_STATUS = [
        ("Pending", "Pending"),
        ("Verified", "Verified"),
        ("Rejected", "Rejected"),
    ]

    full_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)

    address = models.TextField()
    pincode = models.CharField(max_length=10)
    district = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    aadhaar_number = models.CharField(max_length=12)

    educational_qualification = models.CharField(
        max_length=50,
        choices=QUALIFICATION_CHOICES,
    )

    phone_number = models.CharField(max_length=15)
    email = models.EmailField()

    facebook_id = models.CharField(max_length=255, blank=True)
    instagram_id = models.CharField(max_length=255, blank=True)

    utr_number = models.CharField(max_length=30, blank=True, null=True)

    payment_status = models.CharField(
        max_length=20,
        choices=PAYMENT_STATUS,
        default="Pending",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name