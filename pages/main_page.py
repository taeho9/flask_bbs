from flask_ckeditor import upload_success, upload_fail
from flask import Blueprint, render_template, request, current_app
from sqlalchemy import func
from werkzeug.utils import redirect
from blogger import db
from blogger.models import Post 

bp = Blueprint('main', __name__, url_prefix='/')

@bp.route('/')
def index():
    post_list = Post.query.order_by(Post.id.desc())
    return render_template('views/post_list.html', post_list=post_list)

@bp.route('post_write', methods=["GET","POST"])
def post_write():
    if request.method == "POST":
       post = Post(subject=request.form['subject'], content=request.form['contents'], posting_date=datetime.now())
       db.session.add(post)
       db.session.commit()
       return redirect('/')
    else:
        return render_template('views/post_write.html')

@bp.route('post_view/<int:id>')
def post_view(id):
    post = Post.query.filter(Post.id==id).first()
    return render_template('views/post_view.html', post=post)

@bp.route('post_modify/<int:id>', methods=["GET","POST"]) 
def post_modify(id):
    if request.method == "GET":    # 수정할 글을 보여주면 됨
        post = Post.query.filter(Post.id==id).first()
        return render_template('views/post_modify.html', post=post)
    else: # POST 즉 수정 후 업데이트이면...
        post = Post.query.filter(Post.id==id).first()
        post.subject = request.form['subject']
        post.content = request.form['contents']
        db.session.commit()
        return redirect('/post_view/'+ str(id))

@bp.route('upload/<path:filename>')
def uploaded_image(filename):
    path = '/www_1.0/blogger/ckimages'
    return send_from_directory(path, filename)

@bp.route('upload', methods=['POST','OPTIONS'])
def upload():
    #f = request.files.get('upload')
    f = request.json('upload')
    extension = f.filename.split('.')[-1].lower()
    if extension not in ['jpg','gif','png','jpeg']:
           return upload_fail(message='Image file only!')
    f.save(os.path.join('/www_1.0/blogger/upload'))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)
