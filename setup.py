from setuptools import setup, find_packages

setup(name='mam20',
      version='1.0.0',
      description='MaM20 Verseny Távirányító monitorozó és konfiguráló eszköz',
      author='Sipos Krisztián',
      license='GPL',
      packages=find_packages(),
      package_data={'': ['*.png']})
