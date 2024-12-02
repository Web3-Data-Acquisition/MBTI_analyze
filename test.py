import time
import tweepy

# 替换为你的 Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADOVuAEAAAAAepvUyZcEuzhGYwA3E9j2sXBgidA%3D0bK3m8IO6qQMb0vdqo0QAKFOGqIWzlpgYKTHlv6fLXhwXZXY5y"

# 初始化客户端
client = tweepy.Client(bearer_token=BEARER_TOKEN)


def get_user_id(username):
    while True:
        try:
            # 获取用户信息
            user = client.get_user(username=username)
            return user.data.id
        except tweepy.errors.TooManyRequests as e:
            # 获取速率限制的重置时间
            reset_time = int(e.response.headers.get("x-rate-limit-reset", time.time() + 15 * 60))
            wait_time = reset_time - int(time.time())
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)  # 等待限制重置后再重试
        except Exception as e:
            print(f"An error occurred: {e}")
            break


# 示例：获取用户 ID
username = "elonmusk"
user_id = get_user_id(username)
print(f"User ID for {username}: {user_id}")
