# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Student'
        db.create_table('student', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('studentID', self.gf('django.db.models.fields.IntegerField')()),
            ('last_name', self.gf('django.db.models.fields.TextField')()),
            ('first_name', self.gf('django.db.models.fields.TextField')()),
            ('middle_initial', self.gf('django.db.models.fields.TextField')()),
            ('year', self.gf('django.db.models.fields.IntegerField')()),
            ('sex', self.gf('django.db.models.fields.TextField')()),
            ('course', self.gf('django.db.models.fields.TextField')()),
            ('section', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('registration', ['Student'])

        # Adding model 'Event'
        db.create_table('event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.TextField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('registration', ['Event'])

        # Adding model 'Attend'
        db.create_table('attend', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('time', self.gf('django.db.models.fields.DateTimeField')()),
            ('student', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Student'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['registration.Event'])),
        ))
        db.send_create_signal('registration', ['Attend'])


    def backwards(self, orm):
        
        # Deleting model 'Student'
        db.delete_table('student')

        # Deleting model 'Event'
        db.delete_table('event')

        # Deleting model 'Attend'
        db.delete_table('attend')


    models = {
        'registration.attend': {
            'Meta': {'object_name': 'Attend', 'db_table': "'attend'"},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.Event']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'student': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['registration.Student']"}),
            'time': ('django.db.models.fields.DateTimeField', [], {})
        },
        'registration.event': {
            'Meta': {'object_name': 'Event', 'db_table': "'event'"},
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.TextField', [], {})
        },
        'registration.student': {
            'Meta': {'object_name': 'Student', 'db_table': "'student'"},
            'course': ('django.db.models.fields.TextField', [], {}),
            'first_name': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.TextField', [], {}),
            'middle_initial': ('django.db.models.fields.TextField', [], {}),
            'section': ('django.db.models.fields.TextField', [], {}),
            'sex': ('django.db.models.fields.TextField', [], {}),
            'studentID': ('django.db.models.fields.IntegerField', [], {}),
            'year': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['registration']
