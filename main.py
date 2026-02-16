
# Basic Rock Paper Scissors Game
# Name: Rivan
# Date: 2/13/26

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()
#basic needed lists 
choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}
# intro welcome message
console.print("[bold cyan]Welcome to Rock, Paper, Scissors![/bold cyan]")
console.print("[green]You can type 'rock', 'paper', 'scissors' or use 1 for rock, 2 for paper, 3 for scissors.[/green]")
# get and validate the user's choice.
def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	# Keep prompting until user enters a valid choice
	while True:
		user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
		if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
		else:
			user_choice = user_input
		if user_choice in choices:
			break
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")
	#  Use console.input and validate input (accept 1/2/3 or words)
	

#  function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	# Computer randomly selects a choice
	return random.choice(choices)
	

# determine the winner of a round.
def determine_winner(user_choice, computer_choice):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	# Determine round result
	if user_choice == computer_choice:
		return "tie"
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		
		return "user"
	else:
		
		return "computer"
	
	

# print the round result with color.
def print_round_result(user_choice, computer_choice, winner):
	"""Print the choices and the winner of the round using rich colors."""
	console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")
	console.print(f"[bold blue]Human chose: {user_choice}[/bold blue]")
	if winner == "user":
		console.print("[green]you won this round[/green]")
	elif winner == "computer":
		console.print("[red]Computer wins this round![/red]")
	else: 
		console.print("[blue]its a tie![/blue]")

# the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		console.print(f"\n[bold yellow]Round {round_num} of {rounds}[/bold yellow]")
		
		#  Get user and computer choices
		#  Determine winner
		#  Print round result
		#  Update scores
		while True:
			user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
			if user_input in num_to_choice:
				user_choice = num_to_choice[user_input]
			else:
				user_choice = user_input
			if user_choice in choices:
				break
			else:
				console.print("[red]Invalid choice. Please try again.[/red]")
		computer_choice = get_computer_choice()
		winner= determine_winner(user_choice,computer_choice)
		if winner == "user":
			user_score += 1
		elif winner == "computer":
			computer_score += 1
		print_round_result(user_choice, computer_choice,winner)
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")
	elif user_score < computer_score:
		console.print("[bold red]Sorry, the computer wins the game.[/bold red]")
	else:
		console.print("[yellow]It's a tie game![/yellow]")
	
	# Print final scores and announce the overall winner
	console.print("\n[bold underline]Game Over![/bold underline]")
	console.print(f"[cyan]Your score: {user_score}[/cyan]")
	console.print(f"[magenta]Computer score: {computer_score}[/magenta]")

	

if __name__ == "__main__":
	main()
	
