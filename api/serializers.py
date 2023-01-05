from rest_framework import serializers

from books.models import Author, Book, Genre, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('name', 'about', )


class BookSerializer(serializers.ModelSerializer):
    # cover = serializers.SerializerMethodField()
    #
    # def get_cover(self, obj):
    #     return obj.get_cover_display()

    author = serializers.CharField(source='author.name')
    cover = serializers.CharField(source='get_cover_display')
    genre = serializers.SlugRelatedField(
            many=True,
            read_only=True,
            slug_field='name'
    )

    class Meta:
        model = Book
        fields = (
            'title', 'author', 'description', 'genre', 'language', 'cover',
            'price', 'publisher', 'isbn', 'pages', 'quantity',
        )


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'description', )


class ReviewSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=150)
    description = serializers.CharField(max_length=5000)
    mark = serializers.IntegerField(min_value=1, max_value=5)
    created = serializers.DateTimeField()
    edited = serializers.DateTimeField()

    def create(self, validated_data):
        print('\n\n')
        print(validated_data)
        print('\n\n')
        return Review.objects.create(**validated_data)

    # def update(self, instance, validated_data):


    # class Meta:
    #     model = Review
    #     fields = ('title', 'book', 'description', 'author', 'mark', )
