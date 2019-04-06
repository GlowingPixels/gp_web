## Glowing Pixels

* Maintainer and Architect.
   * ``Ritankar Paul``
   * ``Kripa Sindhu Bairagi``
   * ``Sounak Biswas``
   * ``Ramyajit Choudhury``
* Email:
   * ``ritankarpaul47@gmail.com``
   * ``kripabairagi0047@gmail.com``

*Rules:*

1. Interested candidate should have some basic knowledge of version control system like {git}.
2. Create a branch and work on some existing issue or new feature.
3. After completion  the current work create a pull request to merge the changes in master branch.
5. Before merging current maintainer will check all changes and can accept/reject the pull request.
7. After merging to ``master`` it may or may not be available in real website

*For Local Setup:*

```
git clone https://github.com/GlowingPixels/GlowingPixelWeb.git
cd GlowingPixelWeb
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 
```

*Basic git guidelines:*
```
git checkout -b [branch_name]
git add --all
git commit -m "[commit message]"
git push [branch_name]
```
