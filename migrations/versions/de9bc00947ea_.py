"""empty message

Revision ID: de9bc00947ea
Revises: ecd934d1b6c5
Create Date: 2016-03-14 21:25:33.380336

"""

# revision identifiers, used by Alembic.
revision = 'de9bc00947ea'
down_revision = 'ecd934d1b6c5'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('QuestionAnswerLink',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('question_id', sa.Integer(), nullable=False),
    sa.Column('device_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], ['devices.id'], ),
    sa.ForeignKeyConstraint(['question_id'], ['questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('answers')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('answers',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('question_id', sa.INTEGER(), nullable=False),
    sa.Column('device_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['device_id'], [u'devices.id'], ),
    sa.ForeignKeyConstraint(['question_id'], [u'questions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('QuestionAnswerLink')
    ### end Alembic commands ###
