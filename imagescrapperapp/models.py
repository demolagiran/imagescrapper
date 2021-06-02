from django.db import models

class Scrapedimage(models.Model):
    image_url = models.CharField(max_length = 10000)
    #image_name = models.CharField(max_length=100)
    def __str__(self):
        return self.image_url
    #class Meta:
        #db_table = 'Scrappedimage'
    

