"""add user table

Revision ID: 390b7fbef0d1
Revises: 22635969d990
Create Date: 2023-04-08 14:59:47.054180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '390b7fbef0d1'
down_revision = '22635969d990'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade() -> None:
    op.drop_table('users')
    pass
