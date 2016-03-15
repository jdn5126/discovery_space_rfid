"""empty message

Revision ID: ecd934d1b6c5
Revises: d7e970b9dafa
Create Date: 2016-03-14 14:15:04.964201

"""

# revision identifiers, used by Alembic.
revision = 'ecd934d1b6c5'
down_revision = 'd7e970b9dafa'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Question', sa.Text(), nullable=True),
    sa.Column('Game', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['Game'], ['games.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('answers')
    op.drop_table('questions')
    ### end Alembic commands ###