import pymongo
import os.path
import storage.impl as st

# myclient = pymongo.MongoClient("mongodb://localhost:27017/")

class Mongo_Connector:
    def __init__(self, db, collection, host):
        self.client = pymongo.MongoClient(host)
        self.db = self.client[db]
        self.collection = self.db[collection]
    
    def insert_all(self, saved_struct=[], mirror=False):
        if os.path.exists and mirror:
            st.commit("jsonfile")
        keys = []
        for k in self.find_all():
            keys.append(k["_id"])
        if saved_struct:
            for dic in saved_struct:
                if dic["_id"] not in keys:
                    self.collection.insert_one(dic)
                else:
                    update = { "_id": dic["_id"] }
                    newvalues = { "$set": dic }
                    self.collection.update_one(update, newvalues)

        if os.path.exists and mirror:
            st.saved = self.find_all()
            st.commit("jsonfile")


    def find_all(self):
        return list(self.collection.find())
    
    def drop(self, list_keys):
        current_keys = [x["_id"] for x in self.find_all()]
        print(current_keys)
        for _id in list_keys:
            delete = { "_id":  _id}
            if _id in current_keys:
                self.collection.delete_one(delete)
            else:
                return print(f"< No existe > {_id}")

    def get_keys(self):
        return [x["_id"] for x in self.find_all()]
