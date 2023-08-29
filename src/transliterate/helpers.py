import os

__author__ = 'Artur Barseghyan'
__copyright__ = '2013-2018 Artur Barseghyan'
__license__ = 'GPL-2.0-only OR LGPL-2.1-or-later'
__all__ = (
    'PROJECT_DIR',
    'project_dir',
)


def project_dir(base):
    """Project dir."""
    return os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            (os.path.join(*base) if isinstance(base, (list, tuple)) else base)
        ).replace('\\', '/')
    )


PROJECT_DIR = project_dir
