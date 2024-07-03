## Movie Recommender System

This is a content-based movie recommender system designed to provide personalized movie recommendations based on the content of movies users have liked previously.

### How it Works

The movie recommender system functions by following these steps:

1. **User Input**: Users provide movie titles about movies they have enjoyed in the past.

2. **Content Analysis**: The system then analyzes the content of the movies provided by the user. This involves extracting features such as genre, keywords from the plot summary, director, cast, and other relevant attributes.

3. **Similarity Calculation**: Using cosine similarity, the system compares the features of the input movies with those of other movies in the database.

4. **Recommendation Generation**: Based on the similarity scores, the system selects movies that are most similar to the ones provided by the user. These movies are then recommended to the user .

## Technologies Used

- **Python:** Backend development and machine learning implementation.
- **Streamlit**: Web framework for building the user interface.
- **Machine Learning:** Algorithms for movie recommendation.

## Note: 
similarity.pkl file is not uploaded in Model folder because its size is to large so run python notebook first to get the pickle file.
