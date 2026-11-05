import psycopg
from psycopg.rows import dict_row

IMMICH_SOURCE_URI = "postgresql://postgres:YOUR_IMMICH_PASSWORD@YOUR_NAS_IP:5432/immich"
TARGET_COURSE_URI = "postgresql://course_admin:secretpassword@localhost:5433/immich_analytics"

def get_source_conn():
    """Read-only connection to production Immich container."""
    return psycopg.connect(IMMICH_SOURCE_URI, row_factory=dict_row)

def get_target_conn():
    """Write connection to your coursework analytics sandbox."""
    return psycopg.connect(TARGET_COURSE_URI, row_factory=dict_row)