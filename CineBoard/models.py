from django.db import models



class Tag(models.Model):
    name = models.CharField(max_length=100, default='Романтика')



class Films(models.Model):
    GENRE = (
        ('Романтика', 'Романтика'),
        ('Боевик', 'Боевик')
    )

    title = models.CharField(max_length=100, default='фильм')
    description = models.TextField(default='Описание фильма')
    genre = models.CharField(max_length=100, choices=GENRE, default='Романтика')
    tags = models.ManyToManyField(Tag)
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    choice_post = models.ForeignKey(Films, on_delete=models.CASCADE,
                                    related_name='review')
    MARKS = (
        ('❤️', '❤️'),
        ('❤️❤️', '❤️❤️'),
        ('❤️❤️❤️', '❤️❤️❤️'),
        ('❤️❤️❤️❤️', '❤️❤️❤️❤️'),
        ('❤️❤️❤️❤️❤️', '❤️❤️❤️❤️❤️'),
    )
    choice_films = models.ForeignKey(Films, on_delete=models.CASCADE, related_name='rating')
    marks = models.CharField(max_length=100, choices=MARKS, default='❤️❤️❤️❤️')
    text = models.TextField(verbose_name='Напишите отзыв')
    created_at = models.DateTimeField(auto_now_add=True)


