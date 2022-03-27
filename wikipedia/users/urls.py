from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [path('register', views.register, name="register"),
               path('', views.profile, name='profile'),
               path('changepassword',
                    auth_views.PasswordChangeView.as_view(template_name='wikipedia/changepassword.html',
                                                          success_url='/profile'), name='changepassword'),
               path('edit', views.profile_edit, name='edit'),
               path('test', views.ProfileUpdate.as_view(), name="test"),
               path('<int:pk>/delete', views.UserDeleteView.as_view(), name='delete'),
               path('view/<int>', views.OutsideProfileView.as_view(), name='outside_profile_overview'),
               path('privacy', views.UserPrivacyView.as_view(), name='user_privacy'),
               ]
