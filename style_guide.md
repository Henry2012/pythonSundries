-----------------------------------------------------
###[Night Seminar by PC][1]###
* 质疑：Instance Variables: lower_with_underscore?

```python
class CompName():
    pass

comp_name = CompName()
```

* eclipse: pydev, code analysis
    * pep8.py: --ignore=E501,W2
    * options

* Splitting lines

```python
twist = ('Peter Piper '
    	 'split a set '
		 'of simple strings')

# deprecated		 
zero_duration_videos = video_models.Video.all().filter("duration =", 0).fetch(10000) 

# recommended
zero_duration_videos = (video_models.Video.all()
                        .filter("duration =", 0)
                        .fetch(10000))

# deprecated						
kwargs = dict((str(key), value) for key, value in topic_json.iteritems() if key in ['id', 'title', 'standalone_title', 'description', 'tags', 'hide']) 

# recommended
kwargs = dict((str(key), value)
              for key, value in topic_json.iteritems()
              if key in ['id', 'title', 'standalone_title',
                         'description', 'tags', 'hide'])

# deprecated						 
topics_list = [t for t in topics if not (
    (t.standalone_title == "California Standards Test: Algebra I" and t.id != "algebra-i") or
    (t.standalone_title == "California Standards Test: Geometry" and t.id != "geometry-2"))
    ]

# recommended
bad_title_and_ids = [("California Standards Test: Algebra I", "algebra-i"),
                     ("California Standards Test: Geometry", "geometry-2"),
                    ]
topics_list = [t for t in topics
               if not (t.standalone_title, t.id) in bad_title_and_ids]
```
    
###Reference###
1. https://pep8.readthedocs.org/en/latest/intro.html?highlight=ignore
2. http://www.python.org/dev/peps/pep-0008/#naming-conventions
3. http://pychecker.sourceforge.net/
4. https://sites.google.com/a/khanacademy.org/forge/for-developers/styleguide/python
5. http://zh-google-styleguide.readthedocs.org/en/latest/google-python-styleguide/



[1]: http://google-styleguide.googlecode.com/svn/trunk/pyguide.html

-----------------------------------------------------
###Rename Repo in Github###

![alt text][demo]
Setting --> Repository Name Rename
![alt text][rename]
[demo]: /images/rename_repo.png "Demo"
[rename]: /images/setting.png "Rename"
