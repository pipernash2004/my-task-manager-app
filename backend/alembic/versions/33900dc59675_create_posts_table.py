"""create posts  table

Revision ID: 33900dc59675
Revises: 7ffce1e9a53f
Create Date: 2024-07-27 04:43:39.423480

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '33900dc59675'
down_revision: Union[str, None] = '7ffce1e9a53f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,primary_key=True),
                  sa.Column('content',sa.String(),nullable=False),
                  sa.Column('published',sa.Boolean(),nullable=False, server_default="True"),
                  sa.Column('created_at',sa.DateTime(timezone=True),server_default=sa.func.now(),nullable=False))
    pass

def downgrade():
    op.drop_table('posts')
    pass