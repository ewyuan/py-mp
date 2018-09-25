import threading
import vlc
from .player import Player
from .helper import handle_inputs


def main():
    player = Player()
    input_thread = threading.Thread(target=handle_inputs, args=(player,))
    input_thread.start()
    while True:
        if player.get_state().value == vlc.State.Ended and player.get_queue_size() > 0:
            player.play_next()
        if threading.active_count() != 2:
            break


if __name__ == "__main__":
    main()
