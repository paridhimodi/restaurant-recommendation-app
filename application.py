import pandas as pd
from flask import Flask, render_template, request
from sklearn.metrics.pairwise import linear_kernel
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from flask_cors import cross_origin

os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

def create_similarity():
    data = pd.read_csv('model_df')


    # creating a count matrix
    tfidf = TfidfVectorizer(analyzer='word', ngram_range=(1, 2), min_df=0, stop_words='english')
    tfidf_matrix = tfidf.fit_transform(data['reviews_list'].values.astype('U'))

    similarity = linear_kernel(tfidf_matrix, tfidf_matrix)
    return data,similarity


def rcmd(m):
    m = m.lower()

    data, similarity = create_similarity()
    data = pd.read_csv('model_df')
    indices = list(data.name)

    # Create a list to put top restaurants
    recommend_restaurant = []

    # Find the index of the hotel entered
    idx = indices.index(m)

    # Find the restaurants with a similar cosine-sim value and order them from bigger number
    score_series = pd.Series(similarity[idx]).sort_values(ascending=False)

    # Extract top 3 restaurant indexes with a similar cosine-sim value
    top3_indexes = list(score_series.iloc[1:3].index)
    tit = data['name'].iloc[top3_indexes]
    cuisine = data['cuisines'].iloc[top3_indexes]
    rating = data['rating'].iloc[top3_indexes]

    return_df = pd.DataFrame(columns=['name', 'cuisines', 'rating', 'cost'])
    return_df['name'] = tit
    return_df['cuisines'] = cuisine
    return_df['rating'] = rating

    return return_df

application= Flask(__name__, template_folder='templates')
@application.route('/')
@cross_origin()
def home():
    return render_template('index.html')
# Set up the main route
@application.route('/predict', methods=['GET', 'POST'])
@cross_origin()
def main():

    if request.method == 'POST':
        m_name = request.form['name']
        m_name = m_name.title()


        result_final = rcmd(m_name)
        names = []
        cuisines = []
        rating = []

        for i in range(len(result_final)):
            names.append(result_final.iloc[i][0])
            cuisines.append(result_final.iloc[i][1])
            rating.append(result_final.iloc[i][2])


            return render_template('index.html', names="You may like {}".format(names),cuisines="It's cuisine : {}".format(cuisines),rating = "It's rating : {}".format(rating), search_name=m_name)

    return render_template("index.html")


if __name__ == "__main__":
    # application.run(debug=True)
    application.run(host='127.0.0.1', port=8000, debug=True)
# port = int(os.getenv("PORT", 8000))
# if __name__ == "__main__":
#     application.run(port=port, debug=True)
