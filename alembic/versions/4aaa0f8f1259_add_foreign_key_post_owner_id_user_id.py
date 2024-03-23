"""add foreign key post.owner_id->user.id

Revision ID: 4aaa0f8f1259
Revises: a1fc10bdf579
Create Date: 2024-03-23 10:41:48.029819

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '4aaa0f8f1259'
down_revision: Union[str, None] = 'a1fc10bdf579'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column(
        'posts', 
        sa.Column('user_id', sa.Integer(), nullable=False)
    )
    op.create_foreign_key('fk_post_user', 'posts', 'users', ['user_id'], ['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('fk_post_user', 'posts', type_='foreignkey')
    op.drop_column('posts', 'user_id')
    pass
