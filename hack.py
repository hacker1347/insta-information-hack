import requests
from bs4 import BeautifulSoup

def get_instagram_info(username):
    url = f"https://www.instagram.com/{username}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Holen Sie die Anzahl der Follower
    followers_element = soup.find("span", class_="g11s5")
    followers = int(followers_element.text.strip("\n").strip())

    # Holen Sie die Anzahl der Followings
    followings_element = soup.find("span", class_="g11s5", id="followings_count")
    followings = int(followings_element.text.strip("\n").strip())

    # Holen Sie den Namen des Kontos
    user_name_element = soup.find("h1", class_="_4-UF _22_x")
    user_name = user_name_element.text.strip()

    # Holen Sie das Bild der Profilseite
    profile_picture_element = soup.find("img", class_="_1drn _1drn-error _4-u8 _4-u7 _4-u8 _4-u7")
    profile_picture_url = profile_picture_element["src"]

    return {
        "followers": followers,
        "followings": followings,
        "user_name": user_name,
        "profile_picture_url": profile_picture_url
    }

def main():
    username = "your_username"
    instagram_info = get_instagram_info(username)

    print(f"Followers: {instagram_info['followers']}")
    print(f"Followings: {instagram_info['followings']}")
    print(f"User Name: {instagram_info['user_name']}")
    print(f"Profile Picture URL: {instagram_info['profile_picture_url']}")

if __name__ == "__main__":
    main()
