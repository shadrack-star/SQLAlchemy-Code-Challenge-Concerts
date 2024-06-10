# Phase 3 Code Challenge: Concerts

For this assignment, we'll be working with a Concert domain.

We have three models: `Band`, `Concert`, and `Venue`.

For our purposes, a `Band` has many `Concert`s, a `Venue` has many `Concert`s,
and a `Concert` belongs to a `Band` and to a `Venue`.

`Band` - `Venue` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- SQLAlchemy Migrations
- SQLAlchemy Relationships
- Class and Instance Methods
- SQLAlchemy Querying

***

## Instructions

To get started, run `pipenv install` while inside of this directory.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge does not have tests. You cannot run `pytest`.
 You'll need to create your own sample instances so
that you can try out your code on your own. Make sure your relationships and
methods work in the console before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session with
your classes defined. You can test out the methods that you write here. You are
also encouraged to use the `seeds.py` file to create sample data to test your
models and relationships.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## What You Already Have

The starter code has migrations and models for the initial `Band` and
`Venue` models, and seed data for some `Band`s and `Venue`s. The
schema currently looks like this:

### `bands` Table

| Column   | Type   |
| -------- | ------ |
| name     | String |
| hometown | String |

### `venues` Table

| Column | Type   |
| ------ | ------ |
| title  | String |
| city   | String |

You will need to create the migration for the `concerts` table using the
attributes specified in the deliverables below.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

Remember: SQLAlchemy give your classes access to a lot of methods already!
Keep in mind what methods SQLAlchemy gives you access to on each of your
classes when you're approaching the deliverables below.

### Migrations

Before working on the rest of the deliverables, you will need to create a
migration for the `concerts` table.

- A `Concert` belongs to a `Band`, and a `Concert` also belongs to a `Venue`. In
  your migration, create any columns your `concerts` table will need to
  establish these relationships.
- The `concerts` table should also have:
  - A `date` column that stores an string.

After creating the `concerts` table using a migration, use the `seeds.py` file
to create instances of your `Concert` class so you can test your code.

**Once you've set up your `concerts` table**, work on building out the following
deliverables.

### Object Relationship Methods

Use SQLAlchemy query methods where
appropriate.

#### Concert

- `Concert band()`
  - should return the `Band` instance for this Concert
- `Concert venue()`
  - should return the `Venue` instance for this Concert

#### Venue

- `Venue concerts()`
  - returns a collection of all the concerts for the `Venue`
- `Venue bands()`
  - returns a collection of all the bands who performed at the `Venue`

#### Band

- `Band concerts()`
  - should return a collection of all the concerts that the `Band` has played
- `Band venues()`
  - should return a collection of all the venues that the `Band` has performed
    at

Use `python debug.py` and check that these methods work before proceeding. For
example, you should be able to call `session.query(Band).first().venues`  and see a list of the
venues for the first band in the database based on your seed data; and `session.query(Band).first()` should return the band for the first concert in the
database.

### Aggregate and Relationship Methods

#### Concert

- `Concert hometown_show()`
  - returns true if the concert is in the band's hometown, false if it is not
- `Concert introduction()`
  - returns a string with the band's introduction for this concert
  - an introduction is in the form:

```txt
"Hello {insert venue city}!!!!! We are {insert band name} and we're from
{insert band hometown}"
```

#### Band

- `Band play_in_venue(venue, date)`
  - takes a venue (`Venue` instance) and date (as a string) as arguments
  - creates a new concert for the band in that venue on that date
- `Band all_introductions()`
  - returns an array of strings representing all the introductions for this band
  - each introduction is in the form:

```txt
"Hello {insert venue city}!!!!! We are {insert band name} and we're from
{insert band hometown}"
```

- `Band most_performances() class method`
  - returns the `Band` instance for the band that has played the most concerts
  - **Note**: solving this using only SQLAlchemy methods is possible, but
    difficult. Feel free to use regular Python enumerable methods here.

#### Venue

- `Venue concert_on(date)`
  - takes a date (string) as argument
  - finds and returns the first concert on that date at that venue
- `Venue most_frequent_band()`
  - returns the band with the most concerts at the venue
  - **Note**: solving this using only SQLAlchemy methods is possible, but
    difficult. Feel free to use regular Python enumerable methods here.
