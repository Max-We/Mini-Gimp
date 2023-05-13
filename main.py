import click

@click.command()
@click.option('--threshold', type=int, help='Threshold.')
@click.option('--brightness', type=int, help='Threshold.')
@click.option('--contrast', type=int, help='Threshold.')
@click.option('--blur', type=int, help='Threshold.')
@click.option('--sharpen', type=int, help='Threshold.')
def edit(count, name):
    """Simple program that greets NAME for a total of COUNT times."""
    for x in range(count):
        click.echo(f"Hello {name}!")

if __name__ == '__main__':
    edit()