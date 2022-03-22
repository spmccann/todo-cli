import click
from datetime import datetime

click.echo(" _____         _         _____     _           ")
click.echo("|_   _|__   __| | ___   |  ___| __(_) ___  ___ ")
click.echo("  | |/ _ \ / _` |/ _ \  | |_ | '__| |/ _ \/ __|")
click.echo("  | | (_) | (_| | (_) | |  _|| |  | |  __/\__  ")
click.echo("  |_|\___/ \__,_|\___/  |_|  |_|  |_|\___||___/")
click.echo("Version 0.01\n")


@click.group()
def cli():
    pass


@cli.command()
@click.option('--task', prompt='Create task', help='Task user is adding')
@click.option('--desc', prompt='Desc', help='Task Description')
@click.option('--priority', prompt='Priority', help='Priority of task')
@click.argument('out', type=click.File('a'), default='tasks.txt')
def new_task(task, desc, priority, out):
    """Adds a new task"""
    click.echo("Task saved. Use show-tasks to view")
    date = datetime.now().strftime("%c")
    task_id = 0
    with open('tasks.txt') as f:
        for line in f.readlines():
            if 'ID:' in line:
                task_id += 1
    out.write(f"ID: {task_id}\nDate: {date}\nTask: {task}\nDescription: {desc}\nPriority: {priority}\n\n")


@cli.command()
@click.argument('file', type=click.File('r'), default="tasks.txt")
def show_tasks(file):
    """Shows your tasks"""
    click.echo("All OF YOUR OPEN TASKS:")
    click.echo(file.read())


@cli.command()
@click.option('--id', prompt='ID', help='Task to remove')
def resolve_task(id):
    """Resolves a task by id"""
    with open("tasks.txt") as f:
        for line in f.readlines():
            if f'ID: {id}' in line:
                click.echo(f"Task {id} deleted.")
        else:
            click.echo("Task id not found.")


cli.add_command(new_task)
cli.add_command(show_tasks)
cli.add_command(resolve_task)
