from django.shortcuts import redirect, render
from .forms import RegistrationForm
from .models import Registration
from datetime import datetime



def home(request):
    day_one_sessions = [
        {
            "number": "Session 1",
            "title": "India's Civilisational Journey & Partition",
            "topics": [
                "Freedom Struggle",
                "Partition",
                "Constitution Making",
                "Nation Building",
            ],
        },
        {
            "number": "Session 2",
            "title": "India Before 2014 & After 2014",
            "topics": [
                "Governance Reforms",
                "Missed Opportunities",
                "National Security",
                "India's Rise on the Global Stage",
            ],
        },
        {
            "number": "Session 3",
            "title": "Global Leader - Insights from Prime Minister",
            "topics": [
                "Narendra Modi's Leadership",
                "Crisis Management",
                "Governance Reforms",
                "Lessons for Future Political Leaders",
            ],
        },
        {
            "number": "Session 4",
            "title": "Youth Open Mic & Leadership Dialogue",
            "topics": [
                "Interactive discussion with national leaders",
                "Politics and Governance",
                "Public Leadership",
                "Youth Participation",
            ],
        },
    ]

    day_two_sessions = [
        {
            "number": "Session 5",
            "title": "Women Leading India's Transformation",
            "topics": [
                "Women's Leadership",
                "Political Participation",
                "Entrepreneurship",
                "Governance",
                "Public Service",
            ],
        },
        {
            "number": "Achievers' Session",
            "title": "Pathways to Viksit Bharat",
            "topics": [
                "Agriculture",
                "Entrepreneurship",
                "Sports",
                "Medicine",
                "Law",
                "Public Service",
                "Innovation",
                "Environment",
                "Space",
                "Arts",
            ],
        },
        {
            "number": "Session 7",
            "title": "Youth & Their Role in Shaping Politics",
            "topics": [
                "Youth Participation",
                "Elections",
                "Political Communication",
                "Social Media",
                "Grassroots Leadership",
            ],
        },
        {
            "number": "Session 8",
            "title": "Andhra Pradesh's Role in Viksit Bharat @2047",
            "topics": [
                "Amaravati",
                "Infrastructure Development",
                "Economic Growth",
                "Agriculture",
                "Fisheries",
                "IT & Innovation",
                "Ports & Logistics",
                "Cooperative Federalism",
            ],
        },
    ]

    context = {
        "registration_url": "/register/",
        "event_date_iso": "2026-08-22T09:00:00+05:30",
        "objectives": [
            "Build a grounded understanding of India's civilisational journey, freedom struggle, and the sacrifices of Partition.",
            "Enable evidence-based discussions on governance before and after 2014.",
            "Recognise and promote the role of women in political and public leadership.",
            "Equip youth with knowledge and confidence to actively participate in politics and public policy.",
            "Showcase Andhra Pradesh's role in achieving the vision of Viksit Bharat @2047.",
        ],
        "attendees": [
            "Young Political Leaders",
            "Social Entrepreneurs",
            "Youth Changemakers",
            "Women Leaders",
            "Civil Society",
            "Professionals",
        ],
        "day_one_sessions": day_one_sessions,
        "day_two_sessions": day_two_sessions,
        "outcomes": [
            "Develop a deeper understanding of India's democratic evolution.",
            "Learn leadership principles from experienced political leaders.",
            "Build networks with policymakers and public representatives.",
            "Strengthen commitment towards ethical and responsible leadership.",
            "Contribute actively to the vision of Viksit Bharat @2047.",
        ],
    }
    return render(request, "dialogue/home.html", context)



def register(request):

    if request.method == "POST":

        form = RegistrationForm(request.POST)

        if form.is_valid():

            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone_number"]

            if Registration.objects.filter(email=email).exists():
                form.add_error(
                    "email",
                    "This email is already registered."
                )

            if Registration.objects.filter(phone_number=phone).exists():
                form.add_error(
                    "phone_number",
                    "This phone number is already registered."
                )

            if form.errors:
                return render(
                    request,
                    "dialogue/register.html",
                    {"form": form},
                )

            data = form.cleaned_data.copy()
            data["date_of_birth"] = data["date_of_birth"].isoformat()
            request.session["registration_data"] = data
            return redirect("dialogue:payment")

    else:

        form = RegistrationForm()

    return render(
        request,
        "dialogue/register.html",
        {
            "form": form,
        },
    )


def payment(request):

    registration_data = request.session.get("registration_data")

    if not registration_data:
        return redirect("dialogue:register")

    if request.method == "POST":

        registration_data["date_of_birth"] = datetime.strptime(
            registration_data["date_of_birth"],
            "%Y-%m-%d"
        ).date()

        registration = Registration(**registration_data)

        registration.utr_number = request.POST.get("utr_number")

        registration.payment_status = "Pending"

        registration.save()

        request.session.pop("registration_data", None)

        request.session["registration_id"] = registration.id

        return redirect("dialogue:success")

    return render(
        request,
        "dialogue/payment.html",
        {
            "amount": 200,
            "upi_id": "kishanreddy16-2@oksbi",
        },
    )

def success(request):

    registration_id = request.session.get("registration_id")

    if not registration_id:
        return redirect("dialogue:home")

    return render(
        request,
        "dialogue/success.html",
        {
            "registration_id": registration_id,
        },
    )


