from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
class NewLogoutView(LogoutView):
    pass
