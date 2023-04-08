"""add foreign-key to posts table

Revision ID: 377947c59345
Revises: 390b7fbef0d1
Create Date: 2023-04-08 15:02:43.944550

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '377947c59345'
down_revision = '390b7fbef0d1'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_users_fk', source_table="posts", referent_table="users", local_cols=[
                          'owner_id'], remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name="posts")
    op.drop_column('posts', 'owner_id')
    pass
