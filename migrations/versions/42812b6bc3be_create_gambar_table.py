"""Create Gambar Table

Revision ID: 42812b6bc3be
Revises: 0a535f798e9b
Create Date: 2023-12-20 15:02:28.684091

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '42812b6bc3be'
down_revision = '0a535f798e9b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gambar',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('pathname', sa.String(length=255), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('gambar')
    # ### end Alembic commands ###
