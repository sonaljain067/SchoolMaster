# Generated by Django 4.1.7 on 2023-03-24 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("schoolstudent", "0003_remove_schoolinfo_user_remove_studentinfo_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="studentinfo",
            name="email",
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.CharField(
                choices=[
                    ("admin", "Admin"),
                    ("school", "School"),
                    ("student", "Student"),
                ],
                default="",
                max_length=20,
            ),
        ),
    ]