"""add_content_columns_to_posts

Revision ID: f295672bec62
Revises: 165e35b77c2f
Create Date: 2024-03-23 10:24:07.231997

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f295672bec62'
down_revision: Union[str, None] = '165e35b77c2f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(255), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
