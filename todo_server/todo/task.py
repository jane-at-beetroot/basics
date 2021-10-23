from flask import Blueprint, request

from .models import Task


bp = Blueprint('task', __name__)

@bp.route('/', methods=['GET', 'POST'])
def task_list():
    if request.method == 'POST':
        data = request.get_json(force=True)
        new_task = Task(**data)
        return new_task.to_json()
    return Task.list_to_json()

@bp.route('/<int:task_id>')
def task_detail(task_id):
    for task in Task.objects:
        if task.id == task_id:
            return task.to_json()