from setuptools import setup


description = ("Django приложение использования картинок в меньшем качестве для мобильной версии сайта")

setup(
    name='django_img_mobile_vv',
    version='0.1.0',
    author='Vlasov Vitalii',
    author_email='vlasovspk@yandex.ru',
    packages=['django_img_mobile_vv'],
    url='https://github.com/vlasooff',
    license='MIT',
    description=description,
    long_description=open('README.rst').read(),
    zip_safe=False,
    include_package_data=True,
    package_data={'': ['README.rst']},
    install_requires=['django', 'user-agents'],
    classifiers=[
        'Development Status :: 1 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python', 
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)