import os
import sys

sys.path.append(os.getcwd)

from sqlalchemy import (create_engine, PrimaryKeyConstraint, Column, String, Integer, ForeignKey)
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# Set up SQLAlchemy Base and engine
Base = declarative_base()
engine = create_engine('sqlite:///db/concerts.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

# class Concert(Base):
#     pass

class Band(Base):
    __tablename__ = 'bands'

    id = Column(Integer, primary_key=True)
    name = Column(String())
    hometown = Column(String())
    concerts = relationship('Concert', back_populates='band')

    def concerts(self):
        return self.concerts

    def venues(self):
        return [concert.venue for concert in self.concerts]
    
    def play_in_venue(self, venue, date):
        concert = Concert(date=date, band=self, venue=venue)
        session.add(concert)
        session.commit()

    def all_introductions(self):
        return [concert.introduction() for concert in self.concerts]

    @classmethod
    def most_performances(cls):
        return session.query(cls).join(Concert).group_by(cls.id).order_by(func.count().desc()).first()

    def __repr__(self):
        return f'Band: {self.name}'


class Venue(Base):
    __tablename__ = 'venues'

    id = Column(Integer, primary_key=True)
    title = Column(String())
    city = Column(String())
    concerts = relationship('Concert', back_populates='venue')
    
    def concerts(self):
        return self.concerts

    def bands(self):
        return [concert.band for concert in self.concerts]
    
    def concert_on(self, date):
        return session.query(Concert).filter_by(date=date, venue=self).first()

    def most_frequent_band(self):
        band_counts = {}
        for concert in self.concerts:
            band = concert.band
            if band in band_counts:
                band_counts[band] += 1
            else:
                band_counts[band] = 1
        return max(band_counts, key=band_counts.get)

    def __repr__(self):
        return f'Venue: {self.title}'

class Concert(Base):
    __tablename__ = 'concerts'
    id = Column(Integer, primary_key=True)
    date = Column(String)
    name = Column(String)
    band_id = Column(Integer, ForeignKey('bands.id'))
    venue_id = Column(Integer, ForeignKey('venues.id'))
    band = relationship('Band', back_populates='concerts')
    venue = relationship('Venue', back_populates='concerts')

    def band(self):
        return self.band

    def venue(self):
        return self.venue
    
    def hometown_show(self):
        return self.band.hometown == self.venue.city

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
    
    def __repr__(self):
        return f'Concert {self.name}'
