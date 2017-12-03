from flask import render_template, Blueprint, request,current_app, redirect,url_for,flash
from simpledu.decorators import admin_required
from simpledu.models import Course, db
from simpledu.forms import CourseForm

admin = Blueprint('admin',__name__,url_prefix='/admin')

@admin.route('/')
@admin_required
def index():
    return render_template('admin/index.html')


@admin.route('/courses')
@admin_required
def course():
    page = request.args.get('page',default=1, type=int)
    pagination = Course.query.paginate(
        page=page,
        per_page=current_app.config['ADMIN_PER_PAGE'],
        error_out = False
    )

    return render_template('admin/courses.html',pagination=pagination)

@admin.route('/courses/create',methods=['GET','POST'])
@admin_required
def create_course():
    form = CourseForm()
    if form.validate_on_submit():
        form.create_course()
        flash('课程创建成功','success')
        return redirect(url_for('admin.course'))
    return render_template('admin/create_course.html',form=form)


@admin.route('/courses/<int:course_id>/edit',methods=['GET','POST'])
@admin_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    form = Course(obj=course)
    if form.validate_on_submit():
        form.update_course(course)
        flash('课程更新成功','success')
        return redirect(url_for('admin.course'))
    return render_template('admin/edit_course.html',form=form,course=course)



@admin.route('/courses/<int:course_id>/delete')
@admin_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    db.session.delete(course)
    db.session.commit()
    flash('课程删除成功', 'success')
    return redirect(url_for('admin.course'))

