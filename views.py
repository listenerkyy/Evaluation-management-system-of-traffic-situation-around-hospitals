from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import check_password
import json
from .models import User
from .models import Hospital
from .models import GovernanceReport
from .models import SurveyReport


@csrf_exempt
def login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            account = data.get('account')
            password = data.get('password')

            try:
                user = User.objects.get(account=account)
            except User.DoesNotExist:
                return JsonResponse({'role': 0}, status=400)  # 用户不存在

            if check_password(password, user.password):
                return JsonResponse({'role': user.role})
            else:
                return JsonResponse({'role': 0}, status=400)  # 密码错误

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        users_list = list(users.values('uid', 'account', 'sex', 'tel', 'role'))
        return JsonResponse(users_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_hospitals(request):
    if request.method == 'GET':
        hospitals = Hospital.objects.all()
        hospitals_list = list(hospitals.values('yid', 'name', 'district', 'type'))
        return JsonResponse(hospitals_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt  # 允许跨站请求伪造保护
def add_hospital(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            name = data.get('name')
            district = data.get('district')
            type = data.get('type')

            # 创建新的 Hospital 对象
            hospital = Hospital(name=name, district=district, type=type)
            hospital.save()  # 将医院信息保存到数据库

            # 获取所有医院信息
            hospitals = Hospital.objects.all()
            hospitals_list = list(hospitals.values('yid', 'name', 'district', 'type'))

            return JsonResponse(hospitals_list, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def alter_hospital(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            yid = data.get('yid')
            name = data.get('name')
            district = data.get('district')
            type = data.get('type')

            # 查找要修改的 Hospital 对象
            try:
                hospital = Hospital.objects.get(yid=yid)
            except Hospital.DoesNotExist:
                return JsonResponse({'error': 'Hospital not found'}, status=404)

            # 修改 Hospital 对象的属性
            hospital.name = name
            hospital.district = district
            hospital.type = type
            hospital.save()  # 保存修改后的医院信息

            # 获取所有医院信息
            hospitals = Hospital.objects.all()
            hospitals_list = list(hospitals.values('yid', 'name', 'district', 'type'))

            return JsonResponse(hospitals_list, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt  # 允许跨站请求伪造保护
def delete_hospital(request, yid):
    if request.method == 'DELETE':
        try:
            # 查找并删除医院信息
            hospital = Hospital.objects.get(pk=yid)
            hospital.delete()
            return JsonResponse({'message': 'Hospital deleted successfully'}, status=200)
        except Hospital.DoesNotExist:
            return JsonResponse({'error': 'Hospital not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

def get_governance_reports(request):
    if request.method == 'GET':
        reports = GovernanceReport.objects.all()
        reports_list = list(reports.values(
            'gid', 'district', 'hospital_name', 'appointment_ratio', 'appointment_rate', 
            'precise_appointment_time', 'parking_space_ratio', 'has_no_parking_line', 
            'has_pedestrian_facilities', 'has_speed_limit_signs', 'has_pedestrian_signs', 
            'has_enforcement_cameras', 'has_parking_guidance', 'manages_bike_parking', 
            'shares_parking_resources', 'has_illegal_parking', 'has_disorderly_parking', 
            'timely_data_submission', 'cooperates_with_survey', 'hospital_id'
        ))
        return JsonResponse(reports_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def add_governance_report(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            district = data.get('district')
            hospital_name = data.get('hospital_name')
            appointment_ratio = data.get('appointment_ratio')
            appointment_rate = data.get('appointment_rate')
            precise_appointment_time = data.get('precise_appointment_time')
            parking_space_ratio = data.get('parking_space_ratio')
            has_no_parking_line = data.get('has_no_parking_line')
            has_pedestrian_facilities = data.get('has_pedestrian_facilities')
            has_speed_limit_signs = data.get('has_speed_limit_signs')
            has_pedestrian_signs = data.get('has_pedestrian_signs')
            has_enforcement_cameras = data.get('has_enforcement_cameras')
            has_parking_guidance = data.get('has_parking_guidance')
            manages_bike_parking = data.get('manages_bike_parking')
            shares_parking_resources = data.get('shares_parking_resources')
            has_illegal_parking = data.get('has_illegal_parking')
            has_disorderly_parking = data.get('has_disorderly_parking')
            timely_data_submission = data.get('timely_data_submission')
            cooperates_with_survey = data.get('cooperates_with_survey')
            hospital_id = data.get('hospital_id')

            # 创建新的 GovernanceReport 对象
            report = GovernanceReport(
                district=district,
                hospital_name=hospital_name,
                appointment_ratio=appointment_ratio,
                appointment_rate=appointment_rate,
                precise_appointment_time=precise_appointment_time,
                parking_space_ratio=parking_space_ratio,
                has_no_parking_line=has_no_parking_line,
                has_pedestrian_facilities=has_pedestrian_facilities,
                has_speed_limit_signs=has_speed_limit_signs,
                has_pedestrian_signs=has_pedestrian_signs,
                has_enforcement_cameras=has_enforcement_cameras,
                has_parking_guidance=has_parking_guidance,
                manages_bike_parking=manages_bike_parking,
                shares_parking_resources=shares_parking_resources,
                has_illegal_parking=has_illegal_parking,
                has_disorderly_parking=has_disorderly_parking,
                timely_data_submission=timely_data_submission,
                cooperates_with_survey=cooperates_with_survey,
                hospital_id=hospital_id
            )
            report.save()

            # 获取所有治理表信息
            reports = GovernanceReport.objects.all()
            reports_list = list(reports.values(
                'gid', 'district', 'hospital_name', 'appointment_ratio', 'appointment_rate', 
                'precise_appointment_time', 'parking_space_ratio', 'has_no_parking_line', 
                'has_pedestrian_facilities', 'has_speed_limit_signs', 'has_pedestrian_signs', 
                'has_enforcement_cameras', 'has_parking_guidance', 'manages_bike_parking', 
                'shares_parking_resources', 'has_illegal_parking', 'has_disorderly_parking', 
                'timely_data_submission', 'cooperates_with_survey', 'hospital_id'
            ))

            return JsonResponse(reports_list, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def alter_governance_report(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            hospital_id = data.get('hospital_id')

            # 查找需要修改的治理表记录
            try:
                report = GovernanceReport.objects.get(hospital_id=hospital_id)
            except GovernanceReport.DoesNotExist:
                return JsonResponse({'error': 'Report not found'}, status=404)

            # 更新治理表记录
            report.district = data.get('district', report.district)
            report.hospital_name = data.get('hospital_name', report.hospital_name)
            report.appointment_ratio = data.get('appointment_ratio', report.appointment_ratio)
            report.appointment_rate = data.get('appointment_rate', report.appointment_rate)
            report.precise_appointment_time = data.get('precise_appointment_time', report.precise_appointment_time)
            report.parking_space_ratio = data.get('parking_space_ratio', report.parking_space_ratio)
            report.has_no_parking_line = data.get('has_no_parking_line', report.has_no_parking_line)
            report.has_pedestrian_facilities = data.get('has_pedestrian_facilities', report.has_pedestrian_facilities)
            report.has_speed_limit_signs = data.get('has_speed_limit_signs', report.has_speed_limit_signs)
            report.has_pedestrian_signs = data.get('has_pedestrian_signs', report.has_pedestrian_signs)
            report.has_enforcement_cameras = data.get('has_enforcement_cameras', report.has_enforcement_cameras)
            report.has_parking_guidance = data.get('has_parking_guidance', report.has_parking_guidance)
            report.manages_bike_parking = data.get('manages_bike_parking', report.manages_bike_parking)
            report.shares_parking_resources = data.get('shares_parking_resources', report.shares_parking_resources)
            report.has_illegal_parking = data.get('has_illegal_parking', report.has_illegal_parking)
            report.has_disorderly_parking = data.get('has_disorderly_parking', report.has_disorderly_parking)
            report.timely_data_submission = data.get('timely_data_submission', report.timely_data_submission)
            report.cooperates_with_survey = data.get('cooperates_with_survey', report.cooperates_with_survey)

            report.save()

            # 获取所有治理表信息
            reports = GovernanceReport.objects.all()
            reports_list = list(reports.values(
                'gid', 'district', 'hospital_name', 'appointment_ratio', 'appointment_rate', 
                'precise_appointment_time', 'parking_space_ratio', 'has_no_parking_line', 
                'has_pedestrian_facilities', 'has_speed_limit_signs', 'has_pedestrian_signs', 
                'has_enforcement_cameras', 'has_parking_guidance', 'manages_bike_parking', 
                'shares_parking_resources', 'has_illegal_parking', 'has_disorderly_parking', 
                'timely_data_submission', 'cooperates_with_survey', 'hospital_id'
            ))

            return JsonResponse(reports_list, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def delete_governance_report(request, gid):
    if request.method == 'DELETE':
        try:
            report = GovernanceReport.objects.get(gid=gid)
            report.delete()
            return JsonResponse({'message': 'Report deleted successfully'}, status=204)
        except GovernanceReport.DoesNotExist:
            return JsonResponse({'error': 'Report not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def add_survey_report(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            district = data.get('district')
            hospital_name = data.get('hospital_name')
            appointment_ratio = data.get('appointment_ratio')
            appointment_rate = data.get('appointment_rate')
            precise_appointment_time = data.get('precise_appointment_time')
            parking_space_ratio = data.get('parking_space_ratio')
            has_no_parking_line = data.get('has_no_parking_line')
            has_pedestrian_facilities = data.get('has_pedestrian_facilities')
            has_speed_limit_signs = data.get('has_speed_limit_signs')
            has_pedestrian_signs = data.get('has_pedestrian_signs')
            has_enforcement_cameras = data.get('has_enforcement_cameras')
            has_parking_guidance = data.get('has_parking_guidance')
            manages_bike_parking = data.get('manages_bike_parking')
            shares_parking_resources = data.get('shares_parking_resources')
            has_illegal_parking = data.get('has_illegal_parking')
            has_disorderly_parking = data.get('has_disorderly_parking')
            timely_data_submission = data.get('timely_data_submission')
            cooperates_with_survey = data.get('cooperates_with_survey')
            remarks = data.get('remarks')
            hospital_feedback = data.get('hospital_feedback')
            hospital_id = data.get('hospital_id')
            surveyor_id = data.get('surveyor_id')

            # 创建新的 SurveyReport 对象
            report = SurveyReport(
                district=district,
                hospital_name=hospital_name,
                appointment_ratio=appointment_ratio,
                appointment_rate=appointment_rate,
                precise_appointment_time=precise_appointment_time,
                parking_space_ratio=parking_space_ratio,
                has_no_parking_line=has_no_parking_line,
                has_pedestrian_facilities=has_pedestrian_facilities,
                has_speed_limit_signs=has_speed_limit_signs,
                has_pedestrian_signs=has_pedestrian_signs,
                has_enforcement_cameras=has_enforcement_cameras,
                has_parking_guidance=has_parking_guidance,
                manages_bike_parking=manages_bike_parking,
                shares_parking_resources=shares_parking_resources,
                has_illegal_parking=has_illegal_parking,
                has_disorderly_parking=has_disorderly_parking,
                timely_data_submission=timely_data_submission,
                cooperates_with_survey=cooperates_with_survey,
                remarks=remarks,
                hospital_feedback=hospital_feedback,
                hospital_id=hospital_id,
                surveyor_id=surveyor_id
            )
            report.save()

            # 获取所有调研表信息
            reports = SurveyReport.objects.all()
            reports_list = list(reports.values(
                'sid', 'district', 'hospital_name', 'appointment_ratio', 'appointment_rate', 
                'precise_appointment_time', 'parking_space_ratio', 'has_no_parking_line', 
                'has_pedestrian_facilities', 'has_speed_limit_signs', 'has_pedestrian_signs', 
                'has_enforcement_cameras', 'has_parking_guidance', 'manages_bike_parking', 
                'shares_parking_resources', 'has_illegal_parking', 'has_disorderly_parking', 
                'timely_data_submission', 'cooperates_with_survey', 'remarks', 'hospital_feedback', 
                'hospital_id', 'surveyor_id'
            ))

            return JsonResponse(reports_list, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)


def get_survey_reports(request):
    if request.method == 'GET':
        reports = SurveyReport.objects.all()
        reports_list = list(reports.values(
            'sid', 'district', 'hospital_name', 'appointment_ratio', 'appointment_rate', 
            'precise_appointment_time', 'parking_space_ratio', 'has_no_parking_line', 
            'has_pedestrian_facilities', 'has_speed_limit_signs', 'has_pedestrian_signs', 
            'has_enforcement_cameras', 'has_parking_guidance', 'manages_bike_parking', 
            'shares_parking_resources', 'has_illegal_parking', 'has_disorderly_parking', 
            'timely_data_submission', 'cooperates_with_survey', 'remarks', 'hospital_feedback', 
            'hospital_id', 'surveyor_id'
        ))
        return JsonResponse(reports_list, safe=False)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=405)


@csrf_exempt
def alter_survey_report(request):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            surveyor_id = data.get('surveyor_id')
            hospital_id = data.get('hospital_id')

            # 查找需要修改的调研表记录
            try:
                report = SurveyReport.objects.get(surveyor_id=surveyor_id, hospital_id=hospital_id)
            except SurveyReport.DoesNotExist:
                return JsonResponse({'error': 'Report not found'}, status=404)

            # 更新调研表记录
            report.district = data.get('district', report.district)
            report.hospital_name = data.get('hospital_name', report.hospital_name)
            report.appointment_ratio = data.get('appointment_ratio', report.appointment_ratio)
            report.appointment_rate = data.get('appointment_rate', report.appointment_rate)
            report.precise_appointment_time = data.get('precise_appointment_time', report.precise_appointment_time)
            report.parking_space_ratio = data.get('parking_space_ratio', report.parking_space_ratio)
            report.has_no_parking_line = data.get('has_no_parking_line', report.has_no_parking_line)
            report.has_pedestrian_facilities = data.get('has_pedestrian_facilities', report.has_pedestrian_facilities)
            report.has_speed_limit_signs = data.get('has_speed_limit_signs', report.has_speed_limit_signs)
            report.has_pedestrian_signs = data.get('has_pedestrian_signs', report.has_pedestrian_signs)
            report.has_enforcement_cameras = data.get('has_enforcement_cameras', report.has_enforcement_cameras)
            report.has_parking_guidance = data.get('has_parking_guidance', report.has_parking_guidance)
            report.manages_bike_parking = data.get('manages_bike_parking', report.manages_bike_parking)
            report.shares_parking_resources = data.get('shares_parking_resources', report.shares_parking_resources)
            report.has_illegal_parking = data.get('has_illegal_parking', report.has_illegal_parking)
            report.has_disorderly_parking = data.get('has_disorderly_parking', report.has_disorderly_parking)
            report.timely_data_submission = data.get('timely_data_submission', report.timely_data_submission)
            report.cooperates_with_survey = data.get('cooperates_with_survey', report.cooperates_with_survey)
            report.remarks = data.get('remarks', report.remarks)
            report.hospital_feedback = data.get('hospital_feedback', report.hospital_feedback)

            report.save()

            # 获取所有调研表信息
            reports = SurveyReport.objects.all()
            reports_list = list(reports.values(
                'sid', 'district', 'hospital_name', 'appointment_ratio', 'appointment_rate', 
                'precise_appointment_time', 'parking_space_ratio', 'has_no_parking_line', 
                'has_pedestrian_facilities', 'has_speed_limit_signs', 'has_pedestrian_signs', 
                'has_enforcement_cameras', 'has_parking_guidance', 'manages_bike_parking', 
                'shares_parking_resources', 'has_illegal_parking', 'has_disorderly_parking', 
                'timely_data_submission', 'cooperates_with_survey', 'remarks', 'hospital_feedback', 
                'hospital_id', 'surveyor_id'
            ))

            return JsonResponse(reports_list, safe=False)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

