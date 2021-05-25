from django.contrib.gis.db.models import PointField
from django.db import models
import uuid

class Localizacao (models.Model):
    
    '''data_gps_loc = models.DateTimeField()
    km_hora_loc = models.SmallIntegerField()'''

    id_loc = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False),
    dt_criacao_loc = models.DateTimeField(auto_now_add=True),
    ponto_loc = PointField(geography=True, blank=True, null=True, srid=4326, help_text="Point(longitude latitude)")

    @property
    def lat_log(self):
        return list(getattr(self.ponto_loc,'coords', [])[::-1])
    
    def __str__(self):
        return 'ID: %s | Data: %s' % (self.pk, self.ponto_loc)