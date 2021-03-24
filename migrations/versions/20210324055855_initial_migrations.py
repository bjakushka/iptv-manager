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

# constants which defines mentions table names
TBL_NAME_CHANNEL = 'channel'
TBL_NAME_CHANNEL_STREAM = 'channel_stream'
TBL_NAME_PLAYLIST = 'playlist'
TBL_NAME_PLAYLIST_ITEM = 'playlist_item'


def upgrade():
    _create_table_channel()
    _create_table_channel_stream()
    _create_table_playlist()
    _create_table_playlist_item()


def downgrade():
    op.drop_table(TBL_NAME_PLAYLIST_ITEM)
    op.drop_table(TBL_NAME_PLAYLIST)
    op.drop_table(TBL_NAME_CHANNEL_STREAM)
    op.drop_table(TBL_NAME_CHANNEL)


# ---
# functions which create new tables
# ---


def _create_table_channel():
    op.create_table(
        TBL_NAME_CHANNEL,

        # columns
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),

        # constraints
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )


def _create_table_channel_stream():
    op.create_table(
        TBL_NAME_CHANNEL_STREAM,

        # columns
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('channel_id', sa.Integer(), nullable=False),
        sa.Column('url', sa.Text(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),

        # constraints
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(('channel_id',), [f'{TBL_NAME_CHANNEL}.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('channel_id'),
    )


def _create_table_playlist():
    op.create_table(
        TBL_NAME_PLAYLIST,

        # columns
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(128), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),

        # constraints
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('name'),
    )


def _create_table_playlist_item():
    op.create_table(
        TBL_NAME_PLAYLIST_ITEM,

        # columns
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('channel_id', sa.Integer(), nullable=False),
        sa.Column('playlist_id', sa.Integer(), nullable=False),
        sa.Column('created_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),
        sa.Column('updated_at', sa.DateTime(), server_default=sa.text('NOW()'), nullable=False),

        # constraints
        sa.PrimaryKeyConstraint('id'),
        sa.ForeignKeyConstraint(('channel_id',), [f'{TBL_NAME_CHANNEL}.id'], ondelete='RESTRICT'),
        sa.ForeignKeyConstraint(('playlist_id',), [f'{TBL_NAME_PLAYLIST}.id'], ondelete='RESTRICT'),
        sa.UniqueConstraint('channel_id', 'playlist_id'),
    )
