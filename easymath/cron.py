from django.core.management import call_command

def backup_data_scheduled_job():
    print('backup_data_scheduled_job')
    try:
        call_command('dbbackup')
    except:
        pass