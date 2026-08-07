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

    PROFESSION_CHOICES = [
        ("Student", "Student"),
        ("Entrepreneur", "Entrepreneur"),
        ("Working Professional", "Working Professional"),
        ("Government Employee", "Government Employee"),
        ("Teacher / Faculty", "Teacher / Faculty"),
        ("Doctor", "Doctor"),
        ("Engineer", "Engineer"),
        ("Lawyer", "Lawyer"),
        ("Farmer", "Farmer"),
        ("Business Owner", "Business Owner"),
        ("Social Worker / NGO", "Social Worker / NGO"),
        ("Political Worker", "Political Worker"),
        ("Other", "Other"),
    ]

    AGE_CHOICES = [
        ("18", "18"),
        ("19", "19"),
        ("20", "20"),
        ("21", "21"),
        ("22", "22"),
        ("23", "23"),
        ("24", "24"),
        ("25", "25"),
        ("26", "26"),
        ("27", "27"),
        ("28", "28"),
        ("29", "29"),
        ("30", "30"),
        ("31", "31"),
        ("32", "32"),
        ("33", "33"),
        ("34", "34"),
        ("35", "35"),
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

    age = models.CharField(
        max_length=2,
        choices=AGE_CHOICES,
    )

    educational_qualification = models.CharField(
        max_length=50,
        choices=QUALIFICATION_CHOICES,
    )

    profession = models.CharField(
        max_length=50,
        choices=PROFESSION_CHOICES,
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