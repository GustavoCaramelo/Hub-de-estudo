"""create users table

Revision ID: ed02392940ab
Revises: 1be6b225441d
Create Date: 2025-06-11 10:50:25.101018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ed02392940ab'
down_revision: Union[str, None] = '1be6b225441d'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('name', sa.String, nullable=False),
        sa.Column('email', sa.String, nullable=False, unique=True, index=True),
        sa.Column('password', sa.String, nullable=False)
    )



def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('users')
