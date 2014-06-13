# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Setting'
        db.create_table(u'main_setting', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('setting_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('my_name', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('my_job', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('my_descriptions', self.gf('django.db.models.fields.TextField')(max_length=200)),
            ('my_foto', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('status', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'main', ['Setting'])


    def backwards(self, orm):
        # Deleting model 'Setting'
        db.delete_table(u'main_setting')


    models = {
        u'main.setting': {
            'Meta': {'object_name': 'Setting'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'my_descriptions': ('django.db.models.fields.TextField', [], {'max_length': '200'}),
            'my_foto': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'my_job': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'my_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'setting_name': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'status': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        }
    }

    complete_apps = ['main']