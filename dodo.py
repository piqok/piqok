from pathlib import Path


def task_init():
    return {
        'actions': [f'mkdir -p dist build']
    }


def task_test():
    return {
        'actions': ['pytest'],
        'file_dep': list(Path('src').glob('*.py')),
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


def task_upload_test():
    with open('VERSION') as f:
        version = f.read()

    whl = f'dist/piqok-{version}-py3-none-any.whl'
    return {
        'actions': [
            f'python -m twine upload --repository testpypi {whl}'
        ],
        'file_dep': [whl],
        'verbosity': 2,
    }
