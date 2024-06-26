"""Added required tables

Revision ID: e0abcd3e7cfc
Revises: 1f0925eed80b
Create Date: 2024-02-10 21:21:39.628439

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e0abcd3e7cfc'
down_revision: Union[str, None] = '1f0925eed80b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('actors',
    sa.Column('actor_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('birthday', sa.Date(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('img_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('actor_id')
    )
    op.create_index(op.f('ix_actors_actor_id'), 'actors', ['actor_id'], unique=True)
    op.create_index(op.f('ix_actors_name'), 'actors', ['name'], unique=True)
    op.create_table('cinemas',
    sa.Column('cinema_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('rating', sa.Float(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('img_path', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('cinema_id')
    )
    op.create_index(op.f('ix_cinemas_cinema_id'), 'cinemas', ['cinema_id'], unique=True)
    op.create_index(op.f('ix_cinemas_name'), 'cinemas', ['name'], unique=True)
    op.create_table('genres',
    sa.Column('genre_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('genre_id')
    )
    op.create_index(op.f('ix_genres_genre_id'), 'genres', ['genre_id'], unique=True)
    op.create_table('users',
    sa.Column('user_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('role', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('user_id')
    )
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('actor_cinema',
    sa.Column('actor_id', sa.Integer(), nullable=True),
    sa.Column('cinema_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['actor_id'], ['actors.actor_id'], ),
    sa.ForeignKeyConstraint(['cinema_id'], ['cinemas.cinema_id'], )
    )
    op.create_table('comments',
    sa.Column('comment_id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('cinema_id', sa.Integer(), nullable=True),
    sa.Column('source', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['cinema_id'], ['cinemas.cinema_id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.user_id'], ),
    sa.PrimaryKeyConstraint('comment_id')
    )
    op.create_index(op.f('ix_comments_comment_id'), 'comments', ['comment_id'], unique=True)
    op.create_table('genre_cinema',
    sa.Column('genre_id', sa.Integer(), nullable=True),
    sa.Column('cinema_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['cinema_id'], ['cinemas.cinema_id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genres.genre_id'], )
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('genre_cinema')
    op.drop_index(op.f('ix_comments_comment_id'), table_name='comments')
    op.drop_table('comments')
    op.drop_table('actor_cinema')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_genres_genre_id'), table_name='genres')
    op.drop_table('genres')
    op.drop_index(op.f('ix_cinemas_name'), table_name='cinemas')
    op.drop_index(op.f('ix_cinemas_cinema_id'), table_name='cinemas')
    op.drop_table('cinemas')
    op.drop_index(op.f('ix_actors_name'), table_name='actors')
    op.drop_index(op.f('ix_actors_actor_id'), table_name='actors')
    op.drop_table('actors')
    # ### end Alembic commands ###
