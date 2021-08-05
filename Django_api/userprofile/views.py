import random
import string

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render

# Create your views here.
from django.template.loader import render_to_string
from django.urls import reverse
from django.views.generic import UpdateView, CreateView

from userprofile.forms import NewAccountForm
from userprofile.models import UserExtend


class UpdateProfileView(LoginRequiredMixin, UpdateView):
    fields = ['first_name', 'last_name', 'email']
    model = User
    template_name = 'registration/new_account.html'

    def get_success_url(self):
        return reverse('aplicatie1:home')

class CreateNewUser(CreateView):
    form_class = NewAccountForm
    model = UserExtend
    template_name = 'registration/new_account.html'

    def get_success_url(self):
        psw = ''.join(
            random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits
                                         + string.punctuation)
            for _ in range(8))
        try:
            user_instance = User.objects.get(id=self.object.id)
            user_instance.set_password(psw)
            user_instance.save()
            content_email_user = f"Your username and password: {user_instance.username} {psw}"
            msg_html = render_to_string('emails/invite_user.html', {'content_email': str(content_email_user)})
            msg = EmailMultiAlternatives(subject='Invite', body=content_email_user, from_email='contact@test.ro',
                                         to=[user_instance.email])
            msg.attach_alternative(msg_html, 'text/html')
            msg.send()
        except Exception:
            pass
        return reverse('login')

