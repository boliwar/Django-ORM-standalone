import os

import django
import settings
from django.utils.timezone import localtime as dj_localtime, now as dj_now

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard, Visit  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001

    unclosed_visits = Visit.objects.filter(leaved_at__isnull=True)

    for unclosed_visit in unclosed_visits:
        entered_msk = dj_localtime(unclosed_visit.entered_at)
        print(f'Зашёл в хранилище, время по Москве: \n{entered_msk}')
        print()
        time_in =  dj_now() - entered_msk
        print(f'Находится в хранилище:\n{time_in}')
        print('---')
    