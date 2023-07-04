#i really need to comment this lol

import pygame
from random import shuffle
pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))

class Player:
	def __init__(self, number):
		self.alive = True
		self.number = number
		self.handmaid = False

class Card:
	def __init__(self, type, number, id):
		self.type = type
		self.number = number
		self.id = id


class Button:
	def __init__(self, card, x, y, color, turn, pos):
		self.x = x
		self.y = y
		self.color = color
		self.width = 150
		self.height = 100
		self.active = False
		self.turn = turn
		self.pos = pos
		#print(card)
		try:
			self.type = card.type
			self.id = card.id
			self.number = card.number
			#print(card.number)
		except:
			self.type = card


	def draw(self, win, globalTurn):
		pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
		font = pygame.font.SysFont("comicsans", 40)
		text = font.render(self.type, 1, (255,255,255))
		if self.turn == globalTurn:
			win.blit(text, (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)))

	def click(self, pos):
		x1 = pos[0]
		y1 = pos[1]
		if self.x <= x1 <= self.x + self.width and self.y <= y1 <= self.y + self.height:
			return True
		else:
			return False

	def toggle(self):
		self.active = not self.active


def redrawWindow(win):
	global turn
	try:
		win.fill((128,128,128))

		drawCard.draw(win, drawCard.turn)
		for btn in btns:
			#print(btn.active)
			if btn.active:
				#print("yes1")
				btn.draw(win, turn)
		for btn in btns2:
			if btn.active:
				btn.draw(win, turn)

		pygame.display.update()

	except pygame.error as e:
		print(e)
		pass
# define the function blocks
def guard(current_btn, current_btns):
	global end, won, turn, players
	clock = pygame.time.Clock()

	stale = 0

	for p in players:
		if not p.handmaid and p.alive:
			stale += 1

	if stale == 1:
		print("No effect")
		return

	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos) and btn.active and turn != 1 and not players[btn.turn - 1].handmaid:
						#print("speak")
						guess = input()
						while guess == "Guard":
							print("Cannot guess Guard, try again")
							guess = input()
						print(f"Player {turn} has used Guard")
						if guess == btn.type:
							#print("yes")
							print(f"Player {turn} has guessed {btn.type}, and eliminated Player {btn.turn}")
							players[btn.turn - 1].alive = False
						else:
							print(f"Player {turn} has guessed {guess} to no prevail")
						#print("complete")
						return


				for btn in btns2:
					if btn.click(pos) and btn.active and turn != 2 and not players[btn.turn - 1].handmaid:
						#print("speak")
						guess = input()
						while guess == "Guard":
							print("Cannot guess Guard, try again")
							guess = input()
						print(f"Player {turn} has used Guard")
						if guess == btn.type:
							#print("yes")
							print(f"Player {turn} has guessed {btn.type}, and eliminated Player {btn.turn}")
							players[btn.turn - 1].alive = False
						else:
							print(f"Player {turn} has guessed {guess} to no prevail")
						#print("complete")
						return
		redrawWindow(win)

def priest(current_btn, current_btns):
	global end, won, turn, players
	clock = pygame.time.Clock()

	stale = 0

	for p in players:
		if not p.handmaid and p.alive:
			stale += 1

	if stale == 1:
		print("No effect")
		return

	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos) and btn.active and turn != 1 and not players[btn.turn - 1].handmaid:
						btn.draw(win, btn.turn)
						print(f"Player {turn} used Priest, and viewed Player {btn.turn}'s hand ({btn.type})")
						pygame.display.update()
						pygame.time.delay(1000)
						return


				for btn in btns2:
					if btn.click(pos) and btn.active and turn != 2 and not players[btn.turn - 1].handmaid:
						btn.draw(win, btn.turn)
						print(f"Player {turn} used Priest, and viewed Player {btn.turn}'s hand ({btn.type})")
						pygame.display.update()
						pygame.time.delay(1000)
						return

		redrawWindow(win)

