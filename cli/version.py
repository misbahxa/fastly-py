import os
import click
import fastly
from cli.handlers import outputsingle

api = fastly.API(key=os.environ['FASTLY_API_KEY'])

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
def listall(service):
    version_line = "{number},{active},{locked},{created_at},{updated_at}"
    print(version_line.replace('{','').replace('}',''))
    for version in api.versions(service):
        print( version_line.format(
            **version.attrs
            )
        )


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
def activeversion(service):
    version_line = "Number: {number}\nActive: {active}\nLocked: {locked}\nCreated_at: {created_at}\nUpdated_at: {updated_at}"
    print( version_line.format( 
        **api.activeversion(service).attrs 
        )
    )

@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
def show(service, version):
    try:
        outputsingle(api.version(service, version).attrs)
    except fastly.errors.NotFoundError:
        print("Version %s does not exists." % version)


@click.command()
@click.option('--service', envvar='FASTLY_SERVICE_ID')
@click.option('--version', required=True)
def clone(service, version):
    ver = api.version(service, version)
    toversion = ver.clone()['number']
    print("Cloned version %s to %s." % (version, toversion) )