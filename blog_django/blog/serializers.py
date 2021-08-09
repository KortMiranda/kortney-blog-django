from rest_framework import serializers
from rest_framework.relations import HyperlinkedRelatedField
from .models import Post, Comment
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class CommentSerializer(serializers.ModelSerializer):
    # post = serializers.HyperlinkedRelatedField(
    #     view_name='post',
    #     read_only=True
    # )

    # post_id = serializers.PrimaryKeyRelatedField(
    #     queryset=Post.objects.all(),
    #     source='post'
    # )
    class Meta:
        model = Comment
        fields = ('id','name', 'message', )

class PostSerializer(TaggitSerializer, serializers.HyperlinkedModelSerializer):

    tags = TagListSerializerField()
    comments = CommentSerializer(many=True)

    class Meta:
        model = Post
        fields = ('id', 'image', 'title', 'content', 'comments', 'tags', 'natural_time')

