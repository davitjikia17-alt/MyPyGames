# FIXED ADVANCED PYGAME CHESS
# --------------------------------
# FIXES:
# - Proper screen clearing
# - Correct checkmate winner
# - No ghost highlights
# - Better AI turn handling
# - Proper promotion logic
# - Stable move selection
# - Correct redraw order
# - Game-over display
# - Cleaner structure
#
# INSTALL:
# pip install pygame python-chess

import pygame
import chess
import random
import sys

pygame.init()

# ---------------- WINDOW ----------------








WIDTH = 720
HEIGHT = 720
SQ = WIDTH // 8

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fixed Pygame Chess")

clock = pygame.time.Clock()

# ---------------- COLORS ----------------

LIGHT = (240, 217, 181)
DARK = (181, 136, 99)
GREEN = (50, 220, 50)
RED = (220, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# ---------------- FONTS ----------------

FONT = pygame.font.SysFont("arial", 56)
SMALL = pygame.font.SysFont("arial", 32)

# ---------------- BOARD ----------------

board = chess.Board()

# ---------------- PIECES ----------------

pieces = {
    "P": "♙",
    "R": "♖",
    "N": "♘",
    "B": "♗",
    "Q": "♕",
    "K": "♔",
    "p": "♟",
    "r": "♜",
    "n": "♞",
    "b": "♝",
    "q": "♛",
    "k": "♚",
}

# ---------------- GAME STATE ----------------

selected_square = None
legal_moves = []

game_over = False
winner_text = ""

# ---------------- FUNCTIONS ----------------

def draw_board():
    for row in range(8):
        for col in range(8):

            color = LIGHT if (row + col) % 2 == 0 else DARK

            pygame.draw.rect(
                screen,
                color,
                (col * SQ, row * SQ, SQ, SQ)
            )

            square = chess.square(col, 7 - row)

            # Selected square highlight
            if square == selected_square:
                pygame.draw.rect(
                    screen,
                    GREEN,
                    (col * SQ, row * SQ, SQ, SQ),
                    5
                )

            # Legal move indicators
            for move in legal_moves:
                if move.to_square == square:
                    pygame.draw.circle(
                        screen,
                        RED,
                        (col * SQ + SQ // 2,
                         row * SQ + SQ // 2),
                        12
                    )

            piece = board.piece_at(square)

            if piece:
                text = FONT.render(
                    pieces[piece.symbol()],
                    True,
                    BLACK
                )

                rect = text.get_rect(
                    center=(
                        col * SQ + SQ // 2,
                        row * SQ + SQ // 2
                    )
                )

                screen.blit(text, rect)

def draw_status():
    if board.is_check() and not game_over:
        text = SMALL.render("CHECK!", True, RED)
        screen.blit(text, (10, 10))

    if game_over:
        overlay = pygame.Surface((WIDTH, HEIGHT))
        overlay.set_alpha(180)
        overlay.fill((0, 0, 0))
        screen.blit(overlay, (0, 0))

        text = FONT.render(winner_text, True, WHITE)

        rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))

        screen.blit(text, rect)

def get_square(mouse_pos):
    x, y = mouse_pos

    col = x // SQ
    row = y // SQ

    return chess.square(col, 7 - row)

def get_legal_moves(square):
    return [
        move for move in board.legal_moves
        if move.from_square == square
    ]

def make_move(move):
    global game_over
    global winner_text

    board.push(move)

    if board.is_checkmate():
        game_over = True

        if board.turn == chess.WHITE:
            winner_text = "BLACK WINS!"
        else:
            winner_text = "WHITE WINS!"

    elif board.is_stalemate():
        game_over = True
        winner_text = "STALEMATE"

def ai_move():
    if game_over:
        return

    moves = list(board.legal_moves)

    if not moves:
        return

    # Simple AI
    move = random.choice(moves)

    make_move(move)

# ---------------- MAIN LOOP ----------------

running = True

while running:

    clock.tick(60)

    screen.fill(BLACK)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if (
            event.type == pygame.MOUSEBUTTONDOWN
            and not game_over
        ):

            # Human = White
            if board.turn == chess.WHITE:

                clicked_square = get_square(
                    pygame.mouse.get_pos()
                )

                piece = board.piece_at(clicked_square)

                # Selecting piece
                if selected_square is None:

                    if (
                        piece
                        and piece.color == chess.WHITE
                    ):

                        selected_square = clicked_square
                        legal_moves = get_legal_moves(
                            clicked_square
                        )

                # Making move
                else:

                    chosen_move = None

                    for move in legal_moves:
                        if move.to_square == clicked_square:
                            chosen_move = move
                            break

                    if chosen_move:

                        moving_piece = board.piece_at(
                            chosen_move.from_square
                        )

                        # Promotion fix
                        if (
                            moving_piece
                            and moving_piece.symbol() == "P"
                            and chess.square_rank(
                                chosen_move.to_square
                            ) == 7
                        ):

                            chosen_move = chess.Move(
                                chosen_move.from_square,
                                chosen_move.to_square,
                                promotion=chess.QUEEN
                            )

                        make_move(chosen_move)

                        # AI TURN
                        if (
                            not game_over
                            and board.turn == chess.BLACK
                        ):
                            ai_move()

                    # Reset selection
                    selected_square = None
                    legal_moves = []

    draw_board()
    draw_status()

    pygame.display.flip()

pygame.quit()
sys.exit()