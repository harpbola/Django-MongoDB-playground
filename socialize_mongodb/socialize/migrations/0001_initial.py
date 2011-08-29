# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Tag'
        db.create_table('socialize_tag', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('socialize', ['Tag'])

        # Adding model 'Posts'
        db.create_table('blog_posts', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('text', self.gf('django.db.models.fields.CharField')(max_length=1024)),
            ('date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal('socialize', ['Posts'])

        # Adding M2M table for field tags on 'Posts'
        db.create_table('blog_posts_tags', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('posts', models.ForeignKey(orm['socialize.posts'], null=False)),
            ('tag', models.ForeignKey(orm['socialize.tag'], null=False))
        ))
        db.create_unique('blog_posts_tags', ['posts_id', 'tag_id'])


    def backwards(self, orm):
        
        # Deleting model 'Tag'
        db.delete_table('socialize_tag')

        # Deleting model 'Posts'
        db.delete_table('blog_posts')

        # Removing M2M table for field tags on 'Posts'
        db.delete_table('blog_posts_tags')


    models = {
        'socialize.posts': {
            'Meta': {'object_name': 'Posts', 'db_table': "'blog_posts'"},
            'author': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['socialize.Tag']", 'symmetrical': 'False'}),
            'text': ('django.db.models.fields.CharField', [], {'max_length': '1024'})
        },
        'socialize.tag': {
            'Meta': {'object_name': 'Tag'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        }
    }

    complete_apps = ['socialize']
