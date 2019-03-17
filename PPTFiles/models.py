from django.db import models

class PPTFiles(models.Model):
    Title=models.TextField()
    Description=models.TextField()
    def __str__(self):
	       return self.Title+" "+self.Description+" "

class PPTFiles_Attachment(models.Model):
    key = models.ForeignKey(PPTFiles,on_delete=models.CASCADE)
    file = models.TextField( null=True, blank=True)
