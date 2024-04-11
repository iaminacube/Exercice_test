This File intents to Show the tables i created and their column description 



### Table and Decription ###

**Property_Unit**
- `unit_id`: Representing a unique identifier for each unit.
- `unit_number`: Identifier for the unit within the property.
- `unit_type_id`: Referencing the primary key of the `Unit_Type` table.
- `rent`: Represent rent value for unit number.
- `address`, `city`, `state`, `zipcode`, `landlord_name`, `landlord_contact`
- `lease_start_date`, `lease_end_date`
- `is_occupied`: Indicate whether the unit is currently occupied or not.


**Unit_Type**
- `unit_type_id`: Description: Unique identifier for each unit type.
- `type_name`: Description: Name representing the unit type.
- `description`: Brief description or additional information about the unit type.
- `average_size`: Average size of units of this type
- `amenities`: List of amenities available

**Unit_Room**
- `room_id`: Unique identifier for each room.
- `unit_id`: Identifier for the property unit to which the room belongs.
- `room_number`:  Identifier for the room within the property unit.
- `room_type_id`: Identifier for the type of room.
- `floor_number`: The floor number where the room is located within the property unit.
- `square_footage`: The size of the room 
- `is_furnished`: Indicates whether the room is furnished or not.
- `has_balcony`: Indicates whether the room has a balcony or not.

**Room_Type**
- `room_type_id`: Unique identifier for each room type.
- `type_name`: Name or label representing the room type.
- `description`: Brief description or additional information about the room type.
- `average_size`: Average size of rooms of this type
- `max_occupancy`: Maximum number of occupants allowed in rooms of this type.
- `has_bathroom`: Indicates whether rooms of this type have a private bathroom.


**Rent_Payment**
- `payment_id`: Unique identifier for each payment.
- `room_id`: Foreign key referencing the `Unit_Room` table to associate the payment with a specific room.
- `payment_date`: Date when the payment was made.
- `amount`: Amount of rent paid.
- `payment_method`: Indicates how the rent payment was made 
- `late_fee`: Amount of late fee incurred for the payment, if applicable.
- `payment_status`: Indicates the status of the payment (e.g., processed, pending, failed).
- `payment_channel`: Indicates the channel through which the payment was made (e.g., online, in-person, by mail).
- `discounts_applied`: Amount of discounts applied to the rent payment.
- `comments`: Additional information or notes related to the payment.
- `receipt_link`: Link or reference to the payment confirmation or receipt document.