import json
from django.http import JsonResponse
from postmarker.core import PostmarkClient
from users.models import CustomUser
from transaction_emails.models import EmailVersion, TransactionEmail

postmark_token = 'token_upon_request'

def send_email_with_template(self, to_emails=[], version_alias=None):

    # version name would be fed into the function to provide to appropriate information based
    # on the version that is to be used, e.g. version_alias="v1"

    # parameters that would be typically passed in
    to_emails = ['damian@onehep.com', 'damian@onehep.com']
    version_alias="v1"

    # get version object from DB
    try:
        version = EmailVersion.objects.get(version_alias=version_alias)
    except:
        raise

    # Create postmark client.
    postmark = PostmarkClient(server_token=postmark_token)

    for email_address in to_emails:

        transaction_email = None

        try:
            # Get user object from each email in the list.
            to_user = CustomUser.objects.get(email=email_address)

            # Create an email instance and save it in the database. Send the id with the email as
            # metadata and then fetch this email later in the webhook to modify the original email 
            # object, such as whether it was opened or a link was clicked.
            transaction_email = TransactionEmail(to_user=to_user, to_email=email_address, version=version)
            transaction_email.save()

        except:
            raise

        try:
            # Create and send email through Postmark.
            # Used ngrok to test webhook.
            postmark.emails.send_with_template(
                TemplateId=version.postmark_template_id,
                TemplateModel={
                    'product_name': 'Test', 
                    'name': 'Al Capone',
                    'action_url': 'https://c142-65-60-152-4.ngrok.io/postmark_webhook/',    
                },
                From='damian@onehep.com',
                To=email_address,
                TrackOpens=True,
                Metadata = {
                    'EmailId': transaction_email.id,

                }
            )
        except Exception as e:
            raise

    return(JsonResponse({'foo':'bar'}))

def postmark_webhook(request):

    if request.method == 'POST':
        data = json.loads(request.body)

        email_id = None
        email = None
        
        try:
            # get email_id sent as metadata
            email_id = data['Metadata']['EmailId']
        except:
            raise
        
        try:
            # Get email object to modify.
            email = TransactionEmail.objects.get(id=email_id)
        except:
            print("Error: transaction email not found.")
        
        try:
            if email:
                if data['RecordType'] == 'Open':
                    email.opened = True
                    email.save()
                # From postmark: Until your account is approved, no links will be encoded/tracked when sending emails through Postmark.
                elif data['RecordType'] == 'Click':
                    email.link_clicked = True
                    email.save()
            else:
                pass
        except:
            raise

    return(JsonResponse({'foo':'bar'} ))