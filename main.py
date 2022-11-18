import os

import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from datacenter.models import Passcard  # noqa: E402

if __name__ == '__main__':
    # Программируем здесь
    print('Количество пропусков:', Passcard.objects.count())  # noqa: T001
    passcards = Passcard.objects.all()

    owner_name = passcards[0].owner_name
    passcode = passcards[0].passcode
    created_at = passcards[0].created_at
    is_active = passcards[0].is_active

    print(owner_name, passcode, created_at, is_active)
