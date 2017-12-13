import os
import setuptools


# TODO: update
requirements = [
    "numpy",
    "scipy",
    "keras"
]


def readme():
    base_dir = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(base_dir, 'README.md')) as f:
        return f.read()


def setup():
    setuptools.setup(
        name="innvestigate",
        version="0.1",
        description=("A toolbox to innvestigate neural networks decisions."),
        long_description=readme(),
        classifiers=[
            "License :: OSI Approved :: ",
            "Development Status :: 3 - Alpha",
            "Environment :: Console",
            "Intended Audience :: Science/Research",
            "Operating System :: POSIX :: Linux",
            "Programming Language :: Python :: 2.7",
            "Programming Language :: Python :: 3.4",
            "Topic :: Scientific/Engineering :: Artificial Intelligence",
        ],
        url="https://github.com/albermax/innvestigate",
        author="Maxmilian Alber,Pieter-Jan Kindermans",
        author_email="workDoTalberDoTmaximilian@gmail.com",
        license="MIT",
        packages=["innvestigate"],
        install_requires=requirements,
        include_package_data=True,
        zip_safe=False,
    )
    pass


if __name__ == "__main__":
    setup()