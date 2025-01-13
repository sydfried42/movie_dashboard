// movie_chart.js

function initMovieChart(movieData) {
    // Extracting release years and IMDb ratings from the movie data
    const releaseYears = movieData.map(movie => movie.released_year);
    const imdbRatings = movieData.map(movie => movie.imdb_rating);

    // Create a Chart.js line chart
    const ctx = document.getElementById('ratingChart').getContext('2d');
    const ratingChart = new Chart(ctx, {
        type: 'line',  // Line chart type
        data: {
            labels: releaseYears,  // X-axis (years)
            datasets: [{
                label: 'IMDb Rating',
                data: imdbRatings,  // Y-axis (ratings)
                borderColor: 'rgba(75, 192, 192, 1)',  // Line color
                backgroundColor: 'rgba(75, 192, 192, 0.2)',  // Fill color
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Release Year'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'IMDb Rating'
                    },
                    min: 0,
                    max: 10  // Ratings scale from 0 to 10
                }
            }
        }
    });
}

// Wait until the DOM is fully loaded before initializing the chart
document.addEventListener('DOMContentLoaded', function() {
    // Grab the movie_data from the global context (passed from Django view)
    const movieData = window.movieData;  // movieData is available globally
    initMovieChart(movieData);  // Initialize the chart with the movie data
});
