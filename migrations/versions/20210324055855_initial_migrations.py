"""Initial migrations

Revision ID: 2ce4a8dfd6b9
Revises: 
Create Date: 2021-03-24 05:58:55.498166+00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '2ce4a8dfd6b9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',

        # columns
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(255), nullable=False),

        # constraints
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('username'),
    )


def downgrade():
    op.drop_table('users')
