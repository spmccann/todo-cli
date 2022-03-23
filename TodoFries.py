import click
from datetime import datetime
import sqlite3

conn = sqlite3.connect('test.db')

# conn.execute('''
#     CREATE TABLE TODO
#     (ID INTEGER PRIMARY KEY, DATA,
#     NAME           TEXT,
#     TASK           TEXT,
#     DESCRIPTION    TEXT,
#     PRIORITY       TEXT);
# ''')
#
# conn.close()

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
def new_task(task, desc, priority):
    """Adds a new task"""
    click.echo("Task saved. Use show-tasks to view")
    conn.execute(f"INSERT INTO TODO (TASK, DESCRIPTION, PRIORITY) VALUES ('{task}', '{desc}', '{priority}')")
    conn.commit()
    conn.close()


@cli.command()
@click.argument('file', type=click.File('r'), default="tasks.txt")
def show_tasks(file):
    """Shows your tasks"""
    click.echo("All OF YOUR OPEN TASKS:")
    cursor = conn.execute("SELECT id, task, description, priority from TODO")
    for row in cursor:
        click.echo(f"ID: {row[0]}\nTask: {row[1]}\nDescription: {row[2]}\nPriority: {row[3]}\n\n")
    conn.close()


@cli.command()
@click.option('--task_id', prompt='ID', help='Task to remove')
def resolve_task(task_id):
    """Resolves a task by id"""
    click.echo(f"Task {task_id} has been resolved.")
    conn.execute(f"DELETE from TODO where ID = {task_id}")
    conn.commit()
    conn.close()


cli.add_command(new_task)
cli.add_command(show_tasks)
cli.add_command(resolve_task)
