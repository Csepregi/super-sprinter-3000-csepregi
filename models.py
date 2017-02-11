from peewee import *

db = PostgresqlDatabase('web_hazi', user='gabor')


class BaseModel(Model):

    class Meta:
        database = db


class UserStoryManager(BaseModel):
    title = CharField()
    story = TextField()
    criteria = TextField()
    business_value = IntegerField()
    estimation = FloatField()
    status = CharField()

    class Meta:
        order_by = ('id', 'title')