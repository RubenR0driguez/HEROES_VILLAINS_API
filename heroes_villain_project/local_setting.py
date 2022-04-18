# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%0=uei1uwbixk+pd31tn!mi^*f5ne6)3z&=t#dwdw+v3++!t*='



# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heroes_villain_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}