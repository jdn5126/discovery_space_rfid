"""empty message

Revision ID: 93cf356660e7
Revises: None
Create Date: 2016-02-24 15:58:32.237440

"""

# revision identifiers, used by Alembic.
revision = '93cf356660e7'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('password', sa.String(length=120), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin_user')
    ### end Alembic commands ###
