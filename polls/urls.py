from django.urls import path
from . import views
<<<<<<< HEAD
app_name= 'polls'

urlpatterns = [
        path('', views.index, name='index'),
        path('<int:question_id>/detail/', views.detail, name='detail'),
        path('<int:question_id>/results/', views.results, name='results'),
        path('<int:question_id>/vote/', views.vote, name='vote')
]
=======
app_name = 'polls'

### Generic view (class-based view)
urlpatterns=[
    path('', views.IndexView.as_view(), name='index'),
    # ex: /polls/5/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # ex: /polls/5/results.
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
>>>>>>> d93dcd757aa16030377cf7fbdc0c23a154f4442d
