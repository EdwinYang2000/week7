from simpledu.app import create_app


app = create_app('development')
app.config['SECRET_KEY'] = '123456'

if __name__ == '__main__':
    app.run()


