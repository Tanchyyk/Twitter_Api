from flask import Flask, render_template, request
from Twitter_Api.get_jsons import get_json
from Twitter_Api.get_location import add_users_coordinates, get_users_location
from Twitter_Api.put_users_on_map import put_users_on_map

app = Flask(__name__)


@app.route('/', methods=["GET"])
def opening_page():
    return render_template('opening_page.html')


@app.route('/create_map', methods=["POST"])
def create_map():
    user_name = request.form["user_name"]
    users_json = get_json(user_name)

    if "users" in users_json and len(users_json["users"]) > 0:
        list_of_users = add_users_coordinates(get_users_location(users_json))
        return put_users_on_map(list_of_users).get_root().render()
    else:
        return "No users found:((("


if __name__ == "__main__":
    app.run()
