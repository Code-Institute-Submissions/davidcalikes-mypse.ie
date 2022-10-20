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
    path('validate_pupil_id/', views.ValidatePupilId.as_view(), name='validate_pupil_id'),
    path('add_passport/', views.AddPassport.as_view(), name='add_passport'),
    path('passport_list/', views.PassportList.as_view(), name='passport_list'),
    path('passport_detail/<slug:slug>/', views.PassportDetail.as_view(), name='passport_detail'),
    path('update_passport/<int:pk>', views.UpdatePassport.as_view(), name='update_passport'),
    path('delete_passport/<int:pk>', views.DeletePassport.as_view(), name='delete_passport'),
    path('teacher_passport_list/', views.TeacherPassportList.as_view(), name='teacher_passport_list'),
    path('teacher_validate_pupil_id/', views.TeacherValidatePupilId.as_view(), name='teacher_validate_pupil_id'),
    path('teacher_passport_detail/<slug:slug>/', views.TeacherPassportDetail.as_view(), name='teacher_passport_detail'),
    path('pupil_check', views.PupilCheck.as_view(), name='pupil_check'),
]
