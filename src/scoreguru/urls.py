from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from scoreguru.views import LoginView, CreateAccountView, LogoutView
from scoreguru.views import IndexView, ScoreboardView
from scoreguru.views import set_language


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('set-language/', set_language, name='set_language'),
    path('scoreboard/', ScoreboardView.as_view(), name='scoreboard'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', CreateAccountView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password-change/', PasswordChangeView.as_view(
        template_name='scoreguru/password_change.html',
        success_url=reverse_lazy('index')
    ), name='password_change'),
]


if settings.DEBUG: 
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)