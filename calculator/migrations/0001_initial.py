# calculator/migrations/0001_initial.py
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('reg_number', models.CharField(max_length=20)),
                ('branch', models.CharField(choices=[('cse', 'CSE'), ('csd', 'CSD'), ('csbs', 'CSBS'), ('csm', 'CSM'), ('it', 'IT'), ('ece', 'ECE'), ('eee', 'EEE'), ('civ', 'CIV'), ('che', 'CHE'), ('mec', 'MEC')], max_length=10)),
                ('calculation_type', models.CharField(choices=[('sgpa', 'SGPA'), ('cgpa', 'CGPA')], default='sgpa', max_length=4)),
                ('sgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sem1_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sem2_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('sem3_gpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectGrade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=100)),
                ('subject_credit', models.DecimalField(decimal_places=2, max_digits=4)),
                ('grade', models.CharField(max_length=2)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subject_grades', to='calculator.studentrecord')),
            ],
        ),
        migrations.AddIndex(
            model_name='studentrecord',
            index=models.Index(fields=['reg_number'], name='reg_number_idx'),
        ),
        migrations.AddIndex(
            model_name='studentrecord',
            index=models.Index(fields=['name'], name='name_idx'),
        ),
        migrations.AddIndex(
            model_name='studentrecord',
            index=models.Index(fields=['created_at'], name='created_at_idx'),
        ),
    ]