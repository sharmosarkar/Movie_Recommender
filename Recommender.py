import graphlab
import os
import pandas as pd

MODEL_DIR = 'model'


def predict_popularity(popularity_model, users, k):
    if isinstance(users, list):
        popularity_recomm = popularity_model.recommend(users=users, k=5)
        popularity_recomm.print_rows(num_rows=25)
    else:
        print "SSS  :  ", type(users)


def predict_CF_item_sim(item_sim_model, users, k):
    if not isinstance(users, list):
        users_lst = list()
        users_lst.append(users)
    else:
        users_lst = users
    item_sim_recomm = item_sim_model.recommend(users_lst, k=k)
    # item_sim_recomm.print_rows(num_rows=k)
    return item_sim_recomm


def decipher_predictions(item_sim_recomm, users, items, k):
    deciphered_list = list()
    for reco in range(0, k):
        # print item_sim_recomm[1]
        movie_id = item_sim_recomm[reco]['movie_id']
        # print 'movie_id : ', movie_id
        movie = items[items['movie id'] == movie_id]
        df_index = int(movie_id) - 1
        movie_title = movie.get_value(df_index, 'movie title')
        # print 'movie_title : ', movie_title
        movie_genre = (movie == 1).idxmax(axis=1)
        # print 'movie genre : ', movie_genre
        deciphered = {'movie_id': movie_id, 'movie_name': movie_title, 'movie_genre': movie_genre}
        deciphered_list.append(deciphered)
    return deciphered_list


def train_models(train_data, user, item):
    popularity_model = graphlab.popularity_recommender.create(train_data, user_id='user_id',
                                                              item_id='movie_id', target='rating')
    # train the item-item similarity model
    item_sim_model = graphlab.item_similarity_recommender.create(train_data, user_id='user_id', item_id='movie_id',
                                                                 target='rating', similarity_type='pearson')
    # save models
    popularity_model_path = os.path.join(MODEL_DIR, 'popularity', 'popularity_model')
    item_model_path = os.path.join(MODEL_DIR, 'item', 'item_model')
    graphlab.popularity_recommender.PopularityRecommender.save(popularity_model, popularity_model_path)
    graphlab.item_similarity_recommender.ItemSimilarityRecommender.save(item_sim_model, item_model_path)
    user_pkl_path = os.path.join(MODEL_DIR, 'user.pkl')
    item_pkl_path = os.path.join(MODEL_DIR, 'item.pkl')
    user.to_pickle(user_pkl_path)
    item.to_pickle(item_pkl_path)
    return popularity_model, item_sim_model


def load_models():
    popularity_model_path = os.path.join(MODEL_DIR, 'popularity', 'popularity_model')
    item_model_path = os.path.join(MODEL_DIR, 'item', 'item_model')
    popularity_model = graphlab.load_model(popularity_model_path)
    item_model = graphlab.load_model(item_model_path)
    user_pkl_path = os.path.join(MODEL_DIR, 'user.pkl')
    item_pkl_path = os.path.join(MODEL_DIR, 'item.pkl')
    users = pd.read_pickle(user_pkl_path)
    items = pd.read_pickle(item_pkl_path)
    return popularity_model, item_model, users, items
