"""create_post_table

Revision ID: 165e35b77c2f
Revises: 
Create Date: 2024-03-23 10:15:28.069825

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '165e35b77c2f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
    sa.Column('title', sa.String(length=255), nullable=False))
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
