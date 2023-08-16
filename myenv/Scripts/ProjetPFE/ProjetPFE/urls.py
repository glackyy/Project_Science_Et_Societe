app_name = 'main'
from django.contrib import admin
from django.urls import path
from main.views import home, register, login_view, search_view, update_page
from visitor_stats.views import collect_visitor_stats

urlpatterns = [
    path('update_page/<int:page_id>/', update_page, name='update_page'),  # Add a trailing slash at the end
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('search/', search_view, name='search'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('collect-stats/', collect_visitor_stats, name='collect_stats')
]
