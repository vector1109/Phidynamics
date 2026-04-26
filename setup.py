from setuptools import setup, find_packages

setup(
    name="phidynamics",
    version="0.1.1",
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "matplotlib",
    ],
    author="Fabian",
    description="Framework de Bio-Geometría Fractal y Torsión",
)