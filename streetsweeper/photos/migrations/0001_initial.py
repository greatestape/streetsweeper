
from south.db import db
from django.db import models
from photos.models import *

class Migration:
    def forwards(self, orm):
        # Adding model 'Photo'
        db.create_table('photos_photo', (
            ('id', orm['photos.Photo:id']),
            ('photo', orm['photos.Photo:photo']),
            ('width', orm['photos.Photo:width']),
            ('height', orm['photos.Photo:height']),
        ))
        db.send_create_signal('photos', ['Photo'])

    def backwards(self, orm):
        # Deleting model 'Photo'
        db.delete_table('photos_photo')

    models = {
        'photos.photo': {
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['photos']
