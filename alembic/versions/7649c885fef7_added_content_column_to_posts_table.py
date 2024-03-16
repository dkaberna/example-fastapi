"""added content column to posts' table

Revision ID: 7649c885fef7
Revises: 537b64aae3a7
Create Date: 2024-03-15 20:32:55.162453

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7649c885fef7'
down_revision: Union[str, None] = '537b64aae3a7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
