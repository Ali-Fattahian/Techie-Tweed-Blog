from django.core.management import call_command

def scheduled_backup():
  try:
    call_command('dbbackup') # python manage.py dbbackup
  except:
    pass
