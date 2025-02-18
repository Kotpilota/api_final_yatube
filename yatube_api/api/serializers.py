from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post, Group, Follow

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""

    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'pub_date', 'image', 'group']


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""

    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'text', 'created', 'post']
        read_only_fields = ['post', 'author', 'created']


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""

    class Meta:
        model = Group
        fields = ['id', 'title', 'slug', 'description']


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for Follow model with validation rules."""

    user = SlugRelatedField(read_only=True, slug_field='username')
    following = SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ['user', 'following']

    def validate_following(self, value):
        """Prevent users from following themselves.

        Args:
            value (User): The user being followed.

        Raises:
            serializers.ValidationError: If the user is trying to follow
            themselves.

        Returns:
            User: The validated user.
        """
        user = self.context['request'].user
        if user == value:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя!"
            )
        return value

    def validate(self, data):
        """Prevent duplicate follow relationships.

        Args:
            data (dict): The input data.

        Raises:
            serializers.ValidationError: If the follow relationship already
            exists.

        Returns:
            dict: The validated data.
        """
        user = self.context['request'].user
        following = data.get('following')
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                "Вы уже подписаны на этого пользователя!"
            )
        return data

    def create(self, validated_data):
        """Assign the request user as the follower.

        Args:
            validated_data (dict): The validated data.

        Returns:
            Follow: The newly created Follow instance.
        """
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
