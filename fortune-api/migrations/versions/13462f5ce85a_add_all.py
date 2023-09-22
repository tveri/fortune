"""add all

Revision ID: 13462f5ce85a
Revises: 2ad6160bcdcc
Create Date: 2023-09-20 18:34:00.716113

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '13462f5ce85a'
down_revision: Union[str, None] = '2ad6160bcdcc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(), nullable=False))
    op.drop_constraint('users_mail_key', 'users', type_='unique')
    op.create_unique_constraint(None, 'users', ['email'])
    op.drop_column('users', 'mail')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('mail', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'users', type_='unique')
    op.create_unique_constraint('users_mail_key', 'users', ['mail'])
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
