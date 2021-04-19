>>> posts = Post.query.paginate(page=2)
>>> for post in posts.items:
...     print(post)
...
Post('Post 1','2021-04-04 12:52:01.362699')
Post('post 2','2021-04-04 12:52:09.263957')
Post('post 3','2021-04-04 12:52:15.544628')
Post('post 4','2021-04-04 12:52:23.476862')
Post('post 5','2021-04-04 12:52:31.497312')
Post('post 6','2021-04-04 12:52:38.857845')
Post('post 7','2021-04-04 12:52:47.349188')
Post('post 7','2021-04-04 12:52:58.607021')
Post('Post 8','2021-04-04 12:53:09.942270')
Post('post 10','2021-04-04 12:53:25.919107')
>>> posts = Post.query.paginate(per_page=5)
>>> posts.page
1
>>> for post in posts.items:
...     post(post)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
TypeError: 'Post' object is not callable
>>> posts = Post.query.paginate(per_page=5)
>>> for post in posts.items:
...     print(post)
...
Post('python developer updated post 1','2021-04-02 14:46:38.837379')
Post('Our New Developer Hub: Ahoy!','2021-04-02 15:54:37.836326')
Post('Wikipedia:About','2021-04-02 15:56:07.914041')
>>>


>>> from app.models import Post
>>> posts =Post.query.paginate(page=6, per_page=2)
>>> for page in posts.iter_pages():
...     print(page)
...
1
2
None
4
5

Reset User Password
=====================
>>> from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
>>> s = Serializer('secrete', 30)
>>> token = s.dumps({'user_id':1}).decode('utf-8')
>>> token
'eyJhbGciOiJIUzUxMiIsImlhdCI6MTYxNzYzMDY0NSwiZXhwIjoxNjE3NjMwNjc1fQ.eyJ1c2VyX2lkIjo
xfQ.dQUnZxgETJ0GeKts_yY-2BoXdFN_LyWqI0U9A75mC5eclf8d0ZeN4-5xnh79wHISU0-eIdaqnCnCDKb
EFeSVYg'
>>> s.loads(token)
{'user_id': 1}
>>> s.loads(token)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "C:\Users\IBS\python\Flaskblog\venv\lib\site-packages\itsdangerous\jws.py",
line 205, in loads
    date_signed=self.get_issue_date(header),
itsdangerous.exc.SignatureExpired: Signature expired

