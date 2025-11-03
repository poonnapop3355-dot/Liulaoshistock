import firebase_admin
from firebase_admin import credentials, db
import uuid

# Initialize Firebase
cred = credentials.Certificate("backend/firebase-credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://liulaoshistock-default-rtdb.asia-southeast1.firebasedatabase.app'
})

def seed_data():
    # Clear existing data
    db.reference('books').delete()
    db.reference('authors').delete()

    # Create authors
    author1_id = str(uuid.uuid4())
    author2_id = str(uuid.uuid4())
    db.reference(f'authors/{author1_id}').set({'id': author1_id, 'name': 'Author One'})
    db.reference(f'authors/{author2_id}').set({'id': author2_id, 'name': 'Author Two'})

    # Create books
    book1_id = str(uuid.uuid4())
    db.reference(f'books/{book1_id}').set({
        'id': book1_id,
        'isbn13': '978-0321765723',
        'title_th': 'The Lord of the Rings',
        'authors': [author1_id],
    })

    book2_id = str(uuid.uuid4())
    db.reference(f'books/{book2_id}').set({
        'id': book2_id,
        'isbn13': '978-0743273565',
        'title_th': 'The Hobbit',
        'authors': [author1_id, author2_id],
    })

    print("Data seeded successfully!")

if __name__ == '__main__':
    seed_data()
