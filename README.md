# Sample Python Package

## Summary
This is a simple example package created from the packaging-project tutorial at https://packaging.python.org/tutorials/packaging-projects/. <br>
Comments and most of the README content are taken from this tutorial.<br>
Note:
You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## License
Every package uploaded to the Python Package index should include a license. The license tells users installing the package the terms under which they can use the package. See  https://choosealicense.com/ for picking a license. <br>

In the LICENSE file, paste the text of the license to be used. If the License field is left blank, this means no one will be able to use the package.

## Generating Distribution Packages
Generate distribution packages for the package, which are archives uploaded to the Package Index. They can be installed with pip. <br>
1. Ensure the latest versions of `setupttools` and `wheel` are installed with this command:<br>
```python3 -m pip install --user --upgrade setuptools wheel```
2. Run the following command from the same directory where setup.py is located:<br>
``` python3 setup.py sdist bdist_wheel```
3. Once complete, two files should be generated in the `dist` directory: <br>
* Built Distribution, with a **.wh1** extension and 
* Source Archive, with a **.tar.gz** extension<br>
You should always upload a source archive and provide built archives to identify platforms that are compatible with your project.

## Upload your package
Follow these steps to upload the package to the Python Package Index.<br>
1. First, register an account on Test PyPI https://test.pypi.org/account/register/ at  (used for testing and experimentation).
2. Create a PyPI API token at https://test.pypi.org/manage/account/#api-tokens in order to securely upload the project. Make sure to copy and save the token before closing this page.
3. Install `Twine` in order to upload the distribution packages:<br>
```python3 -m pip install --user --upgrade twine```
4. Run the following command to upload all of the archives under `dist`:<br>
``` python3 -m twine upload --repository testpypi dist/*```
5. When prompted for a username and password, use `__token__` for the username. For the password, use the token value **prefixed with `pypi`**<br>
Once uploaded, the package should be viewable on TestPYPI, e.g., https://test.pypi.org/project/example-pkg-YOUR-USERNAME-HERE.

## Install package
Use pip to install the package and verify that it works.
1. Create a new virtualenv and install your package from TestPyPI:<br>
``` python3 -m pip install --index-url https://test.pypi.org/simple/ --no-deps example-pkg-YOUR-USERNAME-HERE```
2. Make sure to specify your username in the package name.
3. Ensure it was installed correctly by importing the package. Run the Python interpreter in the virtualevn with the `python` commnd.
4. From the interpreter shell, import the package:<br>
```>>> import example_pkg```