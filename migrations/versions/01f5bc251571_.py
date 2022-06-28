"""empty message

Revision ID: 01f5bc251571
Revises: 08ed6e8888ed
Create Date: 2022-06-28 13:16:56.596993

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01f5bc251571'
down_revision = '08ed6e8888ed'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('employees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firsName', sa.TEXT(), nullable=True),
    sa.Column('lasName', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.Column('phone', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstName', sa.TEXT(), nullable=True),
    sa.Column('lastName', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.Column('password', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('employees')
    # ### end Alembic commands ###
