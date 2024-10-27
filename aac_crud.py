from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.objectid import ObjectId

class AnimalShelter:
  """CRUD Operations for a specified collection in MongoDB"""

  def __init__(self, user, password, host, port, db, collection):
      """Initialize the MongoDB client"""
      try:
          self.client = MongoClient(f'mongodb://{user}:{password}@{host}:{port}')
          self.database = self.client[db]
          self.collection = self.database[collection]
      except PyMongoError as e:
          print(f"Error connecting to MongoDB: {e}")
          self.client = None

  def create(self, data):
      """Insert a document into the collection"""
      if data is not None:
          try:
              result = self.collection.insert_one(data)
              return result.acknowledged
          except PyMongoError as e:
              print(f"Error inserting document: {e}")
              return False
      else:
          raise ValueError("Data parameter is empty")

  def read(self, query):
      """Query documents from the collection"""
      try:
          cursor = self.collection.find(query)
          return list(cursor)
      except PyMongoError as e:
          print(f"Error querying documents: {e}")
          return []

  def update(self, query, update_data):
      """Update document(s) in the collection"""
      if query is not None and update_data is not None:
          try:
              result = self.collection.update_many(query, {'$set': update_data})
              return result.modified_count
          except PyMongoError as e:
              print(f"Error updating documents: {e}")
              return 0
      else:
          raise ValueError("Query and update_data parameters must not be empty")

  def delete(self, query):
      """Delete document(s) from the collection"""
      if query is not None:
          try:
              result = self.collection.delete_many(query)
              return result.deleted_count
          except PyMongoError as e:
              print(f"Error deleting documents: {e}")
              return 0
      else:
          raise ValueError("Query parameter is empty")
