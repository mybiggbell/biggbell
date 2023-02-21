from django.db import models
from userauth.models import Brand , MyUser ,Creator
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Project(models.Model):
    project_brand = models.ForeignKey(to=Brand, on_delete=models.CASCADE , related_name='project')
    project_name = models.CharField(max_length=350)
    detail_about_project = models.TextField()
    total_cost = models.BigIntegerField()
    project_file = models.FileField(upload_to='project_file')
    payment_id =models.CharField(max_length=150,blank=True)
    paid = models.BooleanField(default=False)

    def get_creator(self):
        pro = Project.objects.get(id=self.id)
        return Project_Approval.objects.filter(project=pro) 

CHOICES_GENDER = [
    ("Pandding", _("Pandding")),
    ("Select", _("Select")),
    ("complete", _("complete")),
    ("Reject", _("Reject"))
]
class Project_Approval(models.Model):
    project = models.ForeignKey(to=Project, on_delete=models.CASCADE,related_name='project_approval')
    creator = models.ForeignKey(to=Creator, on_delete=models.CASCADE,related_name='project_approval_user')
    creator_note = models.TextField()
    is_approval =models.CharField(max_length=20, blank=True, null=True, choices=CHOICES_GENDER)
