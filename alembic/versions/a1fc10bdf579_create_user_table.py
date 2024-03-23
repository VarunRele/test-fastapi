"""create_user_table

Revision ID: a1fc10bdf579
Revises: f295672bec62
Create Date: 2024-03-23 10:30:33.192091

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1fc10bdf579'
down_revision: Union[str, None] = 'f295672bec62'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'Users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(255), unique=True, nullable=False),
        sa.Column('password', sa.String(255), nullable=False),
        sa.Column('created_at', sa.TIMESTAMP(timezone=True), nullable=True, server_default=sa.func.now())
    )
    pass


def downgrade() -> None:
    op.drop_table('Users')
    pass
