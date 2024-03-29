# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Button'
        db.create_table('picasabuttonizer_button', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('guid', self.gf('django.db.models.fields.CharField')(unique=True, max_length=50)),
            ('icon', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('icon_name', self.gf('django.db.models.fields.CharField')(max_length=30, null=True, blank=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('tooltip', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('picasabuttonizer', ['Button'])

        # Adding model 'HybridButton'
        db.create_table('picasabuttonizer_hybridbutton', (
            ('button_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['picasabuttonizer.Button'], unique=True, primary_key=True)),
            ('hybrid_uploader_url', self.gf('django.db.models.fields.URLField')(max_length=30)),
        ))
        db.send_create_signal('picasabuttonizer', ['HybridButton'])

        # Adding model 'TrayexecButton'
        db.create_table('picasabuttonizer_trayexecbutton', (
            ('button_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['picasabuttonizer.Button'], unique=True, primary_key=True)),
            ('exe_name', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal('picasabuttonizer', ['TrayexecButton'])

        # Adding model 'OpenButton'
        db.create_table('picasabuttonizer_openbutton', (
            ('button_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['picasabuttonizer.Button'], unique=True, primary_key=True)),
            ('open', self.gf('django.db.models.fields.CharField')(max_length=70)),
        ))
        db.send_create_signal('picasabuttonizer', ['OpenButton'])


    def backwards(self, orm):
        
        # Deleting model 'Button'
        db.delete_table('picasabuttonizer_button')

        # Deleting model 'HybridButton'
        db.delete_table('picasabuttonizer_hybridbutton')

        # Deleting model 'TrayexecButton'
        db.delete_table('picasabuttonizer_trayexecbutton')

        # Deleting model 'OpenButton'
        db.delete_table('picasabuttonizer_openbutton')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'picasabuttonizer.button': {
            'Meta': {'object_name': 'Button'},
            'guid': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'icon': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'icon_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'tooltip': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']", 'null': 'True', 'blank': 'True'})
        },
        'picasabuttonizer.hybridbutton': {
            'Meta': {'object_name': 'HybridButton', '_ormbases': ['picasabuttonizer.Button']},
            'button_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['picasabuttonizer.Button']", 'unique': 'True', 'primary_key': 'True'}),
            'hybrid_uploader_url': ('django.db.models.fields.URLField', [], {'max_length': '30'})
        },
        'picasabuttonizer.openbutton': {
            'Meta': {'object_name': 'OpenButton', '_ormbases': ['picasabuttonizer.Button']},
            'button_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['picasabuttonizer.Button']", 'unique': 'True', 'primary_key': 'True'}),
            'open': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        },
        'picasabuttonizer.trayexecbutton': {
            'Meta': {'object_name': 'TrayexecButton', '_ormbases': ['picasabuttonizer.Button']},
            'button_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['picasabuttonizer.Button']", 'unique': 'True', 'primary_key': 'True'}),
            'exe_name': ('django.db.models.fields.CharField', [], {'max_length': '70'})
        }
    }

    complete_apps = ['picasabuttonizer']
