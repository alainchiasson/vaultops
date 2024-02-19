from setuptools import setup, find_packages

setup(
    name='vaultops',
    version='1.0',
    description='Vault operations management',
    author='Alain Chiasson',
    author_email='alain@chiasson.org',
    packages=find_packages(),
    install_requires=[
        'hvac',
    ],
)