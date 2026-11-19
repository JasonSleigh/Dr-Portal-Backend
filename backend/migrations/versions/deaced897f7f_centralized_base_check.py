"""centralized base check

Revision ID: deaced897f7f
Revises: 9b7489289c51
Create Date: 2026-11-19 11:59:37.238410

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'deaced897f7f'
down_revision: Union[str, Sequence[str], None] = '9b7489289c51'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
