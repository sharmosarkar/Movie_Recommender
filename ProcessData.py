import numpy as np
import pandas as pd
import os
import graphlab

DATA_DIR = 'movie_dataset/ml-100k/'

_df = None


def get_original_dataframe():
    return _df


def create_train_test_SFrame(ratings_base, ratings_test):
    train_data = graphlab.SFrame(ratings_base)
    test_data = graphlab.SFrame(ratings_test)
    return train_data, test_data


def check_loaded_data(users, ratings, items, ratings_base, ratings_test):
    print 'user data : \n'
    print users.shape
    print users.head()
    print '\nrating data : \n'
    print ratings.shape
    print ratings.head()
    print '\nitem data : \n'
    print items.shape
    print items.head()
    print '\ntrain data : \n'
    print ratings_base.shape
    print ratings_base.head()
    print '\ntest data : \n'
    print ratings_test.shape
    print ratings_test.head()


def process_data(user_data_file, rating_data_file, item_rating_data, type='metadata',
                 rating_train=None, rating_test=None):
    if type == 'metadata':
        # Reading users file:
        u_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
        users = pd.read_csv(user_data_file, sep='|', names=u_cols,
                            encoding='latin-1')
        # Reading ratings file:
        r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
        ratings = pd.read_csv(rating_data_file, sep='\t', names=r_cols,
                              encoding='latin-1')
        # Reading items file:
        i_cols = ['movie id', 'movie title', 'release date', 'video release date', 'IMDb URL', 'unknown', 'Action',
                  'Adventure', 'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama', 'Fantasy',
                  'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi', 'Thriller', 'War', 'Western']
        items = pd.read_csv(item_rating_data, sep='|', names=i_cols,
                            encoding='latin-1')
        return users, ratings, items
    elif type == 'train_test_data':
        r_cols = ['user_id', 'movie_id', 'rating', 'unix_timestamp']
        ratings_base = pd.read_csv(rating_train, sep='\t', names=r_cols, encoding='latin-1')
        ratings_test = pd.read_csv(rating_test, sep='\t', names=r_cols, encoding='latin-1')
        return ratings_base, ratings_test


if __name__ == '__main__':
    data_file = os.path.join(DATA_DIR, 'u.data')
    process_data(data_file)
