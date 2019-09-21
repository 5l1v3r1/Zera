from distutils.dir_util import copy_tree
import click
import pkg_resources

main = click.group()(lambda: None)

@click.command(short_help="initialize project", help="initialize project")
def init():
    copy_tree(pkg_resources.resource_filename(__name__, "example/"), ".")


main.add_command(init)
