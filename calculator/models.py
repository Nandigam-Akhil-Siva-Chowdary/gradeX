# calculator/models.py
from djongo import models

class StudentRecord(models.Model):
    BRANCH_CHOICES = [
        ('cse', 'CSE'),
        ('csd', 'CSD'),
        ('csbs', 'CSBS'),
        ('csm', 'CSM'),
        ('it', 'IT'),
        ('ece', 'ECE'),
        ('eee', 'EEE'),
        ('civ', 'CIV'),
        ('che', 'CHE'),
        ('mec', 'MEC'),
    ]
    
    CALCULATION_CHOICES = [
        ('sgpa', 'SGPA'),
        ('cgpa', 'CGPA'),
    ]
    
    # MongoDB uses ObjectId as primary key automatically
    # No need to define id field
    
    name = models.CharField(max_length=100)
    reg_number = models.CharField(max_length=20)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    calculation_type = models.CharField(max_length=4, choices=CALCULATION_CHOICES, default='sgpa')
    
    # SGPA fields
    sgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    # CGPA fields (3 semesters)
    sem1_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem2_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    sem3_gpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Optional: Define MongoDB indexes for better performance
    class Meta:
        indexes = [
            models.Index(fields=['reg_number']),
            models.Index(fields=['name']),
            models.Index(fields=['created_at']),
        ]

    def __str__(self):
        return f"{self.name} ({self.reg_number}) - {self.get_branch_display()} - {self.calculation_type.upper()}"
    
    def get_result(self):
        """Return the calculated result based on calculation type"""
        if self.calculation_type == 'sgpa':
            return self.sgpa
        else:
            return self.cgpa


class SubjectGrade(models.Model):
    # Use Djongo's ObjectId field for foreign key
    student = models.ForeignKey(
        StudentRecord, 
        on_delete=models.CASCADE, 
        related_name='subject_grades'
    )
    subject_name = models.CharField(max_length=100)
    subject_credit = models.DecimalField(max_digits=4, decimal_places=2)
    grade = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.student.name} - {self.subject_name}: {self.grade}"