from dotenv import load_dotenv
import requests
import os

load_dotenv()

# load env variables
access_token:str = os.getenv("ACCESS_TOKEN")
page_id:str = os.getenv("PAGE_ID")  # ! This is for the watches page
base_url = f'https://graph.facebook.com/{page_id}/posts?access_token={access_token}'

def get_likes_for_post(post_id):
    url = f'https://graph.facebook.com/{post_id}/insights?metric=post_reactions_like_total&access_token={access_token}'
    response = requests.get(url)
    data = response.json()
    
    # Extract the value
    lifetime_like_value = None
    for item in data['data']:
        if item['period'] == 'lifetime':
            lifetime_like_value = item['values'][0]['value']
            break
    
    return lifetime_like_value

def get_all_posts():
    posts = []
    url = base_url
    while url:
        response = requests.get(url)
        data = response.json()
        posts.extend(data['data'])
        url = data.get('paging', {}).get('next')
    return posts

def get_all_likes():
    posts = get_all_posts()
    all_likes = {}
    for post in posts:
        post_id = post['id']
        likes = get_likes_for_post(post_id)
        all_likes[post_id] = likes
    return all_likes

all_likes = get_all_likes()
total_likes = 0
for post_id, likes in all_likes.items():
    print(f'Post ID: {post_id}')
    # for user in likes:
    #     print(user['name'])
    total_likes += likes

print("Total Lifetime Likes: ", total_likes)