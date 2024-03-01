# Generated by Django 4.1.7 on 2024-02-26 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("brand", "0039_alter_brand_tag_delete_brandupdate")]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="embrace",
            field=models.CharField(
                choices=[("breakup letter", "Breakup Letter"), ("none", "None")],
                default="none",
                max_length=20,
                null=True,
            ),
        )
    ]