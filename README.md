🎬 Movie Recommender Website 

A full-featured movie recommendation web app built with React, Streamlit, and Supabase. Users can search for movies, get recommendations, scroll through an interactive list, and even stream selected titles.

 Features

- Searchable Movie Catalog – Instantly find movies by title using a fast, responsive interface.
- Search for Recommendations – Get smart recommendations based on movie similarity using a precomputed similarity matrix. Recommendations are driven by feature similarity such as genre, keywords, cast, and description.
- Poster & Metadata Fetching – Visual results fetched dynamically via TMDb and Supabase APIs.

 How the recommendation algorithms Works

- A similarity matrix (`similarity.pkl`) is generated based on metadata tags using TF-IDF and cosine similarity.
- The backend is built with Streamlit to load and serve recommendations efficiently.
- Posters and media assets are retrieved through Supabase API and TMDb API integrations.
- The frontend is developed in React, allowing users to search, filter, and scroll fluidly through the movie list.

 🛠️ Tech Stack

| Frontend      | Backend          |        API     | Data Tools       |
|---------------|------------------|----------------|------------------|
| React         | Streamlit        | TMDb API       | Scikit-learn     |
| JavaScript    | Python           | Supabase       | Pandas           |
| Tailwind CSS  | Flask            |                | Pickle (for data)|


