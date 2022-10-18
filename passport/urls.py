from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('login_success/', views.LoginSuccess, name='login_success'),
    path('add_enrolled_pupil/', views.AddEnrolledPupil.as_view(), name='add_enrolled_pupil'),
    path('enrolled_pupil_list/', views.EnrolledPupilList.as_view(), name='enrolled_pupil_list'),
    path('<int:pupil_id>/', views.EnrolledPupilRecord.as_view(), name='enrolled_pupil_record'),
    path('update/<int:pk>', views.UpdatePupilRecord.as_view(), name='update_pupil_record'),
    path('delete/<int:pk>', views.DeletePupilRecord.as_view(), name='delete_pupil_record'),
    path('passport_list/', views.PassportList.as_view(), name='passport_list'),
    path('<slug:slug>/', views.PassportDetail.as_view(), name='passport_detail'),
]