def baron(current_btn, current_btns):
	global end, won, turn, players
	clock = pygame.time.Clock()

	stale = 0

	for p in players:
		if not p.handmaid and p.alive:
			stale += 1

	if stale == 1:
		print("No effect")
		return

	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos) and btn.active and turn != 1 and not players[btn.turn - 1].handmaid:
						btn.draw(win, btn.turn)
						if current_btn.number > btn.number:
							print(f"Player {turn} used Baron, and beat Player {btn.turn}'s {btn.type} with a {current_btn.type}")
							players[btn.turn - 1].alive = False
						elif btn.number > current_btn.number:
							print(f"Player {turn} used Baron, and lost against Player {btn.turn}'s {btn.type} with a {current_btn.type}")
							players[current_btn.turn - 1].alive = False
						else:
							print(f"Player {turn} used Baron, and tied against Player {btn.turn}'s {btn.type} with a {current_btn.type}")
						pygame.display.update()
						pygame.time.delay(1000)
						return


				for btn in btns2:
					if btn.click(pos) and btn.active and not players[btn.turn - 1].handmaid:
						btn.draw(win, btn.turn)
						if current_btn.number > btn.number:
							print(f"Player {turn} used Baron, and beat Player {btn.turn}'s {btn.type} with a {current_btn.type}")
							players[btn.turn - 1].alive = False
						elif btn.number > current_btn.number:
							print(f"Player {turn} used Baron, and lost against Player {btn.turn}'s {btn.type} with a {current_btn.type}")
							players[current_btn.turn - 1].alive = False
						else:
							print(f"Player {turn} used Baron, and tied against Player {btn.turn}'s {btn.type} with a {current_btn.type}")
						pygame.display.update()
						pygame.time.delay(1000)
						return



		redrawWindow(win)

def handmaid(current_btn, current_btns):
	players[turn - 1].handmaid = True
	print(f"Player {turn} used Handmaid")
	
def prince(current_btn, current_btns):
	global end, won, turn, players
	clock = pygame.time.Clock()

	stale = 0

	for p in players:
		if not p.handmaid and p.alive:
			stale += 1

	if stale == 1:
		print("No effect")
		return

	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos) and btn.active and turn != 1 and not players[btn.turn - 1].handmaid:
						btn.toggle()
						print(f"Player {turn} used Prince, Player {btn.turn} has discarded their hand ({btn.type})")
						if btn.number == 8:
							print(f"Player {btn.turn} has been eliminated for discarding the Princess")
							players[btn.turn - 1].alive = False
						else:
							draw_card(btns)
						return


				for btn in btns2:
					if btn.click(pos) and btn.active and turn != 2 and not players[btn.turn - 1].handmaid:
						btn.toggle()
						print(f"Player {turn} used Prince, Player {btn.turn} has discarded their hand ({btn.type})")
						if btn.number == 8:
							print(f"Player {btn.turn} has been eliminated for discarding the Princess")
							players[btn.turn - 1].alive = False
						else:
							draw_card(btns2)
						return
	
def king(current_btn, current_btns):
	global end, won, turn, players
	clock = pygame.time.Clock()

	stale = 0

	for p in players:
		if not p.handmaid and p.alive:
			stale += 1

	if stale == 1:
		print("No effect")
		return

	while True:
		clock.tick(60)

		for event in pygame.event.get():
			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos) and btn.active and turn != 1 and not players[btn.turn - 1].handmaid:
						print(f"Player {turn} used King")
						print(f"Player {turn} switched his {current_btn.type} for Player {btn.turn}'s {btn.type}")
						transfer = Card(current_btn.type, current_btn.number, current_btn.id)
						current_btns[current_btn.pos].type = btn.type
						current_btns[current_btn.pos].number = btn.number
						current_btns[current_btn.pod].id = btn.id
						btns[btn.pos].type = transfer.type
						btns[btn.pos].number = transfer.number
						btns[btn.pos].id = transfer.id
						return
						

				for btn in btns2:
					if btn.click(pos) and btn.active and turn != 2 and not players[btn.turn - 1].handmaid:
						print(f"Player {turn} used King")
						print(f"Player {turn} switched his {current_btn.type} for Player {btn.turn}'s {btn.type}")
						transfer = current_btn
						current_btn = btn
						btn = transfer
						return
	
def countess(current_btn, current_btns):
	print(f"Player {turn} used Countess")
	
def princess(current_btn, current_btns):
	pass
	


# map the inputs to the function blocks
options = {1 : guard,
		   2 : priest,
		   3 : baron,
		   4 : handmaid,
		   5 : prince,
		   6 : king,
		   7 : countess,
		   8 : princess
}

def draw_card(btns):
	global end
	for btn in btns:
		if not btn.active:
			try:
				btn.type = cards[0].type
				btn.number = cards[0].number
				btn.id = cards[0].id

				print(f"Player {btn.turn} drew {btn.type}")

				if len(cards) > 0:

					del cards[0]

				btn.toggle()
				#print(btn.active)
				drawCard.type = f"Draw ({len(cards)} left)"
			except:
				end = True
			return


