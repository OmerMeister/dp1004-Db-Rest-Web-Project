import json

if __name__ == "__main__":
    from flask import Flask, request, Response, render_template
    from db_connector import db_get, db_post, db_put, db_delete, db_get_all
    import datetime

    app = Flask(__name__)


    def response_creator(content, code):
        response = Response(content, status=code)
        response.content_type = 'application/json'
        return response


    def timestamp_str():
        return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")


    # DEFAULT PAGE - just in case you suddenly get into it
    @app.route("/")
    def default():
        return render_template('default_rest.html', ), 200


    @app.route("/users/")
    def default_users():
        return render_template('default_rest.html', ), 200


    @app.route('/users/<user_id>', methods=['GET', 'POST', 'DELETE', 'PUT'])
    def user(user_id):
        # GET METHOD
        # gets the user_id from the rest api, applying the db_get method with the provided parameter
        # if db_get returns 0, a code 500 response will be sent. if db_get return a string, a code
        # 200 response will be sent along with the string in the json data.
        # sends the list of all current users both on success and failure
        if request.method == 'GET':
            username = db_get(user_id)
            all_users = db_get_all()
            if username == 0:
                return response_creator(
                    '{"status": "error", "reason": "no such id", "all_users": "%s"}' % (all_users), 500)

            else:
                return response_creator(
                    '{"status": "ok", "user_name": "%s", "all_users": "%s"}' % (username, all_users), 200)


        # POST METHOD
        # gets an id from the rest api url and a username from the query provided json data
        # the provided json data is one key:value like {"user_name": "john"}
        elif request.method == 'POST':
            # getting current time as a string for the creation_time column
            current_time = timestamp_str()
            # converting the request's json data to dictionary and then getting the value of the "user_name" key
            # checking that the username is not empty or contains only spaces
            try:

                # get the request, convert it to dict, get "user_name" from the dict
                user_name = (request.json)['user_name']
                if user_name is None or user_name.isspace() or not user_name:
                    return response_creator("{“status”: “error”, “reason”: ”illegal username”}", 500)
            # response in case the request payload is not json readable
            except Exception as e:
                print(e)
                return response_creator("{“status”: “error”, “reason”: ”bad json data”}", 500)
            # calling the db method with the userid and username to insert to the db, if id is taken
            # the method will return 0, if not, it will apply and return 1
            post_result = db_post(user_id, user_name, current_time)
            if post_result == -1:
                return response_creator(f"“status”: “ok”, “user_added”: {user_name}", 200)
            if post_result == 0:
                return response_creator("{“status”: “error”, “reason”: ”db error”}", 500)
            else:
                return response_creator(f"“status”: “ok”, “user_added”: {user_name}, “id changed to”: {post_result}",
                                        200)

        # PUT METHOD
        # getting an id and json data to update with
        # the provided json data is one key:value like {"user_name": "john"}. creation time will also be updated.
        if request.method == 'PUT':
            # getting current time as a string for the creation_time column
            current_time = timestamp_str()
            # converting the request's json data to dictionary and then getting the value of the "user_name" key
            # checking that the username is not empty or contains only spaces
            try:
                user_name = request.json.get('user_name')
                if user_name is None or user_name.isspace() or not user_name:
                    return response_creator("{“status”: “error”, “reason”: ”illegal username”}", 500)
            # response in case the request payload is not json readable
            except Exception as e:
                return response_creator("{“status”: “error”, “reason”: ”bad json data”}", 500)
            # calling the db method with the userid and username to update in the db, if id doesn't
            # exist the method will return 0, if is, it will update and return 1
            post_result = db_put(user_id, user_name, current_time)
            if post_result == 1:
                return response_creator(f"“status”: “ok”, “user_updated”: {user_name}", 200)

            if post_result == 0:
                return response_creator("{“status”: “error”, “reason”: ”no such id / illegal id provided”}", 500)

        # DELETE METHOD
        # gets the username into a variable, delete the user from the db and then, returns the variable.
        # if it failed, it will return 0
        if request.method == 'DELETE':
            deleted_username = db_delete(user_id)
            if deleted_username == 0:
                return response_creator("{“status”: “error”, “reason”: ”no such id / illegal id provided”}", 500)
            else:
                return response_creator(f"“status”: “ok”, “user_deleted”: {deleted_username}", 200)


    # host is pointing at local machine address
    # debug is used for more detailed logs + hot swapping
    app.run(host='127.0.0.1', debug=True, port=5000)
