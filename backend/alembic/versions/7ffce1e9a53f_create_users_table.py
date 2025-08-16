"""create users  table

Revision ID: 7ffce1e9a53f
Revises: 
Create Date: 2024-07-27 04:38:03.142788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7ffce1e9a53f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('users',sa.Column('id', sa.Integer(),nullable=False,primary_key=True),
                    sa.Column('username',sa.String(),nullable=False, unique= True),
                    sa.Column('email',sa.String(),nullable=False, unique=True),
                    sa.Column('password',sa.String, nullable=False))
    pass


def downgrade():
    op.drop_table('users')
    pass

