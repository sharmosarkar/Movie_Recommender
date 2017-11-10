import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = 'DATA'


def read_data(books_csv, user_csv, ratings_csv):
    # load books data
    books_data = os.path.join(data_dir, books_csv)
    books = pd.read_csv(books_data, sep=';', error_bad_lines=False, encoding="latin-1", low_memory=False)
    books.columns = ['ISBN', 'bookTitle', 'bookAuthor', 'yearOfPublication', 'publisher', 'imageUrlS', 'imageUrlM',
                     'imageUrlL']
    # load user data
    user_data = os.path.join(data_dir, user_csv)
    users = pd.read_csv(user_data, sep=';', error_bad_lines=False, encoding="latin-1", low_memory=False)
    users.columns = ['userID', 'Location', 'Age']
    # load ratings data
    ratings_data = os.path.join(data_dir, ratings_csv)
    ratings = pd.read_csv(ratings_data, sep=';', error_bad_lines=False, encoding="latin-1", low_memory=False)
    ratings.columns = ['userID', 'ISBN', 'bookRating']
    return books, users, ratings


def show_data_stats(ratings, users):
    # ratings histogram
    plt.rc("font", size=12)
    ratings.bookRating.value_counts(sort=False).plot(kind='bar')
    plt.title('Rating Distribution\n')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    plt.savefig('book_rating_distribution.png', bbox_inches='tight')
    plt.show()
    # users histogram
    users.Age.hist(bins=[0, 19, 26, 30, 46, 50, 100])
    plt.title('Age Distribution\n')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.savefig('system2.png', bbox_inches='tight')
    plt.show()


def main():
    books_csv = 'BX-Books.csv'
    user_csv = 'BX-Users.csv'
    ratings_csv = 'BX-Book-Ratings.csv'
    books, users, ratings = read_data(books_csv, user_csv, ratings_csv)
    show_data_stats(ratings, users)


if __name__ == '__main__':
    main()
