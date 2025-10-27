import json

class DataLoad:

    def json_load_register(self, file_name):
        with open(file_name) as f:
            data = json.load(f)
            return [
                (
                    item["name"],
                    item["email"],
                    item["password"],
                    item["phone"]
                )
                for item in data["users"]
            ]
            
            
            
    def json_load_login(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return [
                (
                    item["name"],
                    item["email"],
                    item["password"]
                )
                for item in data["users"]
            ]       
            
            
    def json_load_update(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return [
                (
                    item["updated_name"],
                    item["updated_phone"],
                    item["updated_password"],
                    item["filepath"]
                )
                for item in data["users"]
            ]               
            
            
    def json_load_review(self, filename):
        with open(filename) as f:
            data = json.load(f)
            return [
                (
                    item["review_name"],
                    item["review_email"],
                    item["review_text"]
                )
                for item in data["users"]
            ]                       