global btns, btns2, cards, players, drawCard, end, won, turn

def main():
	run = True
	global btns, btns2, cards, players, drawCard, end, won, turn
	turn = 1
	clock = pygame.time.Clock()


	#cards = [Card("Prince", 5, 0), Card("Prince", 5, 1), Card("Countess", 7, 2), Card("Countess", 7, 3)]
	cards = [Card("Guard", 1, 0), Card("Guard", 1, 1), Card("Guard", 1, 2), Card("Guard", 1, 3), Card("Guard", 1, 4), Card("Priest", 2, 5), Card("Priest", 2, 6), Card("Baron", 3, 7), Card("Baron", 3, 8), Card("Handmaid", 4, 9), Card("Handmaid", 4, 10), Card("Prince", 5, 11), Card("Prince", 5, 12), Card("King", 6, 13), Card("Countess", 7, 14)]
	shuffle(cards)
	btns = [Button('foo', 50, 500, (0,0,0), 1, 0), Button('foo', 250, 500, (255,0,0), 1, 1)]
	btns2 = [Button('foo', 50, 200, (0,0,0), 2, 0), Button('foo', 250, 200, (255,0,0), 2, 1)]
	players = [Player(1), Player(2)]
	drawCard = Button(f"Draw ({len(cards)} left)", width/2, 300, (0,255,0), 1, 0)
	end = False
	won = False
	secretCard = cards[0]
	del cards[0]
	draw_card(btns)
	draw_card(btns2)
	draw_card(btns)
	#print(btns[0].active)

	while run:
		clock.tick(60)
		font = pygame.font.SysFont("comicsans", 40)
		text = font.render((str(turn)), 1, (255,255,255))
		#print(p1Turn, p2Turn)
		win.blit(text, (100, 100))
		for p in players:
			pass



		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()

			if event.type == pygame.MOUSEBUTTONDOWN:
				pos = pygame.mouse.get_pos()
				for btn in btns:
					if btn.click(pos) and btn.active and turn == 1:
						for new_btn in btns:
							if new_btn != btn:
								compareBtn = new_btn
						royal = ["Prince", "King"]
						if btn.type in royal and compareBtn.type == "Countess":
							print("Must play countess")
						else:
							players[turn - 1].handmaid = False

							btn.toggle()
							

							options[btn.number](compareBtn, btns)
							drawCard.type = f"Draw ({len(cards)} left)"

							draw_card(btns2)

							turn = 2

				for btn in btns2:
					if btn.click(pos) and btn.active and turn == 2:
						for new_btn in btns:
							if new_btn != btn:
								compareBtn = new_btn
						royal = ["Prince", "King"]
						if btn.type in royal and compareBtn.type == "Countess":
							print("Must play countess")
						else:
							players[turn - 1].handmaid = False

							btn.toggle()
							

							options[btn.number](compareBtn, btns2)
							drawCard.type = f"Draw ({len(cards)} left)"

							draw_card(btns)

							turn = 1


				x = []
				for p in players:
					if p.alive:
						x.append(p)

				if len(x) == 1:
					end = True
					won = True
					winner = x[0]

				if end:
					print("Game end")
					font = pygame.font.SysFont("comicsans", 60)
					text = font.render("End", 1, (255,0,0))
					win.blit(text, (100,200))
					redrawWindow(win)
					if not won:
						for _btn in btns:
							if _btn.active:
								p1Won = _btn.number
						for _btn in btns2:
							if _btn.active:
								p2Won = _btn.number
						if p1Won > p2Won:
							winner = players[0]
						elif p2Won > p1Won:
							winner = players[1]
						else:
							winner = Player("tie")
					print(f"Winner is player {winner.number}")
					font = pygame.font.SysFont("comicsans", 60)
					text = font.render(f"Winner is player {winner.number}", 1, (255,0,0))
					win.blit(text, (230,100))
					pygame.display.update()
					pygame.time.delay(2000)
					run = False




		redrawWindow(win)

def menu_screen():
	run = True
	clock = pygame.time.Clock()

	try:

		while run:
			clock.tick(60)
			win.fill((128, 128, 128))
			font = pygame.font.SysFont("comicsans", 60)
			text = font.render("Click to Play!", 1, (255,0,0))
			win.blit(text, (100,200))
			pygame.display.update()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					run = False
				if event.type == pygame.MOUSEBUTTONDOWN:
					run = False

		main()
	except pygame.error:
		pass

while True:
	menu_screen()

