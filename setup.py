#!/usr/bin/env python3
from setuptools import setup

PLUGIN_ENTRY_POINT = 'neon-postag-plugin-nltk=neon_postag_plugin_nltk:NltkPosTagger'

setup(
    name='neon-postag-plugin-nltk',
    version='0.0.1',
    description='A word postag plugin for mycroft',
    url='https://github.com/NeonGeckoCom/neon-postag-plugin-nltk',
    author='JarbasAi',
    author_email='jarbasai@mailfence.com',
    license='Apache-2.0',
    packages=['neon_postag_plugin_nltk'],
    install_requires=["ovos-plugin-manager", "nltk"],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    entry_points={
        'intentbox.postag': PLUGIN_ENTRY_POINT
    }
)
