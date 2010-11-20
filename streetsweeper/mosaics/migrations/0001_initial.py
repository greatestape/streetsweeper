
from south.db import db
from django.db import models
from mosaics.models import *

class Migration:
    depends_on = [('photos', '0001_initial')]
    def forwards(self, orm):
        
        # Adding model 'Mosaic'
        db.create_table('mosaics_mosaic', (
            ('id', orm['mosaics.Mosaic:id']),
            ('name', orm['mosaics.Mosaic:name']),
            ('slug', orm['mosaics.Mosaic:slug']),
        ))
        db.send_create_signal('mosaics', ['Mosaic'])
        
        # Adding model 'Patch'
        db.create_table('mosaics_patch', (
            ('id', orm['mosaics.Patch:id']),
            ('mosaic', orm['mosaics.Patch:mosaic']),
            ('scale', orm['mosaics.Patch:scale']),
            ('position_x', orm['mosaics.Patch:position_x']),
            ('position_y', orm['mosaics.Patch:position_y']),
            ('source_image', orm['mosaics.Patch:source_image']),
            ('rotation', orm['mosaics.Patch:rotation']),
            ('mask', orm['mosaics.Patch:mask']),
            ('modified_image', orm['mosaics.Patch:modified_image']),
        ))
        db.send_create_signal('mosaics', ['Patch'])
        
    
    
    def backwards(self, orm):
        
        # Deleting model 'Mosaic'
        db.delete_table('mosaics_mosaic')
        
        # Deleting model 'Patch'
        db.delete_table('mosaics_patch')
        
    
    
    models = {
        'auth.group': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '80', 'unique': 'True'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'unique_together': "(('content_type', 'codename'),)"},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True', 'blank': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False', 'blank': 'True'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'max_length': '30', 'unique': 'True'})
        },
        'contenttypes.contenttype': {
            'Meta': {'unique_together': "(('app_label', 'model'),)", 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'mosaics.mosaic': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'unique': 'True', 'db_index': 'True'})
        },
        'mosaics.patch': {
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mask': ('django.db.models.fields.CommaSeparatedIntegerField', [], {'max_length': '512', 'blank': 'True'}),
            'modified_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'mosaic': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mosaics.Mosaic']"}),
            'position_x': ('django.db.models.fields.FloatField', [], {}),
            'position_y': ('django.db.models.fields.FloatField', [], {}),
            'rotation': ('django.db.models.fields.FloatField', [], {}),
            'scale': ('django.db.models.fields.FloatField', [], {}),
            'source_image': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['photos.Photo']"})
        },
        'photos.photo': {
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'width': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        }
    }
    
    complete_apps = ['mosaics']
