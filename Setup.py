from setuptools import setup, find_packages

setup(
    name='genesis_code_protocol',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai',
        'transformers',
        'torch',
        'numpy',
        'scipy',
        'matplotlib',
        'jupyter',
        'notebook',
        'pandas'
    ],
    entry_points={
        'console_scripts': [
            'gcp-run=genesis_code_protocol.main:run'
        ]
    }
)
