from models import *


def generate_data():
    data_UserStoryManager = [
        {'title': 'Find interview', 'story': 'find posibility',
         'criteria': 'get it', 'business_value': 100,
         'estimation': 1.5, 'status':'progress'},

        {'title': 'Find applicant', 'story': 'just the best',
         'criteria': 'search', 'business_value': 200,
         'estimation': 2, 'status': 'progress'}
    ]

    with db.atomic():
        UserStoryManager.insert_many(data_UserStoryManager).execute()
