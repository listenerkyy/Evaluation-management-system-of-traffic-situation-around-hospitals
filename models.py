from django.db import models
from django.contrib.auth.hashers import make_password

class User(models.Model):
    uid = models.AutoField(primary_key=True)
    account = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    sex = models.BooleanField(null=True, blank=True)
    tel = models.CharField(max_length=20, null=True, blank=True)
    role = models.IntegerField()  # 1: 管理员, 2: 调研员, 3: 院方

    def save(self, *args, **kwargs):
        # 在保存用户时将密码哈希化
        if not self.pk:  # 仅在创建新用户时哈希密码
            self.password = make_password(self.password)
        super(User, self).save(*args, **kwargs)

class Hospital(models.Model):
    yid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, null=False)
    district = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.name

class GovernanceReport(models.Model):
    gid = models.AutoField(primary_key=True)
    district = models.CharField(max_length=255, null=False)
    hospital_name = models.CharField(max_length=255, null=False)
    appointment_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    appointment_rate = models.DecimalField(max_digits=5, decimal_places=2)
    precise_appointment_time = models.DecimalField(max_digits=5, decimal_places=2)
    parking_space_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    has_no_parking_line = models.BooleanField()
    has_pedestrian_facilities = models.BooleanField()
    has_speed_limit_signs = models.BooleanField()
    has_pedestrian_signs = models.BooleanField()
    has_enforcement_cameras = models.BooleanField()
    has_parking_guidance = models.BooleanField()
    manages_bike_parking = models.BooleanField()
    shares_parking_resources = models.BooleanField()
    has_illegal_parking = models.BooleanField()
    has_disorderly_parking = models.BooleanField()
    timely_data_submission = models.BooleanField()
    cooperates_with_survey = models.BooleanField()
    hospital_id = models.IntegerField()

    def __str__(self):
        return self.hospital_name


class SurveyReport(models.Model):
    sid = models.AutoField(primary_key=True)
    district = models.CharField(max_length=255, null=False)
    hospital_name = models.CharField(max_length=255, null=False)
    appointment_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    appointment_rate = models.DecimalField(max_digits=5, decimal_places=2)
    precise_appointment_time = models.DecimalField(max_digits=5, decimal_places=2)
    parking_space_ratio = models.DecimalField(max_digits=5, decimal_places=2)
    has_no_parking_line = models.BooleanField()
    has_pedestrian_facilities = models.BooleanField()
    has_speed_limit_signs = models.BooleanField()
    has_pedestrian_signs = models.BooleanField()
    has_enforcement_cameras = models.BooleanField()
    has_parking_guidance = models.BooleanField()
    manages_bike_parking = models.BooleanField()
    shares_parking_resources = models.BooleanField()
    has_illegal_parking = models.BooleanField()
    has_disorderly_parking = models.BooleanField()
    timely_data_submission = models.BooleanField()
    cooperates_with_survey = models.BooleanField()
    remarks = models.TextField()
    hospital_feedback = models.TextField()
    hospital_id = models.IntegerField()
    surveyor_id = models.IntegerField()

    def __str__(self):
        return self.hospital_name


