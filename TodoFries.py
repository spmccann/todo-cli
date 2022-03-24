import click
from datetime import datetime
import sqlite3

conn = sqlite3.connect('tasks.db')

# conn.execute('''
#     CREATE TABLE TODO
#     (ID INTEGER PRIMARY KEY,
#     DATE           TEXT,
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
click.echo("                                 Version 0.01\n")


@click.group()
def cli():
    pass

# need to create a users db before I can do this
# @cli.command()
# @click.option('--name', prompt='Enter name', help='Set your name')
# def set_name(name):
#     """Set your username"""
#     conn.execute(f"INSERT INTO TOO (NAME) VALUES ('{name}')")


@cli.command()
@click.option('--task', prompt='Create task', help='Task user is adding')
@click.option('--desc', prompt='Desc', help='Task Description')
@click.option('--priority', prompt='Priority', help='Priority of task')
def new_task(task, desc, priority):
    """Adds a new task"""
    date = datetime.now().strftime("%c")
    click.echo("Task saved. Use show-tasks to view")
    conn.execute(f"INSERT INTO TODO (DATE, TASK, DESCRIPTION, PRIORITY) VALUES ('{date}', '{task}', '{desc}', '{priority}')")
    conn.commit()
    conn.close()


@cli.command()
def show_tasks():
    """Shows your tasks"""
    click.echo("All OF YOUR OPEN TASKS:")
    cursor = conn.execute("SELECT id, task, description, priority, date from TODO")
    for row in cursor:
        click.echo(f"ID: {row[0]}\nTask: {row[1]}\nDescription: {row[2]}\nPriority: {row[3]}\nDate: {row[4]}")
    conn.close()


@cli.command()
@click.option('--task_id', prompt='ID', help='Task to remove')
@click.option('--edit_t', prompt='Task(edit)', help='Task to edit')
@click.option('--edit_d', prompt='Desc(edit)', help='Desc to edit')
@click.option('--edit_p', prompt='Priority(edit)', help='Priority to edit')
def edit_task(task_id, edit_t, edit_d, edit_p):
    """Edits a task."""
    conn.execute(f"UPDATE TODO set TASK = '{edit_t}', DESCRIPTION = '{edit_d}', PRIORITY = '{edit_p}' where ID = {task_id}")
    conn.commit()
    conn.close()
    click.echo(f"Task {task_id} has been updated.")


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
cli.add_command(edit_task)
cli.add_command(resolve_task)
