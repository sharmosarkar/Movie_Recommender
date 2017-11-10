import os
import ProcessData
import Recommender
import Evaluation as Eval

DATA_DIR = 'movie_dataset/ml-100k/'


def train():
    user_data_file = os.path.join(DATA_DIR, 'u.user')
    rating_data_file = os.path.join(DATA_DIR, 'u.data')
    item_rating_data = os.path.join(DATA_DIR, 'u.item')
    rating_train_data = os.path.join(DATA_DIR, 'ua.base')
    rating_test_data = os.path.join(DATA_DIR, 'ua.test')
    users, ratings, items = ProcessData.process_data(user_data_file, rating_data_file, item_rating_data,
                                                     type='metadata')
    ratings_base, ratings_test = ProcessData.process_data(None, None, None, 'train_test_data',
                                                          rating_train_data, rating_test_data)
    # ProcessData.check_loaded_data(users, ratings, items, ratings_base, ratings_test)
    train_data, test_data = ProcessData.create_train_test_SFrame(ratings_base, ratings_test)
    popularity_model, item_sim_model = Recommender.train_models(train_data, users, items)
    return popularity_model, item_sim_model, users, items


def predict(user_id, number_reco):
    popularity_model, item_sim_model, users, items = Recommender.load_models()
    # Recommender.predict_popularity(popularity_model, range(1, 6), 5)
    # Recommender.predict_CF_item_sim(item_sim_model, range(1, 6), 5)
    item_sim_recomm = Recommender.predict_CF_item_sim(item_sim_model, user_id, number_reco)
    movie_list = Recommender.decipher_predictions(item_sim_recomm, users, items, number_reco)
    print '\nMovie recommendations for user_id = ' + str(user_id) + ' are : \n'
    for itm in range(0, number_reco):
        movie = movie_list[itm]
        print movie['movie_id'], movie['movie_name'], movie['movie_genre']

def main():
    # model based Collaborative Prediction
    # popularity_model, item_sim_model, users, items = train()
    predict(5, 5)


if __name__ == '__main__':
    main()
