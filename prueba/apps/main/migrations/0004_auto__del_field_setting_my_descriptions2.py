# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Setting.my_descriptions2'
        db.delete_column(u'main_setting', 'my_descriptions2')


    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Setting.my_descriptions2'
        raise RuntimeError("Cannot reverse this migration. 'Setting.my_descriptions2' and its values cannot be restored.")
        
        # The following code is provided here to aid in writing a correct migration        # Adding field 'Setting.my_descriptions2'
        db.add_column(u'main_setting', 'my_descriptions2',
                      self.gf('django.db.models.fields.TextField')(max_length=200),
                      keep_default=False)


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