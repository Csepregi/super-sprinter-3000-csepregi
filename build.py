from models import *
from example_data import *


def build_tables():
    db.connect()
    db.drop_table(UserStoryManager, cascade=True)
    db.create_table(UserStoryManager)
    generate_data()

