"""empty message

Revision ID: 08ed6e8888ed
Revises: 
Create Date: 2022-06-28 11:32:57.220116

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '08ed6e8888ed'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('employees')
    op.drop_table('users')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.Column('password', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('employees',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('firsName', sa.TEXT(), nullable=True),
    sa.Column('lasName', sa.TEXT(), nullable=True),
    sa.Column('email', sa.TEXT(), nullable=True),
    sa.Column('phone', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
