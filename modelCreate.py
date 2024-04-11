class PropertyUnit:
    def __init__(self, unit_id, unit_number, unit_type_id, rent, address, city, state, zipcode, landlord_name, landlord_contact, lease_start_date, lease_end_date, is_occupied):
        self.unit_id = unit_id
        self.unit_number = unit_number
        self.unit_type_id = unit_type_id
        self.rent = rent
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode
        self.landlord_name = landlord_name
        self.landlord_contact = landlord_contact
        self.lease_start_date = lease_start_date
        self.lease_end_date = lease_end_date
        self.is_occupied = is_occupied
        self.rooms = []

class UnitRoom:
    def __init__(self, room_id, unit_id, room_number, room_type_id, floor_number, square_footage, is_furnished, has_balcony):
        self.room_id = room_id
        self.unit_id = unit_id
        self.room_number = room_number
        self.room_type_id = room_type_id
        self.floor_number = floor_number
        self.square_footage = square_footage
        self.is_furnished = is_furnished
        self.has_balcony = has_balcony

class RoomType:
    def __init__(self, room_type_id, type_name, description, average_size, max_occupancy, has_bathroom):
        self.room_type_id = room_type_id
        self.type_name = type_name
        self.description = description
        self.average_size = average_size
        self.max_occupancy = max_occupancy
        self.has_bathroom = has_bathroom
        self.rooms = []

class RentPayment:
    def __init__(self, payment_id, room_id, payment_date, amount, payment_method, late_fee, payment_status, payment_reference, payment_channel, discounts_applied, comments, receipt_link):
        self.payment_id = payment_id
        self.room_id = room_id
        self.payment_date = payment_date
        self.amount = amount
        self.payment_method = payment_method
        self.late_fee = late_fee
        self.payment_status = payment_status
        self.payment_reference = payment_reference
        self.payment_channel = payment_channel
        self.discounts_applied = discounts_applied
        self.comments = comments
        self.receipt_link = receipt_link

# Example usage with relations:
unit1 = PropertyUnit(1, "A101", 1, 1200, "123 Main St", "City", "State", "12345", "John Doe", "123-456-7890", "2024-01-01", "2025-01-01", True)
room1 = UnitRoom(1, 1, "101", 1, 1, 500, True, False)
room_type1 = RoomType(1, "Studio", "Studio apartment", 400, 1, True)
payment1 = RentPayment(1, 1, "2024-04-10", 1200, "Credit Card", 0, "Processed", "123456789", "Online", 0, "No comments", "receipt_link")

# Establishing relationships
unit1.rooms.append(room1)
room1.room_type = room_type1
room_type1.rooms.append(room1)
room1.rent_payments = [payment1]
