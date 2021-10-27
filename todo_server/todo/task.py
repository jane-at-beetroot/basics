from flask import Blueprint, request, abort, render_template

from .models import Task
from ..utils.bubble_sort import bubble_sort
from ..utils.insertion_sort import *


bp = Blueprint('task', __name__)

@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form['title']
        priority = request.form['priority']
        new_task = Task(title=title, priority=priority)
    else:
        order = request.args.get(
            'order', default = '', type = str)
        if order:
            bubble_sort(Task.objects, order)
        else:
            insertion_sort(Task.objects)
    return render_template('task_list.html', tasks=Task.objects)


@bp.route('/<int:task_id>')
def task_detail(task_id):
    for task in Task.objects:
        if task.id == task_id:
            return task.to_json()
    else:
        abort(404)