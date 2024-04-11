BEGIN TRANSACTION hybridTEST

CREATE TABLE [Property_Unit] (
    [Unit_id] int  NOT NULL ,
    [Unit_number] int  NOT NULL ,
    [unit_type_id] int  NOT NULL ,
    [Address2] String  NOT NULL ,
    [Address3] String  NOT NULL ,
    [address] String  NOT NULL ,
    [city] String  NOT NULL ,
    [state] String  NOT NULL ,
    [zipcode] String  NOT NULL ,
    [landlord_name] String  NOT NULL ,
    [landlord_contact] String  NOT NULL ,
    [lease_start_date] DateTime  NOT NULL ,
    [lease_end_date] DateTime  NOT NULL ,
    [is_occupied] Boolean  NOT NULL ,
    CONSTRAINT [PK_Property_Unit] PRIMARY KEY CLUSTERED (
        [Unit_id] ASC
    )
)

CREATE TABLE [Unit_type] (
    [unit_type_id] int  NOT NULL ,
    [type_name] String  NOT NULL ,
    [description] String  NOT NULL ,
    [average_size] Float  NOT NULL ,
    [amenities] String  NOT NULL ,
    CONSTRAINT [PK_Unit_type] PRIMARY KEY CLUSTERED (
        [unit_type_id] ASC
    )
)

CREATE TABLE [Unit_room] (
    [room_id] int  NOT NULL ,
    [unit_id] int  NOT NULL ,
    [room_number] int  NOT NULL ,
    [room_type_id] int  NOT NULL ,
    [floor_number] int  NOT NULL ,
    [square_footage] Float  NOT NULL ,
    [is_furnished] Boolean  NOT NULL ,
    [has_balcony] Boolean  NOT NULL ,
    CONSTRAINT [PK_Unit_room] PRIMARY KEY CLUSTERED (
        [room_id] ASC
    )
)

CREATE TABLE [Room_type] (
    [room_type_id] int  NOT NULL ,
    [type_name] String  NOT NULL ,
    [description] String  NOT NULL ,
    [average_size] Float  NOT NULL ,
    [max_occupancy] int  NOT NULL ,
    [has_bathroom] Boolean  NOT NULL ,
    CONSTRAINT [PK_Room_type] PRIMARY KEY CLUSTERED (
        [room_type_id] ASC
    ),
    CONSTRAINT [UK_Room_type_type_name] UNIQUE (
        [type_name]
    )
)

CREATE TABLE [Rent_Payment] (
    [payment_id] int  NOT NULL ,
    [room_id] int  NOT NULL ,
    [payment_date] date  NOT NULL ,
    [amount] Float  NOT NULL ,
    [payment_method] String  NOT NULL ,
    [late_fee] Float  NOT NULL ,
    [payment_status] String  NOT NULL ,
    [payment_channel] String  NOT NULL ,
    [discounts_applied] Float  NOT NULL ,
    [comments] String  NOT NULL ,
    [receipt_link] String  NOT NULL ,
    CONSTRAINT [PK_Rent_Payment] PRIMARY KEY CLUSTERED (
        [payment_id] ASC
    )
)

ALTER TABLE [Property_Unit] WITH CHECK ADD CONSTRAINT [FK_Property_Unit_unit_type_id] FOREIGN KEY([unit_type_id])
REFERENCES [Unit_type] ([unit_type_id])

ALTER TABLE [Property_Unit] CHECK CONSTRAINT [FK_Property_Unit_unit_type_id]

ALTER TABLE [Unit_room] WITH CHECK ADD CONSTRAINT [FK_Unit_room_unit_id] FOREIGN KEY([unit_id])
REFERENCES [Property_Unit] ([Unit_id])

ALTER TABLE [Unit_room] CHECK CONSTRAINT [FK_Unit_room_unit_id]

ALTER TABLE [Unit_room] WITH CHECK ADD CONSTRAINT [FK_Unit_room_room_type_id] FOREIGN KEY([room_type_id])
REFERENCES [Room_type] ([room_type_id])

ALTER TABLE [Unit_room] CHECK CONSTRAINT [FK_Unit_room_room_type_id]

ALTER TABLE [Rent_Payment] WITH CHECK ADD CONSTRAINT [FK_Rent_Payment_room_id] FOREIGN KEY([room_id])
REFERENCES [Unit_room] ([room_id])

ALTER TABLE [Rent_Payment] CHECK CONSTRAINT [FK_Rent_Payment_room_id]

COMMIT TRANSACTION hybridTEST