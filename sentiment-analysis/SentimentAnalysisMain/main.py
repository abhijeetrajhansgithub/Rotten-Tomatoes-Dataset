import csv
import json


def data_preprocessing():
    with open(r'../data/rotten_tomatoes_movie_reviews.csv', 'r') as csv_file:
        # convert all values in "id" to string
        csv_reader: csv.DictReader = csv.DictReader(csv_file)
        rows_: list = []
        for line in csv_reader:
            line['id'] = str(line['id'])
            rows_.append(line)
    return rows_


def filter_data(rows):
    movie_name_dict: dict = {}

    for line in rows:
        movie_id: str = line['id'].lower()
        if movie_id not in movie_name_dict:
            movie_name_dict[movie_id]: list = []
        movie_name_dict[movie_id].append(line['reviewText'])

    # print(movie_name_dict)
    # print(len(movie_name_dict))

    # save this dict to a json file
    with open(r'../data/movie_name_dict.json', 'w') as json_file:
        json.dump(movie_name_dict, json_file, indent=4)


if __name__ == '__main__':
    rows: list = data_preprocessing()
    filter_data(rows)
