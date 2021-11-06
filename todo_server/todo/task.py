from copy import deepcopy

from flask import Blueprint, request, abort, render_template

from .models import Task
from ..utils.bubble_sort import bubble_sort
from ..utils.insertion_sort import *


bp = Blueprint('task', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/task', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        title = request.form['title']
        priority = int(request.form['priority'])
        new_task = Task(title=title, priority=priority)
    else:
        order = request.args.get(
            'order', default = '', type = str)
        tasks = deepcopy(Task.objects)
        if order:
            bubble_sort(tasks, order)
        else:
            insertion_sort(tasks)
    return render_template('task_list.html', tasks=tasks)


@bp.route('/<int:task_id>')
def task_detail(task_id):
    for task in Task.objects:
        if task.id == task_id:
            return task.to_json()
    else:
        abort(404)