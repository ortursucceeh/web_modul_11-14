"""empty message

Revision ID: 9591ecaee4f4
Revises: 608b85447a69
Create Date: 2023-03-05 17:30:07.377998

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9591ecaee4f4'
down_revision = '608b85447a69'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
