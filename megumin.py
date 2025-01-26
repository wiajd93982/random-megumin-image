import requests
from flask import Flask, render_template_string

app = Flask(__name__)


def get_random_megumin_image_from_api():
    url = "https://safebooru.donmai.us/posts.json?tags=megumin&limit=1&random=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data and len(data) > 0 and "file_url" in data[0]:
            return data[0]["file_url"]
    return None


@app.route("/random-megumin")
def random_megumin():
    image_url = get_random_megumin_image_from_api()
    if image_url:
        # Return an HTML page with the image embedded
        html_content = f'<html><body><h1>Random Megumin Image</h1><img src="{image_url}" alt="Megumin" /></body></html>'
        return render_template_string(html_content)
    return "Failed to fetch image", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
