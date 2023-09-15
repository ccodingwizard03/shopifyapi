from django.db import models
from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
# Create your models here.
import base64
from django.core.files.base import ContentFile

from .api_call import get_image_title

class Product(models.Model):
    """Model definition for Product."""
    name = models.TextField(verbose_name='Artwork name or title')
    image = models.ImageField(verbose_name='Image',null=True,blank=True)
    location = models.TextField(verbose_name='Store, Warm, or Cold Storage',null=True,blank=True)
    artist_inspired_by = models.TextField(verbose_name='For AI generated art only',null=True,blank=True)
    artist = models.TextField(verbose_name='Last Name, First Name, Avatar Name, or AI',null=True,blank=True)
    tags = models.TextField(verbose_name='Keywords or tags associated with the artwork',null=True,blank=True)
    description = models.TextField(verbose_name='Description of the artwork',null=True,blank=True)
    orientation = models.TextField(verbose_name='Orientation of the artwork (e.g., landscape, portrait)',null=True,blank=True)
    subject = models.TextField(verbose_name='Landscape, Still Life, Portrait, Cityscape, etc.',null=True,blank=True)
    inspired_by = models.TextField(verbose_name='Source of inspiration for the artwork',null=True,blank=True)
    fa_wa = models.TextField(verbose_name='Wall art or Fine Art',null=True,blank=True)
    style = models.TextField(verbose_name='Style of the artwork when used as wall art',null=True,blank=True)
    genre = models.TextField(verbose_name='Genre of the artwork for fine art categorization',null=True,blank=True)
    artwork_id = models.IntegerField(verbose_name='Used to identify images by number. Will get inserted into filename',null=True,blank=True)
    decor = models.TextField(verbose_name='Type of decor (e.g., modern, traditional)',null=True,blank=True)
    medium = models.TextField(verbose_name='Oil, Watercolor, Photograph, others',null=True,blank=True)
    color = models.TextField(verbose_name='Primary color of the artwork',null=True,blank=True)
    color_mix = models.TextField(verbose_name='Combination of colors used in the artwork',null=True,blank=True)
    old_price = models.IntegerField(verbose_name='Previous price of the artwork',null=True,blank=True)
    current_price = models.IntegerField(verbose_name='Current price of the artwork',null=True,blank=True)
    big_file_path = models.TextField(verbose_name='Path to the high-resolution image file',null=True,blank=True)
    little_file_path = models.TextField(verbose_name='Path to the low-resolution image file',null=True,blank=True)
    size_mp = models.IntegerField(verbose_name='Size of the image in megapixels',null=True,blank=True)
    uploaded_by = models.TextField(verbose_name='User who uploaded the artwork to the store',null=True,blank=True)
    upload_date = models.DateTimeField(verbose_name='Date and time when the artwork was uploaded',null=True,blank=True)
    cold_storage_by = models.TextField(verbose_name='User who sent the artwork to cold storage',null=True,blank=True)
    cold_storage_date = models.DateTimeField(verbose_name='Date and time when the artwork was moved to cold storage',null=True,blank=True)
    warm_storage_by = models.TextField(verbose_name='User who sent the artwork to warm storage',null=True,blank=True)
    warm_storage_date = models.DateTimeField(verbose_name='Date and time when the artwork was moved to warm storage',null=True,blank=True)
    routing_decision_date = models.DateTimeField(verbose_name='Date and time when the routing decision was made',null=True,blank=True)
    description_of_fine_art_genre = models.TextField(verbose_name='Detailed description of the fine art genre',null=True,blank=True)
    creation_date = models.DateTimeField(verbose_name='Pulled from Metadata',null=True,blank=True)
    availability_status = models.TextField(verbose_name='In inventory or sold',null=True,blank=True)
    licensing_agreement = models.TextField(verbose_name='For guest artists. Details of agreement.',null=True,blank=True)
    prompt = models.TextField(verbose_name='prompt',null=True,blank=True)



    # TODO: Define fields here

    class Meta:
        """Meta definition for Product."""

        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        """Unicode representation of Product."""
        return self.name


# method for updating
@receiver(pre_save, sender=Product, weak=False, )
def presave_payment_model_check(sender, instance=None, created=False, **kwargs):
    #Reference: https://stackoverflow.com/questions/11561722/django-what-is-the-role-of-modelstate
    if instance._state.adding:

        # we would need to create the object
        import requests

        headers = {
            'X-Shopify-Access-Token': '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',
            'Content-Type': 'application/json',
        }

        artist_inspired_by = get_image_title(instance.image.path)

        print(artist_inspired_by)
        json_data = {
            'product': {
                'title': instance.name,
                'body_html': '<strong>'+artist_inspired_by+'</strong>',
                'vendor': instance.subject,
                'product_type': 'Snowboard',
                'status': 'draft',
            },
        }

        print(instance.image._file.file)
        attachment = base64.b64encode(instance.image._file.file.read()).decode()
        response = requests.post(
            'https://gai-test.myshopify.com/admin/api/2023-07/products.json',
            headers=headers,
            json=json_data,
        )
        print(response.json())
        product_id = response.json()['product']['id']

        print(product_id,5444444444444444444444)

        json_data_image = {
            'image': {
                'position': 1,
                'metafields': [
                    {
                        'key': 'new',
                        'value': 'newvalue',
                        'type': 'single_line_text_field',
                        'namespace': 'global',
                    },
                ],
                'attachment': attachment,
                'filename': instance.image.name,
            },
        }

        response_image = requests.post(
            'https://gai-test.myshopify.com/admin/api/2023-07/products/'+str(product_id)+'/images.json',
            headers=headers,
            json=json_data_image,
        )

        instance.description = artist_inspired_by
        # instance.save()

        print ("Creating an object",response_image)
    else:
        #we are updating the object
        print ("Updating an object",instance.pk)
    