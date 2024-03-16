"""REDO - add last few cols to posts table

Revision ID: 3e4cdca83cb4
Revises: ac20edab8e77
Create Date: 2024-03-15 22:03:16.178311

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e4cdca83cb4'
down_revision: Union[str, None] = 'ac20edab8e77'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # op.add_column('posts', sa.Column(
    #     'published', sa.Boolean(), nullable=False, server_default='TRUE'),)

    # op.add_column('posts', sa.Column(
    #     'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    #op.drop_column('posts', 'published')
    #op.drop_column('posts', 'created_at')
    pass
