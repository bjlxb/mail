import random

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from pip._vendor.requests import Response
from rest_framework import status
from rest_framework.views import APIView

from test_mall.libs.captcha.captcha import captcha
from test_mall.utils.exceptions import logger
from verifications.serializers import RegisterSmscodeSerializer

"""
1.分析需求  （到底要做什么
2.把需要做的记录下来    （缕清思路
3.路由和请求方式
4.确定视图
5.按照步骤实现功能

前端传递一个uuid过来，我们后端生成一个图片
1.接收 image_code_id
2.生成图片和验证码
3.把验证码保存到redis中
4.返回图片相应

GET     /verifications/images/(?P<image_code_id>.+)/
或GET     /verifications/images/?image_code_id=xxx

"""


class RegisterImageAPIView(APIView):

    def get(self, request, image_code_id):
        # 1.接收 image_code_id
        # 2.生成图片和验证码
        text, image = captcha.generate_captcha()
        # 3.把验证码保存到redis中
        # 3.1链接redis
        # redis_conn = get_redis_connection('code')
        # 3.2设置图片
        # redis_conn.setex('img_'+image_code_id, 60, text)
        # 4.返回图片相应  不使用Response
        print(text)
        print(image)
        return HttpResponse(image, content_type='image/jpeg')


class RegisterSmscodeAPIView(APIView):

    def get(self, request, mobile):
        # 1.接收参数
        params = request.query_params
        # 2.校验参数    还需要验证码，用户输入的图片验证码和redis的保存是否一致
        serializer = RegisterSmscodeSerializer(data=params)
        serializer.is_valid(raise_exception=True)
        # 3.生成短信
        sms_code = '%06d' % random.randint(0, 999999)
        # 4.将短信保存在redis中
        redis_conn = get_redis_connection('code')
        redis_conn.setex('sms_'+mobile, 5*60, sms_code)
        # 5.使用云通讯发送短信
        # CCP().send_template_sms(mobile,[sms_code,5],1)

        from test_mall.celery_tasks.sms.tasks import send_sms_code
        # delay的参数和任务的参数对应
        # 必须调用delay方法
        send_sms_code.delay(mobile, sms_code)

        # 6.返回相应
        return Response({'msg': 'ok'})
