from mongoengine import connect, Document, IntField, StringField, FloatField, DateTimeField

database_name = 'sanjob'
MONGO_INITDB_ROOT_USERNAME = 'sanjob'
MONGO_INITDB_ROOT_PASSWORD = 'pass4san!'
AUTHENTICATIONDATABASE = 'admin'
host = 'localhost'
database_port = 27017


def connect_database():
    connect(database_name, host=host, port=int(database_port))


# Process collection to store function runs system usage
class Threads(Document):
    thread_id = IntField(required=True)
    title = StringField(required=True)
    question = StringField()
    last_post = IntField()
    page_number = IntField()


class Answers(Document):
    thread_id = IntField(required=True)
    answer = StringField()


def write_threads(thread_id, title, question, last_post, pagenumber):
    post = Threads(thread_id=thread_id,
                   title=title,
                   question=question,
                   last_post=last_post,
                   page_number=pagenumber)
    post.save()


def write_answers(thread_id, answer):
    post = Answers(thread_id=thread_id, answer=answer)
    post.save()


def get_threads_ids():
    ids = []
    for entry in Threads.objects:
            ids.append(entry['thread_id'])
    return ids
