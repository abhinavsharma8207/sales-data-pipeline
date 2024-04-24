from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey

Base = declarative_base()

class Customer(Base):
    __tablename__ = 'customer'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    lat = Column(Float)
    lon = Column(Float)


class Sale(Base):
    __tablename__ = 'sales'
    id = Column(Integer, primary_key=True)
    customer_id = Column(Integer)
    date = Column(DateTime)
    product_id = Column(Integer)
    quantity = Column(Integer)
    price = Column(Float)


class SaleWeather(Base):
    __tablename__ = 'sales_weather'
    order_id = Column(Integer, primary_key=True)  # Assuming order_id is unique
    temperature = Column(Float)  # Store temperature as a float
    weather_condition = Column(String)  # Store weather condition as a string


class TotalSalesPerCustomer(Base):
    __tablename__ = 'total_sales_per_customer'
    customer_id = Column(Integer, primary_key=True)
    username = Column(String)
    total_sales = Column(Float)


class AverageOrderQuantity(Base):
    __tablename__ = 'average_order_quantity'
    product_id = Column(Integer, primary_key=True)
    average_quantity = Column(Float)


class TopSellingProducts(Base):
    __tablename__ = 'top_selling_products'
    product_id = Column(Integer, primary_key=True)
    total_revenue = Column(Float)


class TopSellingCustomers(Base):
    __tablename__ = 'top_selling_customers'
    customer_id = Column(Integer, primary_key=True)
    username = Column(String)
    total_revenue = Column(Float)


class SalesTrends(Base):
    __tablename__ = 'sales_trends'
    month = Column(DateTime, primary_key=True)
    total_sales = Column(Float)


class SalesPerWeatherCondition(Base):
    __tablename__ = 'sales_per_weather_condition'
    weather_condition = Column(String, primary_key=True)
    average_sales = Column(Float)
