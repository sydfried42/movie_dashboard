from django.db import models

class Movie(models.Model):
    # Image link for the movie poster
    poster_link = models.URLField(max_length=200, blank=True, null=True)
    
    # Title of the movie/TV show
    series_title = models.CharField(max_length=255)
    
    # Year the movie was released
    released_year = models.PositiveIntegerField()
    
    # Certification/Rating from boards (e.g., A, U, PG)
    certificate = models.CharField(max_length=10, blank=True, null=True)
    
    # Runtime in minutes (e.g., 142 min)
    runtime = models.CharField(max_length=50)
    
    # Genres associated with the movie
    genre = models.CharField(max_length=100)
    
    # IMDB rating (out of 10)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)
    
    # Movie overview/description
    overview = models.TextField()
    
    # Meta score (critics rating)
    meta_score = models.PositiveIntegerField(blank=True, null=True)
    
    # Director of the movie
    director = models.CharField(max_length=255)
    
    # Main stars/actors in the movie
    star1 = models.CharField(max_length=255)
    star2 = models.CharField(max_length=255)
    star3 = models.CharField(max_length=255)
    star4 = models.CharField(max_length=255)
    
    # Number of votes on IMDB
    no_of_votes = models.PositiveIntegerField()
    
    # Gross earnings (box office revenue)
    gross = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    
    # Date the movie was added to the database
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.series_title

    class Meta:
        # To ensure movies are sorted by their release year (descending)
        ordering = ['-released_year']
