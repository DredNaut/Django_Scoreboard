from django.db import models

# Create your models here.

class Team(models.Model):

    members = models.CharField(max_length=200)
    rank = models.IntegerField(default=0)
    pt_score =  models.IntegerField(default=0)
    ruck_score =  models.IntegerField(default=0)
    wpns_score =  models.IntegerField(default=0)
    ln_score =  models.IntegerField(default=0)
    tc3_score =  models.IntegerField(default=0)
    est_score =  models.IntegerField(default=0)
    radio_score =  models.IntegerField(default=0)
    hgac_score =  models.IntegerField(default=0)
    cff_score =  models.IntegerField(default=0)

    def __str__(self):
        return self.members

    def total_score(self):
        return self.pt_score + self.ruck_score + self.wpns_score + self.ln_score + self.tc3_score + self.est_score + self.radio_score + self.hgac_score + self.cff_score
