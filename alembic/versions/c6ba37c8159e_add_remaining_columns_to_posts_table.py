"""add remaining columns to posts table

Revision ID: c6ba37c8159e
Revises: 4aaa0f8f1259
Create Date: 2024-03-23 11:31:57.408637

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c6ba37c8159e'
down_revision: Union[str, None] = '4aaa0f8f1259'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts',
        sa.Column('published', sa.Boolean(), server_default='1', nullable=False)
    )
    op.add_column(
        'posts',
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.func.now())
    )
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
