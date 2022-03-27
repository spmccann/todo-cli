import click
from datetime import datetime
import sqlite3

conn = sqlite3.connect(r"C:\Users\scott\OneDrive\PyCharmProjects\Todo\todo.db")


# conn.execute('''
#     CREATE TABLE TODO
#     (ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
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


@cli.command()
@click.option('--title', prompt='Create task', help='Task user is adding')
@click.option('--desc', prompt='Desc', help='Task Description')
@click.option('--priority', prompt='Priority', help='Priority of task')
def new_task(title, desc, priority):
    """Adds a new task"""
    click.echo("Task saved. Use show-tasks to view")
    date = datetime.now().strftime("%c")
    t = (None, None, title, desc, priority, date, None)
    conn.execute("INSERT INTO todo_app VALUES (?, ?, ?, ?, ?, ?, ?)", t)
    conn.commit()
    conn.close()


@cli.command()
def show_tasks():
    """Shows your tasks"""
    click.echo("All OF YOUR OPEN TASKS:")
    cursor = conn.execute("SELECT id, title, description, priority, date from todo_app")
    for row in cursor:
        click.echo(f"ID: {row[0]}\nTask: {row[1]}\nDescription: {row[2]}\nPriority: {row[3]}\nDate: {row[4]}")
    conn.close()


@cli.command()
@click.option('--id', prompt='ID', help='Task to remove')
@click.option('--edit_t', prompt='Task(edit)', help='Task to edit')
@click.option('--edit_d', prompt='Desc(edit)', help='Desc to edit')
@click.option('--edit_p', prompt='Priority(edit)', help='Priority to edit')
def edit_task(id, edit_t, edit_d, edit_p):
    """Edits a task."""
    t = (edit_t, edit_d, edit_p, id)
    conn.execute("UPDATE todo_app set TITLE = ?, DESCRIPTION = ?, PRIORITY = ? WHERE ID = ?", t)
    conn.commit()
    conn.close()
    click.echo(f"Task {id} has been updated.")




@cli.command()
@click.option('--id', prompt='ID', help='Task to remove')
def resolve_task(id):
    """Resolves a task by id"""
    click.echo(f"Task {id} has been resolved.")
    t = id
    conn.execute("DELETE from todo_app where ID = ?", t)
    conn.commit()
    conn.close()


cli.add_command(new_task)
cli.add_command(show_tasks)
cli.add_command(edit_task)
cli.add_command(resolve_task)
