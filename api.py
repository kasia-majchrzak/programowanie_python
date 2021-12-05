import csv
import json

from flask import Flask
from flask_restful import reqparse, Api, Resource

from modules.Link import Link
from modules.Movie import Movie
from modules.Rating import Rating
from modules.Tag import Tag

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')

MOVIES: list = []
LINKS: list = []
RATINGS: list = []
TAGS: list = []


def getFileRows(path: str) -> list:
    result: list = []
    with open(path, 'r', encoding="utf8",
                newline='\n') as movies_csv_file:
        list_csv = csv.reader(movies_csv_file, delimiter=',', quotechar="\"")
        header = next(list_csv)
        for row in list_csv:
            result.append(row)
        return result


movies_csv = getFileRows("assets/movies.csv")
for row in movies_csv:
    MOVIES.append(Movie(int(row[0]), row[1], row[2]))


links_csv = getFileRows("assets/links.csv")
for row in links_csv:
    LINKS.append(Link(int(row[0]), row[1], row[2]))


ratings_csv = getFileRows("assets/ratings.csv")
for row in ratings_csv:
    RATINGS.append(Rating(int(row[0]), row[1], row[2], row[3]))


tags_csv = getFileRows("assets/tags.csv")
for row in tags_csv:
    TAGS.append(Tag(row[0], row[1], row[2], row[3]))


class MoviesList(Resource):
    def get(self):
        return [ob.__dict__ for ob in MOVIES]


class LinksList(Resource):
    def get(self):
        return [ob.__dict__ for ob in LINKS]


class RatingsList(Resource):
    def get(self):
        return [ob.__dict__ for ob in RATINGS]


class TagsList(Resource):
    def get(self):
        return [ob.__dict__ for ob in TAGS]


api.add_resource(MoviesList, '/movies', endpoint='movies')
api.add_resource(LinksList, '/links', endpoint='links')
api.add_resource(RatingsList, '/ratings', endpoint='ratings')
api.add_resource(TagsList, '/tags', endpoint='tags')

if __name__ == '__main__':
    app.run(debug=True)
