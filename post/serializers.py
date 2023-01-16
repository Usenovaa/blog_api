from rest_framework import serializers
from .models import Category, Tag, Post


class CategorySerializer(
    serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('title',)


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ('title',)


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(
        source='author.name')

    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title):
        if self.Meta.model.objects.filter(
                title=title).exists():
            raise serializers.ValidationError(
                'Такой заголовок уже существует'
            )
        return title

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        tags = validated_data.pop('tags', [])
        post = Post.objects.create(author=user,
                        **validated_data)
        post.tags.add(*tags)
        return post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['title', 'slug',
                  'image', 'created_at']
