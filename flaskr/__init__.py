import os
from flask import Flask
from . import db
from . import auth
from . import blog

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, boo!'

    # Init the database
    db.init_app(app)

    # Authentication blueprint
    app.register_blueprint(auth.bp)

    # Blog Blueprint
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get('PORT', 4000))
    print(f'ATTEMPTING TO RUN APP ON PORT: {port}')

    app.run(host='0.0.0.0', port=port)
