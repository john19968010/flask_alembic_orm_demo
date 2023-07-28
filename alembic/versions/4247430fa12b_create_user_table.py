"""create_user_table

Revision ID: 4247430fa12b
Revises: 
Create Date: 2023-07-28 15:56:58.992813

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4247430fa12b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('gender', sa.Boolean(), nullable=True),
    sa.Column('account', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=100), nullable=True),
    sa.Column('birth', sa.DateTime(), nullable=True),
    sa.Column('note', sa.String(length=45), nullable=True),
    sa.Column('create_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###