from datetime import datetime
from app import db, Artist, Venue, Show, shows

# #Artists
# artist1 = Artist(name="Guns N Petals")
# artist1.city = "San Francisco"
# artist1.genres = ["Rock 'n Roll"]
# artist1.sate = "CA"
# artist1.phone = "326-123-5000"
# artist1.website = "https://www.gunsnpetalsband.com"
# artist1.facebook_link = "https://www.facebook.com/GunsNPetals"
# artist1.seeking_venue = True
# artist1.website = "https://www.gunsnpetalsband.com"
# artist1.seeking_description = "Looking for shows to perform at in the San Francisco Bay Area!"
# artist1.image_link = "https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80"

# db.session.add(artist1)

# artist2 = Artist(name="Matt Quevedo")
# artist2.city = "New York"
# artist2.genres = ["Jazz"]
# artist2.sate = "NY"
# artist2.phone = "300-400-5000"
# artist2.website = ""
# artist2.facebook_link = "https://www.facebook.com/mattquevedo923251523"
# artist2.seeking_venue = False
# artist2.website = "https://www.gunsnpetalsband.com"
# artist2.seeking_description = "Looking for shows to perform at in the San Francisco Bay Area!"
# artist2.image_link = "https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80"

# db.session.add(artist2)

# artist3 = Artist(name="The Wild Sax Band")
# artist3.city = "San Francisco"
# artist3.genres = ["Jazz", "Classical"]
# artist3.sate = "CA"
# artist3.phone = "432-325-5432"
# artist3.website = ""
# artist3.facebook_link = ""
# artist3.seeking_venue = False
# artist3.website = ""
# artist3.seeking_description = ""
# artist3.image_link = "https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80"

# db.session.add(artist3)
# db.session.commit()


# venue1 = Venue(name="The Musical Hop")
# venue1.genres = ["Jazz", "Reggae", "Swing", "Classical", "Folk"]
# venue1.address = "1015 Folsom Street"
# venue1.city = "San Francisco"
# venue1.state = "CA"
# venue1.phone = "123-123-1234"
# venue1.website_link = "https://www.themusicalhop.com"
# venue1.facebook_link = "https://www.facebook.com/TheMusicalHop"
# venue1.seeking_talent = True
# venue1.seeking_description = "We are on the lookout for a local artist to play every two weeks. Please call us."
# venue1.image_link = "https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60"

# db.session.add(venue1)

# venue2 = Venue(name="The Dueling Pianos Bar")
# venue2.genres = ["Classical", "R&B", "Hip-Hop"]
# venue2.address = "335 Delancey Street"
# venue2.city = "New York"
# venue2.state = "NY"
# venue2.phone = "914-003-1132"
# venue2.website_link = "https://www.theduelingpianos.com"
# venue2.facebook_link = "https://www.facebook.com/theduelingpianos"
# venue2.seeking_talent = False
# venue2.seeking_description = ""
# venue2.image_link = "https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80"

# db.session.add(venue2)

# venue3 = Venue(name="Park Square Live Music & Coffee")
# venue3.genres = ["Rock n Roll", "Jazz", "Classical", "Folk"]
# venue3.address = "34 Whiskey Moore Ave"
# venue3.city = "San Francisco"
# venue3.state = "CA"
# venue3.phone = "415-000-1234"
# venue3.website_link = "https://www.parksquarelivemusicandcoffee.com"
# venue3.facebook_link = "https://www.facebook.com/ParkSquareLiveMusicAndCoffee"
# venue3.seeking_talent = False
# venue3.image_link = "https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80"

# db.session.add(venue3)
# db.session.commit()

# datetime(year, month, day, hour, minute, second, microsecond)


# SHOWS
# show1 = Show(venue_id=Venue.query.filter_by(name='The Musical Hop').first().id)
# show1.artist_id = Artist.query.filter_by(name='Guns N Petals').first().id
# show1.start_time = datetime(2019,5,21,21,30)
# db.session.add(show1)

# show2 = Show(venue_id=Venue.query.filter_by(name='Park Square Live Music & Coffee').first().id)
# show2.artist_id = Artist.query.filter_by(name='Matt Quevedo').first().id
# show2.start_time = datetime(2019,6,15,23,00)
# db.session.add(show2)

# show3 = Show(venue_id=Venue.query.filter_by(name='Park Square Live Music & Coffee').first().id)
# show3.artist_id = Artist.query.filter_by(name='The Wild Sax Band').first().id
# show3.start_time = datetime(2035,4,1,20,00)
# db.session.add(show3)

# show4 = Show(venue_id=Venue.query.filter_by(name='Park Square Live Music & Coffee').first().id)
# show4.artist_id = Artist.query.filter_by(name='The Wild Sax Band').first().id
# show4.start_time = datetime(2035,4,1,20,00)
# db.session.add(show4)

# show5 = Show(venue_id=Venue.query.filter_by(name='Park Square Live Music & Coffee').first().id)
# show5.artist_id = Artist.query.filter_by(name='The Wild Sax Band').first().id
# show5.start_time = datetime(2035,4,15,20,00)
# db.session.add(show5)

# db.session.commit()