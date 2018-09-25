import helper
import threading
from player import Player


def main():
    player = Player()
    input_thread = threading.Thread(target=helper.handle_inputs, args=(player,))
    input_thread.start()
    while True:
        if player.get_state().value == 6:
            player.play_next()
        if threading.active_count() != 2:
            break


if __name__ == "__main__":
    main()
