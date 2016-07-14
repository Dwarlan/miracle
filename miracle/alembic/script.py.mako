"""${message}

Revision ID: ${up_revision}
Revises: ${down_revision}
Create Date: ${create_date}
"""

import logging

from alembic import op
import sqlalchemy as sa
${imports if imports else ""}

log = logging.getLogger('alembic.migration')
revision = ${repr(up_revision)}
down_revision = ${repr(down_revision)}


def upgrade():
    log.info('Upgrade')
    ${upgrades if upgrades else "pass"}


def downgrade():
    log.info('Downgrade')
    ${downgrades if downgrades else "pass"}
