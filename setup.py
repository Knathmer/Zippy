from setuptools import setup, find_packages

setup(
    name="zippy",
    version="0.1.0",
    description="Tray-based archive extractor",
    author="Eraj Anwar",
    packages=find_packages(where="."),
    include_package_data=True, # Finds non python related data like images
    entry_points={
        "console_scripts": [
            "zippy = zippy.main:main" # zippy.main is the module path, and then .main is referencing the main function
        ]
    }
)