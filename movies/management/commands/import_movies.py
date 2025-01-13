import csv
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Import movies from a CSV file'

    def handle(self, *args, **kwargs):
        # Path to CSV file
        with open('imdb_top_1000.csv', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                # Convert the data types as needed
                try:
                    movie = Movie(
                        poster_link=row['Poster_Link'],
                        series_title=row['Series_Title'],
                        released_year=int(row['Released_Year']),
                        certificate=row['Certificate'] if row['Certificate'] else None,
                        runtime=row['Runtime'],
                        genre=row['Genre'],
                        imdb_rating=float(row['IMDB_Rating']),
                        overview=row['Overview'],
                        meta_score=int(row['Meta_score']) if row['Meta_score'] else None,
                        director=row['Director'],
                        star1=row['Star1'],
                        star2=row['Star2'],
                        star3=row['Star3'],
                        star4=row['Star4'],
                        no_of_votes=int(row['No_of_Votes']),
                        gross=float(row['Gross'].replace(',', '')) if row['Gross'] else None,
                    )
                    movie.save()
                except Exception as e:
                    # Log any row that fails
                    self.stdout.write(self.style.WARNING(f"Error importing row {row['Series_Title']}: {str(e)}"))
                    continue

        self.stdout.write(self.style.SUCCESS('Successfully imported movies'))
