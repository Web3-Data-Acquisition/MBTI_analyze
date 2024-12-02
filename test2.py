import requests
import time

# 替换为你的 Bearer Token
BEARER_TOKEN = "AAAAAAAAAAAAAAAAAAAAADOVuAEAAAAAepvUyZcEuzhGYwA3E9j2sXBgidA%3D0bK3m8IO6qQMb0vdqo0QAKFOGqIWzlpgYKTHlv6fLXhwXZXY5y"


def get_user_id(username):
    url = f"https://api.twitter.com/2/users/by/username/{username}"
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}"
    }

    while True:
        response = requests.get(url, headers=headers)

        # 如果请求成功
        if response.status_code == 200:
            data = response.json()
            return data['data']['id']

        # 如果遇到速率限制
        elif response.status_code == 429:
            reset_time = int(response.headers.get("x-rate-limit-reset", time.time() + 15 * 60))
            wait_time = reset_time - int(time.time())
            print(f"Rate limit exceeded. Waiting for {wait_time} seconds...")
            time.sleep(wait_time)

        # 其他错误
        else:
            print(f"Error: {response.status_code} - {response.text}")
            break


# 示例：获取用户 ID
username = "guigudao"
user_id = get_user_id(username)
if user_id:
    print(f"User ID for {username}: {user_id}")
else:
    print("Failed to fetch user ID.")
