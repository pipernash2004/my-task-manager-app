"""create forign key for posts  table

Revision ID: ff2715ac75b9
Revises: 33900dc59675
Create Date: 2024-07-27 04:44:52.184138

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ff2715ac75b9'
down_revision: Union[str, None] = '33900dc59675'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None




def upgrade():
    op.add_column('posts',sa.Column('owner_id',sa.Integer(),nullable=False))
    op.create_foreign_key('post_user_fk',source_table='posts', referent_table='users',local_cols=['owner_id'],remote_cols=['id'], ondelete="CASCADE")
    
    pass


def downgrade():
    op.drop_constraint('post_user_fk','posts')
    op.drop_column('posts','owner_id')
    pass


