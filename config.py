# 상위 디렉토리에 있어야 함
db = {
        'user' : 'db계정명',
        'password' : 'db계정비밀번호',
        'host' : '127.0.0.1',
        'port' : '3306',
        'database' : 'DB이름'
    }

SQLALCHEMY_DATABASE_URI = f"mysql+mysqlconnector://{db['user']}:{db['password']}@{db['host']}:{db['port']}/{db['database']}?charset=utf8"

SQLALCHEMY_TRACK_MODIFICATIONS = False