# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Street.x_offset'
        db.add_column('streets_street', 'x_offset', self.gf('django.db.models.fields.IntegerField')(default=0), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Street.x_offset'
        db.delete_column('streets_street', 'x_offset')


    models = {
        'streets.street': {
            'Meta': {'object_name': 'Street'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'x_offset': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['streets']
