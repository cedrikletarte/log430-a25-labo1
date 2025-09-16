"""
User DAO (Data Access Object)
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""
import os
from dotenv import load_dotenv
import pymongo
from bson import ObjectId
from models.user import User

class UserDAOMongo:
    def __init__(self):
        try:
            env_path = "../.env"
            print(os.path.abspath(env_path))
            load_dotenv(dotenv_path=env_path)
            db_host = os.getenv("MONGODB_HOST")
            db_user = os.getenv("DB_USERNAME")
            db_pass = os.getenv("DB_PASSWORD")
            db_name = os.getenv("MONGODB_DB_NAME", "user_database")

            self.client = pymongo.MongoClient(host=db_host, username=db_user, password=db_pass)
            self.db = self.client[db_name]

        except FileNotFoundError:
            print("Attention : Veuillez créer un fichier .env")
        except Exception as e:
            print("Erreur : " + str(e))

    def select_all(self):
        """ Select all users from MongoDB """
        users = self.db.users.find()
        result = []
        for doc in users:
            user_id = str(doc.get('_id')) if doc.get('_id') else None
            name = doc.get('name')
            email = doc.get('email')
            result.append(User(user_id, name, email))
        return result

    def insert(self, user):
        """ Insert given user into MongoDB """
        # Préparer le document sans user_id
        user_doc = {
            "name": user.name,
            "email": user.email,
        }
        result = self.db.users.insert_one(user_doc)
        return result.inserted_id

    def update(self, user):
        """ Update given user in MongoDB """
        if not user.id:
            return 0
        result = self.db.users.update_one(
            {"_id": ObjectId(user.id)},
            {"$set": {"name": user.name, "email": user.email}}
        )
        return result.modified_count

    def delete(self, user_id):
        """ Delete user from MongoDB with given user ID """
        print(f"Deleting user with ID: {user_id}")
        result = self.db.users.delete_one({"_id": user_id})
        return result.deleted_count

    def delete_all(self):
        """ Empty users collection in MongoDB """
        result = self.db.users.delete_many({})
        return result.deleted_count

    def close(self):
        self.client.close()
