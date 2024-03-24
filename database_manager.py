import json
from pymongo import MongoClient

def regions():
    with open("Data\\data.json", "r") as f:
        data = json.load(f)
    return list(data.keys())

class DatabaseManager:
    def __init__(self):
        self.client = MongoClient("localhost", 27017)
        self.database = self.client["your_database_name"]

    def create_table(self):
        pass # No need to create tables in MongoDB, as it's schema-less

    def add_data(self, table_name, **kwargs):
        self.database[table_name].insert_one(kwargs)

    def get_existing_relations(self):
        result = self.database["student_advisor"].find()
        return [(i['student_id'], i['advisor_id'],) for i in result]

    def delete_row(self, table_name, row_id):
        if table_name == "advisors":
            self.database[table_name].delete_one({"advisor_id": row_id})
        else:
            self.database[table_name].delete_one({"student_id": row_id})

    def load_data(self, table_name):
        return list(self.database[table_name].find())

    def search(self, table_name, **kwargs):
        return list(self.database[table_name].find(kwargs))

    def update(self, table_name, row_id, **kwargs):
        if table_name == "students":
            self.database[table_name].update_one({"student_id": row_id}, {"$set": kwargs})
        elif table_name == "advisors":
            self.database[table_name].update_one({"advisor_id": row_id}, {"$set": kwargs})

    def check_bd(self):
        return self.database["student_advisor"].count_documents({}) == 0

    def list_advisors_with_students_count(self, order_by):
        pipeline = [
            {"$lookup": {"from": "student_advisor", "localField": "advisor_id", "foreignField": "advisor_id", "as": "students"}},
            {"$addFields": {"student_count": {"$size": "$students"}}},
            {"$project": {"advisor_id": 1, "name": 1, "surname": 1, "student_count": 1}},
            {"$sort": {"student_count": order_by}}
        ]
        return list(self.database["advisors"].aggregate(pipeline))

    def list_students_with_advisors_count(self, order_by):
        pipeline = [
            {"$lookup": {"from": "student_advisor", "localField": "student_id", "foreignField": "student_id", "as": "advisors"}},
            {"$addFields": {"advisor_count": {"$size": "$advisors"}}},
            {"$project": {"student_id": 1, "name": 1, "surname": 1, "advisor_count": 1}},
            {"$sort": {"advisor_count": order_by}}
        ]
        return list(self.database["students"].aggregate(pipeline))
