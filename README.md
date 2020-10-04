# Sample Python Package

## Summary
This is a simple example package created from the packaging-project tutorial at https://packaging.python.org/tutorials/packaging-projects/. <br>
Comments and most of the README content are taken from this tutorial.

You can use
[Github-flavored Markdown](https://guides.github.com/features/mastering-markdown/)
to write your content.

## License
Every package uploaded to the Python Package index should include a license. The license tells users installing the package the terms under which they can use the package. See  https://choosealicense.com/ for picking a license. <br>

In the LICENSE file, paste the text of the license to be used. If the License field is left blank, this means no one will be able to use the package.

## Distribution Pckages
Generate distribution packages for the package, whch are archives uploaded to the Package Index. They can be installed with pip. <br>
1. Ensure the latest versions of `setupttools` and `wheel` are installed:
```python3 -m pip install --user --upgrade setuptools wheel```
2. Run the following command from the same directory where setup.py is located:
``` python3 setup.py sdist bdist_wheel```
3. Once complete, two files should be generated in the `dist` directory: <br>
* Built Distribution, with a **.wh1** extension and 
* Source Archive, with a **.tar.gz** extension<br>
You should always upload a source archive and provide built archives to identify platforms that are compatible with your project.

## Upload your package