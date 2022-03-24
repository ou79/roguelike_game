from typing import NoReturn, Optional
import tcod.event

from actions import Action, BumpAction, EscapeAction, MovementAction

class EventHandler(tcod.event.EventDispatch):
    def ev_quit(self, event: tcod.event.Quit) -> NoReturn:
        raise SystemExit()

    def ev_keydown(self, event: tcod.event.KeyDown) -> Optional[Action]: 
        action: Optional[Action] = None

        key = event.sym

        if key == tcod.event.K_UP:
            action = BumpAction(dx=0, dy=-1)
        elif key == tcod.event.K_DOWN:
            action = BumpAction(dx=0, dy=1)
        elif key == tcod.event.K_RIGHT:
            action = BumpAction(dx=1, dy=0)
        elif key == tcod.event.K_LEFT:
            action = BumpAction(dx=-1, dy=0)
        elif key == tcod.event.K_ESCAPE:
            action = EscapeAction() 

        # No valid key was pressed
        return action