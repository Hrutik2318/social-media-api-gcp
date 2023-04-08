"""add last few columns to posts table

Revision ID: d374e9cbd819
Revises: 377947c59345
Create Date: 2023-04-08 15:06:26.384565

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd374e9cbd819'
down_revision = '377947c59345'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column(
        'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass
