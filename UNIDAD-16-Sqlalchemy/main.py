import sqlalchemy as db
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column,String,Integer
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.orm import Session
  

Base = declarative_base()
class Customer(Base):
    __tablename__ = 'customer'
    name = Column(String)
    age = Column(Integer) 
    email = Column(String)
    address = Column(String) 
    zip_code = Column(String)
    id = Column(Integer, primary_key= True)
    def __repr__(self):
        return "<Customer(name='%s',age='%s',email='%s',addres='%s',zip_code='%s')>" % (self.name, self.age, self.name, self.address, self.zip_code)


class Database():
    engine = db.create_engine("postgresql://postgres:12345678@localhost/test")
    def __init__(self) :
        self.connection = self.engine.connect()
        print("DB instance created")
        

    def FetchByQyert(self, query):
        fetchQuery = self.connection.execute(f"SELECT * FROM {query}")
        for data in fetchQuery.fetchall():
            print(data) 

    def saveDate(self,customer):
        self.connection.execute(f"""INSERT INTO customer(name,age,email,address,zip_code)
                                VALUES('{customer.name}',
                                        '{customer.age}',
                                        '{customer.email}',
                                        '{customer.address}',
                                        '{customer.zip_code}')""")

    def fetchUserByName(self):
        meta = MetaData()
        customer = Table('customer',meta,Column('name'))
        data = self.connection.execute(customer.select())
        for cust in data:
             print(cust)


    def fetchAllUsers(self):
        self.session = Session(bind = self.connection)
        customers = self.session.query(Customer).all()
        for cust in customers:
            print(cust)


    def saveData(self, customer):
        session = Session(bind = self.connection)
        session.add(customer)
        session.commit()


    def updateCustomer(self, customerName, addres):
        session = Session(bind=self.connection)
        dataToUpdate = {Customer.addres: addres}
        customerData = session.query(Customer).filter(Customer.name==customerName)
        customerData.update(dataToUpdate)
        session.commit()


    def deleteCustomer(self, customer):
        session = Session(bind=self.connection)
        customerData = session.query(customer).filter(Customer.name==customer).first()
        session.delete(customerData)
        session.commit()


