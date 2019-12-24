from pprint import pprint
from pymongo import MongoClient
from pymongo import ReturnDocument
# from bson.objectid import ObjectId
import json
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while 1:
    # j = json.loads
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")
    patient_data = clientsocket.recv(1024).decode()
    data_obj = json.loads(patient_data)
    r = 'receive'
    clientsocket.send(r.encode())

    class MongoDBManagement:
        def __init__(self):
            self.client = MongoClient('localhost', 27017)
            self.db = self.client['mongoDatabaseDemo']
            self.collection_patient = self.db['patients']
        
        def insert_one_patient(self):
            self.collection_patient.insert_one(data_obj)
            print(data_obj)
        
        # def delete_one_patient(self):
            # self.collection_patient.delete_one({"NAMA": input("HAPUS PASIEN: ")})
    if __name__ == "__main__":
        mongoDB = MongoDBManagement()
        mongoDB.insert_one_patient()
        # mongoDB.delete_one_patient()