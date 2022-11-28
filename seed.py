"""Seed file to make sample data for users db. We will
execute this seed.py before we run app.py"""

from models import User, db, Post, Tag, PostTag
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()
PostTag.query.delete()
Tag.query.delete()

# Add users
user1 = User(first_name='Tom', last_name="Brady")
user2 = User(first_name='John', last_name="Smith")
user3 = User(first_name='Sandy', last_name="Duncan")

#add Posts
post1 = Post(title='First post', content = "I love my day", users=user1 )
post2 = Post(title='Yet Another Post', content = "I love my family", users=user2)
post3 = Post(title='Flask Is Awesome', content = "I learn Flask everyday", users=user3)
db.session.add_all([user1, user2, user3, post1, post2, post3])
db.session.commit()


tag1= Tag(id =1,name = "Fun", post_tags =[PostTag(post_id = post1.id)])
tag2 = Tag(id=2, name= "Even more", post_tags =[PostTag(post_id = post2.id)])
tag3 = Tag(id =3, name= "Bloop", post_tags =[PostTag(post_id = post3.id)])


# Add new objects to session, so they'll persist
db.session.add_all([tag1, tag2, tag3])

# Commit--otherwise, this never gets saved!
db.session.commit()


