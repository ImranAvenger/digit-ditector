from setuptools import setup, find_packages

setup(
    name="digit-detector",
    version="0.1.0",
    description="A machine learning model trained to recognize and classify handwritten digits (0-9)",
    py_modules=["app"],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.24.0",
        "Pillow>=10.3.0",
        "scikit-learn>=1.3.0",
        "matplotlib>=3.7.0",
        "tensorflow>=2.13.0",
    ],
)
