from pymongo import MongoClient
import wikipedia

breeds = wikipedia.page('List_of_dog_breeds')
breeds_list = breeds.links

def check_valid_breed(page):
    if 'Dog breeds' in page.categories and len(dog_page.images) > 0:
        return True
    return False

client = MongoClient('mongodb://localhost:27017')
pawy_db = client['pawy']
breed_collection = pawy_db['breed']
breed_collection.delete_many({})

for breed in breeds_list:
    dog_page = wikipedia.page(breed)
    if check_valid_breed(dog_page):
        dog = {
            'name' : dog_page.title,
            'image' : dog_page.images[0],
            'description' : dog_page.content,
            'url' : dog_page.url
        }
        print('saving dog:', dog['name'])
        breed_collection.save(dog)
