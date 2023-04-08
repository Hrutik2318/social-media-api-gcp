"""create posts table

Revision ID: e3d877c75832
Revises: 
Create Date: 2023-04-08 14:34:07.461537

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3d877c75832'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts',
                    sa.Column('id', sa.Integer(), primary_key=True),
                    sa.Column('title', sa.String(), nullable=False)
                    )
    pass


def downgrade() -> None:
    op.drop_table('posts')
    pass
