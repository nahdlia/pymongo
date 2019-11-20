from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
from bson.objectid import ObjectId


class MongoDBManagement:
    def __init__(self):
        self.client = MongoClient('localhost', 27017)
        self.db = self.client['mongoDatabaseDemo']
        self.collection_patient = self.db['patients']
    
    def insert_one_patient(self):
        self.collection_patient.insert_one({
            "NAMA": input("MASUKKAN NAMA PASIEN: "),
            "UMUR" :input("MASUKKAN UMUR: "),
            "WALI": input("MASUKKAN NAMA WALI PASIEN: "),
            "ALAMAT": input("MASUKKAN ALAMAT: "),
        })
    
    # def delete_one_patient(self):
    #     self.collection_patient.delete_one({"NAMA": input("HAPUS PASIEN: ")})
if __name__ == "__main__":
    mongoDB = MongoDBManagement()
    mongoDB.insert_one_patient()
    # mongoDB.delete_one_patient()