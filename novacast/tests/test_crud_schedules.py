import pytest
from app.db.crud.schedules import create_schedule, get_schedule, update_schedule, delete_schedule
from app.db.models.schedule import Schedule

@pytest.fixture
def sample_schedule():
    return Schedule(id="1", name="Test Schedule", cron_expression="* * * * *")

def test_create_schedule(sample_schedule):
    created_schedule = create_schedule(sample_schedule)
    assert created_schedule.id == sample_schedule.id
    assert created_schedule.name == sample_schedule.name

def test_get_schedule(sample_schedule):
    create_schedule(sample_schedule)
    fetched_schedule = get_schedule(sample_schedule.id)
    assert fetched_schedule.id == sample_schedule.id

def test_update_schedule(sample_schedule):
    create_schedule(sample_schedule)
    sample_schedule.name = "Updated Schedule"
    updated_schedule = update_schedule(sample_schedule)
    assert updated_schedule.name == "Updated Schedule"

def test_delete_schedule(sample_schedule):
    create_schedule(sample_schedule)
    delete_schedule(sample_schedule.id)
    fetched_schedule = get_schedule(sample_schedule.id)
    assert fetched_schedule is None