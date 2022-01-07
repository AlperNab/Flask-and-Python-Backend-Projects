from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from HiringCars import db

#cur.execute("CREATE TABLE Customer(firstname VARCHAR(30) NOT NULL,secondname VARCHAR(30) NOT NULL ,thirdname VARCHAR(30) NOT NULL, carType VARCHAR(30) NOT NULL , dateHired DATETIME  NOT NULL ,dateReturned DateTIME NOT NULL )")


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(20), nullable=False)
    secondname = db.Column(db.String(20), nullable=False)
    thirdname = db.Column(db.String(20), unique=True, nullable=False)
    carType=db.Column(db.String(20), nullable=False)
    dateHired = db.Column(db.DateTime, nullable=False)
    dateReturned = db.Column(db.DateTime, nullable=False)
    car = db.relationship('Post', backref='thirdname', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"Customer('{self.firstname}', '{self.secondname}', '{self.thirdname}', '{self.carType}', '{self.dateHired}', '{self.dateReturned}')"
