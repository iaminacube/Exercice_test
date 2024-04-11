from peewee import Model, SqliteDatabase, ForeignKeyField, CharField, FloatField, IntegerField, BooleanField, DateField

# Create a SQLite database instance
db = SqliteDatabase('property_management.db')

class BaseModel(Model):
    class Meta:
        database = db

class UnitType(BaseModel):
    type_name = CharField()

class PropertyUnit(BaseModel):
    unit_number = CharField()
    unit_type = ForeignKeyField(UnitType, backref='units')
    rent = FloatField()
    address = CharField()
    city = CharField()
    state = CharField()
    zipcode = CharField()
    landlord_name = CharField()
    landlord_contact = CharField()
    lease_start_date = DateField()
    lease_end_date = DateField()
    is_occupied = BooleanField()

class RoomType(BaseModel):
    type_name = CharField()
    description = CharField()
    average_size = FloatField()
    max_occupancy = IntegerField()
    has_bathroom = BooleanField()

class UnitRoom(BaseModel):
    unit = ForeignKeyField(PropertyUnit, backref='rooms')
    room_number = CharField()
    room_type = ForeignKeyField(RoomType, backref='rooms')
    floor_number = IntegerField()
    square_footage = FloatField()
    is_furnished = BooleanField()
    has_balcony = BooleanField()

class RentPayment(BaseModel):
    room = ForeignKeyField(UnitRoom, backref='payments')
    payment_date = DateField()
    amount = FloatField()
    payment_method = CharField()
    late_fee = FloatField()
    payment_status = CharField()
    payment_reference = CharField()
    payment_channel = CharField()
    discounts_applied = FloatField()
    comments = CharField()
    receipt_link = CharField()

# Create tables
db.connect()
db.create_tables([UnitType, PropertyUnit, RoomType, UnitRoom, RentPayment])
