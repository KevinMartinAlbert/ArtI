import os
import sys
import datetime
import django
from django.core.management import call_command

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ArtI.settings")

django.setup()

BACKUP_DIR = "backups/"
os.makedirs(BACKUP_DIR, exist_ok=True)

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
backup_file = os.path.join(BACKUP_DIR, f"db_backup_{timestamp}.json")

with open(backup_file, "w") as f:
    call_command("dumpdata", "--indent", "2", stdout=f)

print(f"Backup created at {backup_file}")
