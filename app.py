from flaskr import create_app
import os

if __name__ == "__main__":
    app = create_app()
    port = int(os.environ.get('PORT', 4000))
    print(f'ATTEMPTING TO RUN APP ON PORT: {port}')

    app.run(host='0.0.0.0', port=port)
