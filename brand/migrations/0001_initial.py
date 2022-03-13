# Generated by Django 3.2.12 on 2022-02-06 16:39

import brand.models.commentary
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='-unnamed-', max_length=200, verbose_name='Name of this brand/data source')),
                ('description', models.TextField(blank=True, default='-blank-', null=True, verbose_name='Description of this instance of this brand/data source')),
                ('website', models.URLField(blank=True, null=True, verbose_name='Website of this brand/data source. i.e. bankofamerica.com')),
                ('countries', django_countries.fields.CountryField(help_text='Where the brand offers retails services', max_length=746, multiple=True)),
                ('tag', models.CharField(help_text=('the tag we use or this brand/datasource record at Bank.Green. ', 'Prepend this with the relevant datasource. i.e. banktrack_bank_of_america. for brands, prepend with nothing at all i.e. bank_of_america'), max_length=100, unique=True)),
                ('permid', models.CharField(blank=True, max_length=15)),
                ('isin', models.CharField(blank=True, max_length=15)),
                ('viafid', models.CharField(blank=True, max_length=15)),
                ('lei', models.CharField(blank=True, max_length=15)),
                ('googleid', models.CharField(blank=True, max_length=15)),
                ('rssd', models.CharField(blank=True, max_length=15)),
                ('rssd_hd', models.CharField(blank=True, max_length=15)),
                ('cusip', models.CharField(blank=True, max_length=15)),
                ('thrift', models.CharField(blank=True, max_length=15)),
                ('thrift_hc', models.CharField(blank=True, max_length=15)),
                ('aba_prim', models.CharField(blank=True, max_length=15)),
                ('ncua', models.CharField(blank=True, max_length=15)),
                ('fdic_cert', models.CharField(blank=True, max_length=15)),
                ('occ', models.CharField(blank=True, max_length=15)),
                ('ein', models.CharField(blank=True, max_length=15)),
                ('source_link', models.URLField(blank=True, null=True, verbose_name="Link to the data source's webpage. i.e. the banktrack.org or b-impact webpage for the bank")),
                ('subsidiary_of_1_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 1')),
                ('subsidiary_of_2_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 2')),
                ('subsidiary_of_3_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 3')),
                ('subsidiary_of_4_pct', models.IntegerField(default=0, verbose_name='percentage owned by subsidiary 4')),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time of last update')),
                ('subsidiary_of_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_1_data_source', to='brand.brand')),
                ('subsidiary_of_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_2_data_source', to='brand.brand')),
                ('subsidiary_of_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_3_data_source', to='brand.brand')),
                ('subsidiary_of_4', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subsidiary_of_4_data_source', to='brand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Commentary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aliases', models.CharField(blank=True, help_text='Other names for the brand, used for search. comma seperated. i.e. BOFA, BOA', max_length=200, null=True)),
                ('display_on_website', models.BooleanField(default=False)),
                ('comment', models.TextField(help_text='Meta. Comments for staff and/or editors')),
                ('rating', models.CharField(choices=[(brand.models.commentary.RatingChoice['GREAT'], 'great'), (brand.models.commentary.RatingChoice['OK'], 'ok'), (brand.models.commentary.RatingChoice['BAD'], 'bad'), (brand.models.commentary.RatingChoice['WORST'], 'worst'), (brand.models.commentary.RatingChoice['UNKNOWN'], 'unknown')], max_length=8)),
                ('unique_statement', models.CharField(blank=True, help_text='Positive/Negative. i.e. Despite introducing policies to restrict unconventional oil and gas finance, BNP Paribas recently ', max_length=300, null=True)),
                ('headline', models.CharField(blank=True, help_text='Positive/Negative. i.e. #1 in Coal', max_length=200, null=True)),
                ('top_blurb_headline', models.CharField(help_text='Positive/Negative. i.e. Your money is being used to fund the climate crisis at an alarming rate.', max_length=200)),
                ('top_blurb_subheadline', models.CharField(help_text='Positive/Negative. i.e. According to the latest research*, in 2020 your bank was the 4th largest funder...', max_length=300)),
                ('snippet_1', models.CharField(blank=True, default='', help_text='Negative. Custom fact about the brand. Used to fill in templates', max_length=150)),
                ('snippet_1_link', models.URLField(blank=True, default='', help_text='link to dirty deal 1 detauls')),
                ('snippet_2', models.CharField(blank=True, default='', help_text='Negative. Custom fact about the brand. Used to fill in templates', max_length=150)),
                ('snippet_2_link', models.URLField(blank=True, default='', help_text='link to dirty deal 2 detauls')),
                ('snippet_3', models.CharField(blank=True, default='', help_text='Negative. Custom fact about the brand. Used to fill in templates', max_length=150)),
                ('snippet_3_link', models.URLField(blank=True, default='', help_text='link to dirty deal 3 detauls')),
                ('top_three_ethical', models.BooleanField(default=False, help_text='Positive. Is this bank recommended best banks of a country page?')),
                ('recommended_order', models.IntegerField(default=3, help_text='Positive. in case there are more recommended banks than can fit on the page, lower numbers are given priority', null=True)),
                ('recommended_in', django_countries.fields.CountryField(help_text='Positive. what countries will this bank be recommended in?', max_length=746, multiple=True)),
                ('from_the_website', models.TextField(help_text='Positive. used to to describe green banks in their own words')),
                ('checking_saving', models.BooleanField(default=False, help_text='Positive. does the bank offer checkings or savings accounts?')),
                ('checking_saving_details', models.CharField(blank=True, default='', help_text='Positive. Details on available checkings and savings accounts', max_length=50)),
                ('free_checking', models.BooleanField(default=False, help_text='Positive. does the bank offer free checkings?')),
                ('free_checking_details', models.CharField(blank=True, default='', help_text='Positive. Details on available free checkings', max_length=50)),
                ('interest_rates', models.CharField(blank=True, help_text='Positive. Details about offered interest rates', max_length=50, null=True)),
                ('free_atm_withdrawl', models.BooleanField(default=False, help_text='Positive. does the bank offer free ATM withdrawals?')),
                ('free_atm_withdrawl_details', models.CharField(blank=True, default='', help_text='Positive. Details on available free ATM withdrawals', max_length=50)),
                ('online_banking', models.BooleanField(default=False, help_text='Positive. does the bank offer online banking?')),
                ('local_branches', models.BooleanField(default=False, help_text='Positive. does the bank offer local branches?')),
                ('local_branches_details', models.CharField(blank=True, help_text='Positive. Details on local branches', max_length=50, null=True)),
                ('mortgage_or_loan', models.BooleanField(default=False, help_text='Positive. does the bank offer mortgage or loans?')),
                ('deposit_protection', models.CharField(blank=True, help_text='Positive. Details on deposit protection', max_length=50, null=True)),
                ('credit_cards', models.BooleanField(default=False, help_text='Positive. does the bank offer credit cards?')),
                ('credit_cards_details', models.CharField(blank=True, help_text='Positive. Details on credit cards', max_length=50, null=True)),
                ('free_international_card_payment', models.BooleanField(default=False, help_text='Positive. does the bank offer free international card payments?')),
                ('free_international_card_payment_details', models.CharField(blank=True, help_text='Positive. Details on free international card payments', max_length=50, null=True)),
                ('brand', models.OneToOneField(help_text='What brand is this comment associated with?', on_delete=django.db.models.deletion.CASCADE, related_name='commentary_brand', to='brand.brand')),
            ],
        ),
    ]
