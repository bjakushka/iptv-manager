from .demo_data import DemoDataSeeder

SEEDER_MAP = {
    'DemoDataSeeder': DemoDataSeeder
}


def run_seeder(name, db):
    """Runs specific db-seeder by its class name

    :param string name: Name of seeder-class to run
    :param flask_sqlalchemy.SQLAlchemy db: Instance of database
    :return:
    """
    _SeederClass = SEEDER_MAP.get(name, None)
    if not _SeederClass:
        raise Exception(
            f'Seeder with name `{name}` could not be found'
        )

    seeder = _SeederClass(db)
    seeder.run()
