from celery import Celery

"""
1.创建任务
2.创建celery实例
3.在celery设置任务和borker
4.worker
"""

# 1.celery是一个即插即用的任务队列
# celery是需要和django（当前工程）进行交互    工程会调用celery
# 让celery加载当前工程的默认配置

# 第一种方式:
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mall.settings")
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "test_mall.settings.dev")
# 第二种方式
# 进行Celery允许配置,为celery使用django配置文件进行设置
# import os
# if not os.getenv('DJANGO_SETTINGS_MODULE'):
#     os.environ['DJANGO_SETTINGS_MODULE'] = 'test_mall.settings'


# 2.创建celery实例
# main 习惯性填写celery文件路径
# 确保main不出现重复
app = Celery(main='celery_tasks')

# 3.设置borker
# 加载borker的配置信息   参数:路径信息
app.config_from_object('celery_tasks.config')

# 4.自动加载任务
# celery自动检测任务    参数：列表 // 元素：任务的包路径
# app.autodiscover_tasks(['celery_tasks.sms', 'celery_tasks.email', 'celery_tasks.html'])
app.autodiscover_tasks(['celery_tasks.sms'])

# 5.worker去执行任务
# 需要在虚拟环境中执行指令    celery -A celery实例对象的文件路径 worker -l info
# celery -A clery_tasks.main worker -l info




























