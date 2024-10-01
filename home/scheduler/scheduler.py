import os
import requests
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django_apscheduler import util
from django.conf import settings





def send_document(document_path=None):
    # Get the full path of db.sqlite3
    db_path = os.path.join(settings.BASE_DIR, 'db.sqlite3')

  
    url = f"https://api.telegram.org/bot6308227197:AAHweeHPdwsa9SDWpr7g627qxpqtbZsaWsU/sendDocument"

    data = {
        "chat_id": 5294965763,
    }

    with open(
        db_path, "rb"
    ) as document:
        files = {"document": document}
        response = requests.post(url, data=data, files=files)

    return response.json()


def backup_every_minute():
    send_document()
    print("Backed up")


@util.close_old_connections
def delete_old_job_executions(max_age=2):
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")
    scheduler.add_job(
        backup_every_minute,
        "interval",
        hours=6,
        jobstore="default",
        id="backup_every_five_seconds",
        replace_existing=True,
    )
    scheduler.add_job(
        delete_old_job_executions,
        "interval",
        hours=3,
        jobstore="default",
        id="delete_old_job_executions",
        replace_existing=True,
    )
    try:
        scheduler.start()
    except KeyboardInterrupt:
        scheduler.shutdown()
