"""empty message

Revision ID: 44f5651376d4
Revises: 
Create Date: 2021-12-21 22:29:16.559335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44f5651376d4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('password_hash', sa.String(length=250), nullable=False),
    sa.Column('salt', sa.String(length=16), nullable=False),
    sa.Column('status', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name')
    )
    op.create_table('house',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('size', sa.Float(), nullable=False),
    sa.Column('featured', sa.Boolean(), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('short_description', sa.String(length=200), nullable=False),
    sa.Column('location', sa.String(length=100), nullable=False),
    sa.Column('balcony_terrace', sa.Boolean(), nullable=False),
    sa.Column('garden', sa.Boolean(), nullable=False),
    sa.Column('kitchen', sa.Boolean(), nullable=False),
    sa.Column('pets', sa.Boolean(), nullable=False),
    sa.Column('parking', sa.Boolean(), nullable=False),
    sa.Column('wheelchair', sa.Boolean(), nullable=False),
    sa.Column('basement', sa.Boolean(), nullable=False),
    sa.Column('dishwasher', sa.Boolean(), nullable=False),
    sa.Column('washing_machine', sa.Boolean(), nullable=False),
    sa.Column('dryer', sa.Boolean(), nullable=False),
    sa.Column('ac', sa.Boolean(), nullable=False),
    sa.Column('heating', sa.Boolean(), nullable=False),
    sa.Column('wifi', sa.Boolean(), nullable=False),
    sa.Column('students', sa.Boolean(), nullable=False),
    sa.Column('working_proffesionals', sa.Boolean(), nullable=False),
    sa.Column('couples', sa.Boolean(), nullable=False),
    sa.Column('male', sa.Boolean(), nullable=False),
    sa.Column('female', sa.Boolean(), nullable=False),
    sa.Column('smoking', sa.String(length=50), nullable=False),
    sa.Column('instruments', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('house_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('cloud_id', sa.String(length=100), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['house.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('slug', sa.String(length=50), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.Column('beds', sa.Integer(), nullable=False),
    sa.Column('private_bathroom', sa.Boolean(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['house.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('slug'),
    sa.UniqueConstraint('slug')
    )
    op.create_table('booking_order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('check_in_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('check_out_date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('tennant_email', sa.String(length=50), nullable=False),
    sa.Column('tennant_name', sa.String(length=50), nullable=False),
    sa.Column('tennant_number', sa.String(length=50), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.Column('house_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['house_id'], ['house.id'], ),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('room_image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=100), nullable=False),
    sa.Column('cloud_id', sa.String(length=100), nullable=False),
    sa.Column('room_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['room_id'], ['room.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room_image')
    op.drop_table('booking_order')
    op.drop_table('room')
    op.drop_table('house_image')
    op.drop_table('house')
    op.drop_table('admin')
    # ### end Alembic commands ###
