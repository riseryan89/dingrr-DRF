## 딩그르르 REAL WORLD DJANGO REST FRAMEWORK

1. [블로그 #1 - 프로젝트 생성편](https://dingrr.com/blog/post/rwdrfp-real-world-drf-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%ED%83%84%EC%83%9D)
2. [블로그 #2 - 프로젝트 구조](https://dingrr.com/blog/post/rwdrfp-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8-%EA%B5%AC%EC%A1%B0)


## STACKS
1. Python 3.7.7
2. Django 3.0.4
3. Django RESTFramework 3.11.0
4. MySQL 8.0
5. REDIS in Docker(**NOT YET**, but will use)
6. Celery(**NOT YET**, but will use)



## USAGE
1. Download or Clone this Repository
2. Install and activate VirtualEnv
3. pip install -r requirements.txt
4. python3 manage.py runserver

*REMEMBER*
THIS IS A REAL WORLD PROJECT.<br>
DO NOT FORGET TO CHANGE ALL DETAILS BEFORE USE.<br><br>
YOU WILL BE REQUIRED TO HAVE **.key_store** file. The format should be like below;
```python
[THIS_IS_INTERNAL_USE_ONLY]
NEVER_SHARE = Please
NEVER_UPLOAD = Anywhere
IF_YOU_DONT_KNOW = JUST_LEAVE_IT


[DB]
HOST_DEBUG = localhost
HOST_PROD = localhost
PORT = 3306
USER = your_user
PW = your_pw
CHARSET = utf8mb4
DB_NAME = your_db

```
Place .key_store file in the main folder where dingrr and apps folders are located.


## Any Forks, Stars, PRs, Helps, Suggetions
Thanks! 