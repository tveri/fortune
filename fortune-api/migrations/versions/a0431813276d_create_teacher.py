"""create teacher

Revision ID: a0431813276d
Revises: 13c4d2f90991
Create Date: 2023-09-20 17:07:22.549797

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a0431813276d'
down_revision: Union[str, None] = '13c4d2f90991'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teachers',
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('educational_platform_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['educational_platform_id'], ['educational_platforms.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('teachers')
    # ### end Alembic commands ###
