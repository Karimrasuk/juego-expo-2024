import pygame
import random
import sys

# Inicializa Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Blackjack")

# Colores
GREEN = (0, 128, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Fuente
font = pygame.font.SysFont("Arial", 36)

# Baraja de cartas
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [(rank, suit) for rank in ranks for suit in suits]

def deal_card():
    return deck.pop(random.randint(0, len(deck) - 1))

def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        rank = card[0]
        if rank in ['K', 'Q', 'J']:
            value += 10
        elif rank == 'A':
            aces += 1
            value += 11
        else:
            value += int(rank)
    while value > 21 and aces:
        value -= 10
        aces -= 1
    return value

def draw_hand(hand, x, y):
    for i, card in enumerate(hand):
        text = font.render(f"{card[0]} of {card[1]}", True, WHITE)
        screen.blit(text, (x, y + i * 40))

def show_result(message):
    text = font.render(message, True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))

def main():
    global deck
    deck = [(rank, suit) for rank in ranks for suit in suits]  # Reiniciar la baraja
    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]
    
    clock = pygame.time.Clock()
    running = True
    game_over = False
    player_standing = False

    while running:
        screen.fill(GREEN)
        
        # Mostrar manos
        draw_hand(player_hand, 50, 50)
        draw_hand(dealer_hand, 400, 50)

        # Calcular valores
        player_value = calculate_hand_value(player_hand)
        dealer_value = calculate_hand_value(dealer_hand)

        player_text = font.render(f"Player Value: {player_value}", True, WHITE)
        dealer_text = font.render(f"Dealer Value: {dealer_value}", True, WHITE)
        screen.blit(player_text, (50, 300))
        screen.blit(dealer_text, (400, 300))

        # Mostrar resultado si el juego ha terminado
        if game_over:
            if player_value > 21:
                show_result("¡Perdiste! Te pasaste de 21.")
            elif dealer_value > 21 or player_value > dealer_value:
                show_result("¡Ganaste!")
            elif player_value < dealer_value:
                show_result("¡Perdiste!")
            else:
                show_result("¡Es un empate!")
        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_h:  # Pedir carta
                        player_hand.append(deal_card())
                        if calculate_hand_value(player_hand) > 21:
                            game_over = True
                    elif event.key == pygame.K_s:  # Plantarse
                        player_standing = True
                        while dealer_value < 17:
                            dealer_hand.append(deal_card())
                            dealer_value = calculate_hand_value(dealer_hand)
                        game_over = True

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
