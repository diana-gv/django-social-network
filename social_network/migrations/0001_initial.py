# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'FriendRequest'
        db.create_table(u'social_network_friendrequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('from_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_outgoing_friend_requests', to=orm['auth.User'])),
            ('to_user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user_incoming_friend_requests', to=orm['auth.User'])),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social_network', ['FriendRequest'])

        # Adding model 'SocialGroup'
        db.create_table(u'social_network_socialgroup', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='groups_created_by', to=orm['auth.User'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('closed', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('social_network', ['SocialGroup'])

        # Adding M2M table for field administrators on 'SocialGroup'
        m2m_table_name = db.shorten_name(u'social_network_socialgroup_administrators')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('socialgroup', models.ForeignKey(orm['social_network.socialgroup'], null=False)),
            ('user', models.ForeignKey(orm[u'auth.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['socialgroup_id', 'user_id'])

        # Adding model 'GroupMembershipRequest'
        db.create_table(u'social_network_groupmembershiprequest', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('requester', self.gf('django.db.models.fields.related.ForeignKey')(related_name='requested_group_memberships', to=orm['auth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='aspirants', to=orm['social_network.SocialGroup'])),
            ('message', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('accepted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('social_network', ['GroupMembershipRequest'])

        # Adding model 'GroupComment'
        db.create_table(u'social_network_groupcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='(app_label)s_groupcomment_set_post', to=orm['auth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='(app_label)s_groupcomment_set_post', to=orm['social_network.SocialGroup'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('social_network', ['GroupComment'])

        # Adding model 'GroupImage'
        db.create_table(u'social_network_groupimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='(app_label)s_groupimage_set_post', to=orm['auth.User'])),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(related_name='(app_label)s_groupimage_set_post', to=orm['social_network.SocialGroup'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=500, null=True, blank=True)),
        ))
        db.send_create_signal('social_network', ['GroupImage'])

        # Adding model 'GroupFeedItem'
        db.create_table(u'social_network_groupfeeditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('group', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['social_network.SocialGroup'])),
            ('event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notifications.Event'])),
            ('template_config', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['notifications.NotificationTemplateConfig'])),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
        ))
        db.send_create_signal('social_network', ['GroupFeedItem'])

        # Adding model 'FeedComment'
        db.create_table(u'social_network_feedcomment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('creator', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feed_comments', to=orm['auth.User'])),
            ('receiver', self.gf('django.db.models.fields.related.ForeignKey')(related_name='feed_received_comments', to=orm['auth.User'])),
            ('comment', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('social_network', ['FeedComment'])


    def backwards(self, orm):
        # Deleting model 'FriendRequest'
        db.delete_table(u'social_network_friendrequest')

        # Deleting model 'SocialGroup'
        db.delete_table(u'social_network_socialgroup')

        # Removing M2M table for field administrators on 'SocialGroup'
        db.delete_table(db.shorten_name(u'social_network_socialgroup_administrators'))

        # Deleting model 'GroupMembershipRequest'
        db.delete_table(u'social_network_groupmembershiprequest')

        # Deleting model 'GroupComment'
        db.delete_table(u'social_network_groupcomment')

        # Deleting model 'GroupImage'
        db.delete_table(u'social_network_groupimage')

        # Deleting model 'GroupFeedItem'
        db.delete_table(u'social_network_groupfeeditem')

        # Deleting model 'FeedComment'
        db.delete_table(u'social_network_feedcomment')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'notifications.action': {
            'Meta': {'object_name': 'Action'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '200', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'read_as': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'notifications.event': {
            'Meta': {'object_name': 'Event'},
            'date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'details': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'extra_data': ('notifications.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']", 'null': 'True'}),
            'target_pk': ('django.db.models.fields.TextField', [], {}),
            'target_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'event'", 'to': u"orm['contenttypes.ContentType']"}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.EventType']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'events'", 'to': u"orm['auth.User']"})
        },
        'notifications.eventtype': {
            'Meta': {'object_name': 'EventType'},
            'action': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.Action']"}),
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.EventTypeCategory']", 'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'immediate': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'read_as': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'target_type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'notifications.eventtypecategory': {
            'Meta': {'object_name': 'EventTypeCategory'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'read_as': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'notifications.notificationtemplateconfig': {
            'Meta': {'unique_together': "(('event_type', 'transport', 'context'),)", 'object_name': 'NotificationTemplateConfig'},
            'context': ('django.db.models.fields.CharField', [], {'default': "u'default'", 'max_length': '255'}),
            'data': ('notifications.fields.JSONField', [], {'null': 'True', 'blank': 'True'}),
            'event_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.EventType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'single_template_path': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'template_path': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'transport': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.Transport']"})
        },
        'notifications.transport': {
            'Meta': {'object_name': 'Transport'},
            'allows_context': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allows_freq_config': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'allows_subscription': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'cls': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'delete_sent': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'sites.site': {
            'Meta': {'ordering': "(u'domain',)", 'object_name': 'Site', 'db_table': "u'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'social_network.feedcomment': {
            'Meta': {'object_name': 'FeedComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feed_comments'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'receiver': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'feed_received_comments'", 'to': u"orm['auth.User']"})
        },
        'social_network.friendrequest': {
            'Meta': {'object_name': 'FriendRequest'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'from_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_outgoing_friend_requests'", 'to': u"orm['auth.User']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'to_user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user_incoming_friend_requests'", 'to': u"orm['auth.User']"})
        },
        'social_network.groupcomment': {
            'Meta': {'object_name': 'GroupComment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'(app_label)s_groupcomment_set_post'", 'to': u"orm['auth.User']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'(app_label)s_groupcomment_set_post'", 'to': "orm['social_network.SocialGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'social_network.groupfeeditem': {
            'Meta': {'object_name': 'GroupFeedItem'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.Event']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['social_network.SocialGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['sites.Site']"}),
            'template_config': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['notifications.NotificationTemplateConfig']"})
        },
        'social_network.groupimage': {
            'Meta': {'object_name': 'GroupImage'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'(app_label)s_groupimage_set_post'", 'to': u"orm['auth.User']"}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'(app_label)s_groupimage_set_post'", 'to': "orm['social_network.SocialGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'})
        },
        'social_network.groupmembershiprequest': {
            'Meta': {'object_name': 'GroupMembershipRequest'},
            'accepted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'group': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'aspirants'", 'to': "orm['social_network.SocialGroup']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'message': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'requester': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'requested_group_memberships'", 'to': u"orm['auth.User']"})
        },
        'social_network.socialgroup': {
            'Meta': {'object_name': 'SocialGroup'},
            'administrators': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'groups_administrated_by'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['auth.User']"}),
            'closed': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'creator': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'groups_created_by'", 'to': u"orm['auth.User']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '500', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['social_network']