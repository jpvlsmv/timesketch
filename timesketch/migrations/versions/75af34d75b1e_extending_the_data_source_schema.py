"""Extending the data source schema.

Revision ID: 75af34d75b1e
Revises: 41cae2c10cd7
Create Date: 2021-03-19 13:18:17.575912

"""

# This code is auto generated. Ignore linter errors.
# pylint: skip-file


# revision identifiers, used by Alembic.
revision = "75af34d75b1e"
down_revision = "41cae2c10cd7"

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "datasource", sa.Column("error_message", sa.UnicodeText(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("datasource", "error_message")
    # ### end Alembic commands ###
