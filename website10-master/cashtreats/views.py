from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .models import cashtreats
from application.models import databank
from friends.models import friends
from rest_framework import viewsets
from .serializers import rest

# Ensure to "PIP install stripe
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class restframe(viewsets.ModelViewSet):
    queryset = databank.objects.all()
    serializer_class = rest



def home(request):
    if request.GET.get('q'):
        q = request.GET.get('q')
        data = friends.objects.filter(address__icontains=q)

    return render(request, 'cashtreats/home.html', )

def terms(request):

    return render(request, 'cashtreats/terms.html', )


def about(request):
    return render(request, 'cashtreats/about.html', )

def policy(request):
    return render(request, 'cashtreats/policy.html', )

def services(request):
    return render(request, 'cashtreats/services.html', )

# Added by Godspower
def payment(request):
    Key = settings.STRIPE_PUBLISHABLE_KEY

    if request.method == 'POST':
        amount = int(request.POST['amount'])

        try:
    
            customer = stripe.Customer.create(
                email = request.POST.get('email'),
                name = request.POST.get('full_name'),
                description = "Payment",
                source=request.POST['stripeToken'],
            )

        except stripe.error.CardError as e:
            messages.error(request, 'There was an error charging your card, ensure ypu have sufficient funds')
            return redirect('payment')

        except stripe.error.RateLimitError as e:
            messages.error(request, 'Rate Error')
            return redirect('payment')

        except stripe.error.InvalidRequestError as e:
            messages.error(request, 'Invalid requestor!')
            return redirect('payment')

        except stripe.error.AuthenticationError as e:
            messages.error(request, 'Invalid API auth')
            return redirect('payment')

        except stripe.error.StripeError as e:
            messages.error(request, 'Stripe Error')
            return redirect('payment')

        except Exception as e:
            messages.error(request, 'Error paying with your card at the moment')
            return redirect('payment')

        charge = stripe.Charge.create(
            customer=customer,
            amount = int(amount) *100,
            currency = 'usd',
            description='payment',
        )

        transRetrive = stripe.Charge.retrieve(
            charge["id"],
            api_key='sk_test_51MZU2lDGd4yPq3jdwAyL0LD8LTu8yfsPg96iyhpKPZ7XikvpBIvDDiVHgdKFx4JTizWkc1MZyW82b0OmcTqMSQXv00lHquZLBH'
            )
        charge.save() # Uses the same API Key.

        messages.success(request, "Payment succesful!.")
        return redirect('/')

    return render(request, 'payment-demo.html', {
        'Key':Key,
    })



# def upload(request,user_id):
#     for afile in request.FILES.getlist('files'):
#         user = UserProfile.objects.get(user_id=user_id)
#         pic = UserProfile(request.POST or request.FILES)
#         pic.image = afile
#         pic.save()
#         redirect('upload')
#     else:
#
#         return render(request,'cashtreats/upload.html')
