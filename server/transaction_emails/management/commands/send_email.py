from django.core.management.base import BaseCommand, CommandError
from transaction_emails.views import send_email
from postmarker.core import PostmarkClient

class Command(BaseCommand):
    help = 'Sends an email through Postmark'

    def add_arguments(self, parser):
        # parser.add_argument('num_emails', nargs='+', type=int)
        pass

    def handle(self, *args, **options):

        try: 
            send_email()
            self.stdout.write(self.style.SUCCESS('Successfully sent email.'))
        except Exception as e:
            self.stdout.write(self.style.ERROR('Error: ' + e))
            