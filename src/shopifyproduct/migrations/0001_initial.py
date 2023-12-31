# Generated by Django 3.2.12 on 2023-09-06 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Artwork name or title')),
                ('cocation', models.TextField(blank=True, null=True, verbose_name='Store, Warm, or Cold Storage')),
                ('artist_inspired_by', models.TextField(blank=True, null=True, verbose_name='For AI generated art only')),
                ('artist', models.TextField(blank=True, null=True, verbose_name='Last Name, First Name, Avatar Name, or AI')),
                ('tags', models.TextField(blank=True, null=True, verbose_name='Keywords or tags associated with the artwork')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description of the artwork')),
                ('orientation', models.TextField(blank=True, null=True, verbose_name='Orientation of the artwork (e.g., landscape, portrait)')),
                ('subject', models.TextField(blank=True, null=True, verbose_name='Landscape, Still Life, Portrait, Cityscape, etc.')),
                ('inspired_by', models.TextField(blank=True, null=True, verbose_name='Source of inspiration for the artwork')),
                ('fa_wa', models.TextField(blank=True, null=True, verbose_name='Wall art or Fine Art')),
                ('style', models.TextField(blank=True, null=True, verbose_name='Style of the artwork when used as wall art')),
                ('genre', models.TextField(blank=True, null=True, verbose_name='Genre of the artwork for fine art categorization')),
                ('artwork_id', models.IntegerField(blank=True, null=True, verbose_name='Used to identify images by number. Will get inserted into filename')),
                ('decor', models.TextField(blank=True, null=True, verbose_name='Type of decor (e.g., modern, traditional)')),
                ('medium', models.TextField(blank=True, null=True, verbose_name='Oil, Watercolor, Photograph, others')),
                ('color', models.TextField(blank=True, null=True, verbose_name='Primary color of the artwork')),
                ('color_mix', models.TextField(blank=True, null=True, verbose_name='Combination of colors used in the artwork')),
                ('old_price', models.IntegerField(blank=True, null=True, verbose_name='Previous price of the artwork')),
                ('current_price', models.IntegerField(blank=True, null=True, verbose_name='Current price of the artwork')),
                ('big_file_path', models.TextField(blank=True, null=True, verbose_name='Path to the high-resolution image file')),
                ('little_file_path', models.TextField(blank=True, null=True, verbose_name='Path to the low-resolution image file')),
                ('size_mp', models.IntegerField(blank=True, null=True, verbose_name='Size of the image in megapixels')),
                ('uploaded_by', models.TextField(blank=True, null=True, verbose_name='User who uploaded the artwork to the store')),
                ('upload_date', models.DateTimeField(blank=True, null=True, verbose_name='Date and time when the artwork was uploaded')),
                ('cold_storage_by', models.TextField(blank=True, null=True, verbose_name='User who sent the artwork to cold storage')),
                ('cold_storage_date', models.DateTimeField(blank=True, null=True, verbose_name='Date and time when the artwork was moved to cold storage')),
                ('warm_storage_by', models.TextField(blank=True, null=True, verbose_name='User who sent the artwork to warm storage')),
                ('warm_storage_date', models.DateTimeField(blank=True, null=True, verbose_name='Date and time when the artwork was moved to warm storage')),
                ('routing_decision_date', models.DateTimeField(blank=True, null=True, verbose_name='Date and time when the routing decision was made')),
                ('description_of_fine_art_genre', models.TextField(blank=True, null=True, verbose_name='Detailed description of the fine art genre')),
                ('creation_date', models.DateTimeField(blank=True, null=True, verbose_name='Pulled from Metadata')),
                ('availability_status', models.TextField(blank=True, null=True, verbose_name='In inventory or sold')),
                ('licensing_agreement', models.TextField(blank=True, null=True, verbose_name='For guest artists. Details of agreement.')),
                ('prompt', models.TextField(blank=True, null=True, verbose_name='prompt')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]
