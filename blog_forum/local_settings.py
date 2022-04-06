from decouple import config

DATABASES = {
    'default': {
        'ENGINE': config('DB_ENGINE'),
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT')

    }
}

SECRET_KEY = ')we6@9_l*hn!7hb0*mg-ssyf-#glmr4h@-(til7#te5)7w)k$9'