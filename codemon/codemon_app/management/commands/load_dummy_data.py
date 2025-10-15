from django.core.management.base import BaseCommand
from codemon_app.initial_data import load_data

class Command(BaseCommand):
    help = 'Load dummy data for CodeMon application'
    
    def handle(self, *args, **options):
        self.stdout.write('🚀 Loading CodeMon dummy data...')
        load_data()
        self.stdout.write(
            self.style.SUCCESS('✅ Dummy data loaded successfully!')
        )