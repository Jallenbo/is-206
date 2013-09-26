# coding=utf-8
from sys import exit
from random import randint

class Scene(object):
	def enter(self):
		exit(1)
		
class Galtvang(Scene):
	def enter(self):
		print "Du skal begynne på Galtvort høyere skole for hekseri og trolldom,"
		print "og trenger flere ting til skolestart."
		print "Du har ankommet Galtvang, og skal handle det du trenger."
		print "Først av alt trenger du en tryllestav."
		print "For å få tak i dette må du besøke denne mannen. Hvem?"
		
		secret_word = "Olivander"
		
		guess = raw_input("Tryllestavmann: ")
		
		if guess == secret_word:
			print "Det stemmer! Gå videre til bokhandelen"
			return 'bokhandel'
			
		else:
			print "Feil! Gå tilbake til Galtvang."
			return 'galtvang'

class Bokhandel(Scene):
	def enter(self):
		print """Nå må du handle bøker. Sammen med vennene dine besøker du bokhandelen. 
		En mann står utenfor og slipper ikke folk inn med mindre de gjetter hva slags 
		farge det er på underbuksene hans. Hvis du gjetter feil sender han deg hjem
		med første tog. Du får tre forsøk."""
		
		secret_word = "rosa"
		
		guess = raw_input("Farge: ")
		guesses = 0
		while guess != secret_word and guesses < 3:
			print "Det var ikke rett farge. Prøv igjen."
			guesses += 1
			guess = raw_input("Farge: ")
		
		if guess == secret_word:
			print "Korrekt! Mannen skammet seg over fargen, og løp hjem."
			print "Du fikk bøkene du skulle, men treffer på Draco Malfang."
			print "Han tar alle bøkene og løper inn i banken."
			print "Du løper etter ham."
			return 'bank'
			
		else:
			print "Du tar toget hjem. Drømmen om å bli en stor trollmann er knust."
			exit(1)
			
class Bank(Scene):
	def enter(self):
		print """Du tar igjen Draco inne i banken, men han nekter å gi bøkene tilbake,
		med mindre du klarer å gjette hvilket tall han tenker på.
		Draco gir deg fem forsøk, og et hint: Tallet er mellom 10 og 70."""
		
		secret_number = "%d%d" % (randint(1,9), randint(0,9))
		
		guess = raw_input("Tall: ")
		guesses = 0
		while guess != secret_number and guesses < 5:
			print "Feil tall, min venn. Prøv igjen."
			guesses += 1
			guess = raw_input("Tall: ")
			
		if guess == secret_number:
			print "Draco kaster fra seg bøkene, og spankulerer ut av banken."
			print "Nå mangler trenger du kun å komme deg inn på skolen."
			return 'galtvort'
			
		else:
			print "Draco tok alle bøkene. Du måtte gi opp drømmen om å bli trollmann."
			exit(1)

class Galtvort(Scene):
	def enter(self):
		print """Det siste hinderet blir å komme seg inn døren.
		For å gjøre det vanskelig har rektoren lagt fem identiske inngangsdører.
		Den ene fører inn på skolen, de andre fører tilbake til Galtvang.
		Hvilken velger du?"""
		
		entrance = randint(1,5)
		guess = raw_input("Dør: ")
		
		if int(guess) == entrance:
			print "Gratulerer! Du kan nå begynne studiene ved Galtvort."
			exit(1)
		
		else:
			print "Feil dør. Ingen studier på deg. Tilbake til Galtvang med deg!"
			return 'galtvang'