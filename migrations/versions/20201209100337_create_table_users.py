"""Create table `Users`

Revision ID: 48458f4d7701
Revises:
Create Date: 2020-12-09 10:03:37.375419+00:00

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '48458f4d7701'
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
