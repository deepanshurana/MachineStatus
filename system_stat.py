import socket
import pprint
import time
import sys
import os
from subprocess import call
import json 
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'machineProject.settings')
django.setup()

from machineApp.models import MOD
ports = {"Anutone": 15022, "NRT": 16022, "KPS": 16025, "Pinak": 16023, "Manas": 16024}

status ={}

true, false = 1, 0
def system_status():
    for key, value in ports.items():
        c = socket.socket()
        try:
            c.connect(("monitoring.paralaxiom.in", value))
            status[key] = True
        except socket.error:
            status[key] = False
        
        c.close()
    print(status, type(status))
    # statusJson = json.dumps(status, sort_keys=True)

    MOD.objects.filter(owner='paralaxiom').update(data=status)
    # print(statusJson)
    return status


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')


if __name__ == "__main__":
    while True:
        systems = system_status()
        #pprint.pprint(systems, indent=4)
        text = ""
        for k, v in systems.items():
            if v:
                #print(f'\033[0;37;49m{k}: \033[0;32;49m{v}')
                text += f'\033[0;37;49m{k}: \033[0;32;49m{v}\n'
            else:
                #print(f'\033[0;37;49m{k}: \033[5;31;49m{v}')
                text += f'\033[0;37;49m{k}: \033[5;31;49m{v}\n'

        clear()
        print(f'{text}')
        sys.stdout.flush()
        # sys.stdout.write("\033[F")
        try:
            for i in range(5):
                time.sleep(1)
        except KeyboardInterrupt:
            print('\nExiting...')
            break
