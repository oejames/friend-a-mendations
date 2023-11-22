from flask import Flask, render_template, request, jsonify

import requests

import json

from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()


port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)

app = Flask(__name__)

TMDB_API_KEY = os.getenv("API_KEY")

# Sample data

try:
    with open('library.json', 'r') as f:
        library = json.load(f)
except FileNotFoundError:
    library = {}


# library = {
#     'cheer_up': [
#         {'title': '27 Dresses', 'person': 'Alice', 'perfect_for': 'When you need a pick-me-up', 'reasoning': "It's kind of perfect for when you need to be cheered up "},
#         {'title': 'Feel-Good Suggestion 2', 'person': 'Bob', 'perfect_for': 'Anytime', 'reasoning': 'It always brings a smile to my face.'},
#         # Add more recommendations as needed
#     ],
#     'celebrate': [
#         {'title': 'Celebration Choice 1', 'person': 'Charlie', 'perfect_for': 'Special occasions', 'reasoning': 'Great for celebrating achievements.'},
#         # Add more recommendations as needed
#     ],
# }

filters = {
    'cheer_up': 'When You Need Cheering Up',
    'laugh': 'When You Need to Laugh',
    'fall_in_love': 'When You Want To Fall In Love',
    'sad': 'When You Need To Cry'

    # Add more categories as needed
}

@app.route('/')
def index():
    return render_template('index.html', filters=filters)

@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    selected_type = request.form.get('type')

    if selected_type not in library:
        return "Invalid request"

    selected_recommendations = library[selected_type]

    # Get a random recommendation
    random_recommendation = selected_recommendations[0]  # For simplicity, we'll just pick the first recommendation

    return render_template('recommendation.html', recommendation=random_recommendation)




@app.route('/get_movie_details', methods=['POST'])
def get_movie_details():
    movie_title = request.form.get('movie_title')

    # Make a request to TMDb API to get movie details
    tmdb_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}'
    
    try:
        response = requests.get(tmdb_url)
        response.raise_for_status()  # Check for errors in the response
        data = response.json()

        # Extract relevant movie details
        if data['results']:
            movie_details = [
                {
                    'title': movie['title'],
                    'image_url': f"https://image.tmdb.org/t/p/w500/{movie['poster_path']}",
                }
                for movie in data['results']
            ]
        else:
            movie_details = None

        return jsonify({'movie_details': movie_details})
    except requests.exceptions.RequestException as e:
        print(f"Error in TMDb API request: {e}")
        return jsonify({'movie_details': None})




@app.route('/get_library', methods=['POST'])
def get_library():
    selected_type = request.form.get('type')

    if selected_type not in library:
        return "Invalid request"

    selected_recommendations = library[selected_type]

    # Render the library HTML with friend-a-mendations
    library_html = render_template('library.html', filters=filters, recommendations=library)
    return jsonify({'library_html': library_html})



@app.route('/add_recommendation', methods=['POST'])
def add_recommendation():
    movie_title = request.form.get('movie_title')
    category = request.form.get('category')
    recommendation = request.form.get('recommendation')
    initials = request.form.get('initials')

    # Make a request to TMDb API to get movie details
    tmdb_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&query={movie_title}'
    response = requests.get(tmdb_url)
    data = response.json()

    # Extract relevant movie details
    if data['results']:
        movie_details = {
            'title': data['results'][0]['title'],
            'image_url': f"https://image.tmdb.org/t/p/w500/{data['results'][0]['poster_path']}",
        }
    else:
        movie_details = None

    if category in filters:  # Check if the category is one of the pre-made categories
        if category in library:
            library[category].append({
                'title': movie_title,
                'person': initials, 
                'perfect_for': category, 
                'reasoning': recommendation,
                'image_url': movie_details['image_url'] if movie_details else None  # Include the image URL
            })
        else:
            library[category] = [{
                'title': movie_title,
                'person': initials, 
                'perfect_for': category, 
                'reasoning': recommendation,
                'image_url': movie_details['image_url'] if movie_details else None  # Include the image URL
            }]
        # Save the updated library to a file
        with open('library.json', 'w') as f:
            json.dump(library, f)
        return "Recommendation added successfully"
    elif category.lower() == 'other/new':  # Allow users to type in a new category
        # Add logic to handle adding a new category
        # You can prompt the user to enter a new category and add it to the filters
        return "New category added successfully"
    else:
        return "Invalid category"


@app.route('/add_recommendation_page')
def add_recommendation_page():
    return render_template('add_recommendation_page.html', filters=filters)



if __name__ == '__main__':
    app.run(debug=True)
