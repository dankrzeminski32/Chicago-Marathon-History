from flask import Blueprint
from src import db
from src.scrapers import history
from src import seeder
from config import TestConfig
from flask_sqlalchemy import SQLAlchemy
from src.services.athlete_service import AthleteService
from src.services.marathon_service import MarathonEventService

db_commands_bp = Blueprint("db", __name__)

@db_commands_bp.cli.command("create")
def create():
    db.create_all()

@db_commands_bp.cli.command("seed")
def seed():
    marathons = history.HistoryMarathonScraper().get_marathons()
    marathon_list = list(marathons.values())
    seed = seeder.Seeder()
    seed.populate_table(marathon_list)
    db.session.commit()
    data = history.HistoryAthleteScraper().get_data()
    print(f"LENGTH OF RETRIEVED DATA, {data}")
    seed.populate_athletes_and_results(data)

@db_commands_bp.cli.command("seedsample")
def seedsample():
    marathons = history.HistoryMarathonScraper().get_marathons()
    marathon_list = list(marathons.values())
    seed = seeder.Seeder()
    seed.populate_table(marathon_list)
    db.session.commit()
    data = history.HistoryAthleteScraper().get_data(sample=True)
    print(f"LENGTH OF RETRIEVED DATA, {data}")
    seed.populate_athletes_and_results(data)

@db_commands_bp.cli.command("recreate")
def recreate():
    db.drop_all()
    db.create_all()


@db_commands_bp.cli.command("test")
def test():
    print(MarathonEventService.get_by_year(2030))
    print(AthleteService.get_all_by_year(2008))