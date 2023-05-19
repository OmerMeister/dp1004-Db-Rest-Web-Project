if __name__ == "__main__":
    from random import randint
    import requests  # importing the general requests lib to make requests to the backend
    from flask import Flask, url_for, request, Response, render_template, json
    import os
    import signal

    app = Flask(__name__)


    def response_creator(content, code):
        response = Response(content, status=code)
        response.content_type = 'application/json'
        return response


    @app.errorhandler(404)
    def page_not_found(error):
        # Custom response or redirect for 404 errors
        return render_template('404.html', ), 404


    @app.route('/stop_server')
    def stop_server():
        os.kill(os.getpid(), signal.CTRL_C_EVENT)
        return 'Server stopped'


    # DEFAULT PAGE - just in case you suddenly get into it
    @app.route("/")
    def default():
        return render_template('default_web.html', ), 200


    @app.route('/get_user_name', )
    def default_no_id():
        return render_template('get_user_name.html')


    @app.route('/get_user_name/', )
    def default_no_id_slash():
        return render_template('get_user_name.html')


    @app.route('/get_user_name/<user_id>', methods=['GET'])
    def get_user_name(user_id):
        response = requests.get(f'http://127.0.0.1:5000/users/{user_id}')
        try:
            dict_obj = response.json()
            username = dict_obj["user_name"]
            all_users = dict_obj["all_users"][:-2]
            all_users = all_users.replace('(', '')
            all_users = all_users.replace(')', '  ⬤  ')
            status = "user"
        except:
            username = "no such user"
            status = "error"
            dict_obj = response.json()
            all_users = dict_obj["all_users"][:-2]
            all_users = all_users.replace('(', '')
            all_users = all_users.replace(')', '  ⬤  ')
        if request.method == 'GET':
            return render_template('get_user_name_id.html', username=username, status=status, all_users=all_users)


    # host is pointing at local machine address
    # debug is used for more detailed logs + hot swapping
    app.run(host='127.0.0.1', debug=True, port=5001)
