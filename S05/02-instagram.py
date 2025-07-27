from instagrapi import Client

USERNAME = "test"
PASSWORD = "1234"
TARGET_USER = "fdmxfarhan"

cl = Client()
cl.login(USERNAME, PASSWORD)

# Get user id of the target account
user_id = cl.user_id_from_username(TARGET_USER)

# Get followers of the target account (limit to avoid spam)
followers = cl.user_followers(user_id, amount=50)

# Follow each follower
for follower_id in followers:
    try:
        cl.user_follow(follower_id)
        print(f"Followed: {follower_id}")
    except Exception as e:
        print(f"Failed to follow {follower_id}: {e}")
