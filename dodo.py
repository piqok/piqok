from pathlib import Path
import pytest


def task_init():
    return {
        'actions': [f'mkdir -p dist build']
    }


def task_test():
    def test():
        pytest.main(['-v'])

    return {
        'actions': [test],
        'file_dep': list(Path('piqok').glob('*.py')),
        'verbosity': 2,
    }


def task_build():
    return {
        'actions': [
            'python setup.py sdist bdist_wheel'
        ],
        'file_dep': ['VERSION'],
    }


def task_local_install():
    return {
        'actions': ['python setup.py install'],
        'file_dep': list(Path('dist').glob('*')),
    }


def task_upload():
    with open('VERSION') as f:
        version = f.read()

    whl = f'dist/piqok-{version}-py3-none-any.whl'
    return {
        'actions': [
            f'python -m twine upload {whl}'
        ],
        'file_dep': [whl],
        'uptodate': [True],
        'verbosity': 2,
    }
