# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# define timeout for multipurpose_modmap
define_timeout(1)

# [Global modemap] Change modifier keys as in xmodmap
define_modmap({
    Key.CAPSLOCK: Key.RIGHT_CTRL
})

# # [Conditional modmap] Change modifier keys in certain applications
# define_conditional_modmap(re.compile(r'Emacs'), {
#     Key.RIGHT_CTRL: Key.ESC,
# })

# [Multipurpose modmap] Give a key two meanings. A normal key when pressed and
# released, and a modifier key when held down with another key. See Xcape,
# Carabiner and caps2esc for ideas and concept.
define_multipurpose_modmap(
    # Enter is enter when pressed and released. Control when held down.
    {Key.ENTER: [Key.ENTER, Key.RIGHT_CTRL]}

    # Capslock is escape when pressed and released. Control when held down.
    # {Key.CAPSLOCK: [Key.ESC, Key.LEFT_CTRL]
    # To use this example, you can't remap capslock with define_modmap.
)

# HandS (変換/無変換 and Space) Keys
define_multipurpose_modmap({
    Key.MUHENKAN: [Key.MUHENKAN, Key.LEFT_SHIFT],
    Key.HENKAN: [Key.HENKAN, Key.RIGHT_SHIFT]
})

# [Conditional multipurpose modmap] Multipurpose modmap in certain conditions,
# such as for a particular device.
define_conditional_multipurpose_modmap(lambda wm_class, device_name: device_name.startswith("Microsoft"), {
   # Left shift is open paren when pressed and released.
   # Left shift when held down.
   Key.LEFT_SHIFT: [Key.KPLEFTPAREN, Key.LEFT_SHIFT],

   # Right shift is close paren when pressed and released.
   # Right shift when held down.
   Key.RIGHT_SHIFT: [Key.KPRIGHTPAREN, Key.RIGHT_SHIFT]
})


# Keybindings for Firefox/Chrome
define_keymap(re.compile("Firefox|Google-chrome"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("RC-M-j"): K("C-TAB"),
    K("RC-M-k"): K("C-Shift-TAB"),
    # Type C-j to focus to the content
    K("RC-j"): K("C-f6"),
    # very naive "Edit in editor" feature (just an example)
    K("RC-o"): [K("C-a"), K("C-c"), launch(["gedit"]), sleep(0.5), K("C-v")]
}, "Firefox and Chrome")

# Keybindings for Zeal https://github.com/zealdocs/zeal/
define_keymap(re.compile("Zeal"), {
    # Ctrl+s to focus search area
    K("RC-s"): K("C-k"),
}, "Zeal")

emacs_like_apps = (
    "Emacs", "URxvt",
    "Gnome-terminal",
)

# Emacs-like keybindings in non-Emacs applications
define_keymap(lambda wm_class: wm_class not in emacs_like_apps, {
    # Cursor
    K("RC-b"): with_mark(K("left")),
    K("RC-f"): with_mark(K("right")),
    K("RC-p"): with_mark(K("up")),
    K("RC-n"): with_mark(K("down")),
    K("RC-h"): with_mark(K("backspace")),
    # Forward/Backward word
    K("M-b"): with_mark(K("C-left")),
    K("M-f"): with_mark(K("C-right")),
    # Beginning/End of line
    K("RC-a"): with_mark(K("home")),
    K("RC-e"): with_mark(K("end")),
    # Page up/down
    K("M-v"): with_mark(K("page_up")),
    K("RC-v"): with_mark(K("page_down")),
    # Beginning/End of file
    K("M-Shift-comma"): with_mark(K("C-home")),
    K("M-Shift-dot"): with_mark(K("C-end")),
    # Newline
    K("RC-m"): K("enter"),
    K("RC-j"): K("enter"),
    K("RC-o"): [K("enter"), K("left")],
    # Copy
    K("RC-w"): [K("C-x"), set_mark(False)],
    K("M-w"): [K("C-c"), set_mark(False)],
    K("RC-y"): [K("C-v"), set_mark(False)],
    # Delete
    K("RC-d"): [K("delete"), set_mark(False)],
    K("M-d"): [K("C-delete"), set_mark(False)],
    # Kill line
    K("RC-k"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Undo
    K("RC-slash"): [K("C-z"), set_mark(False)],
    K("RC-Shift-ro"): K("C-z"),
    # Mark
    K("RC-space"): set_mark(True),
    K("RC-M-space"): with_or_set_mark(K("C-right")),
    # Search
    K("RC-s"): K("F3"),
    K("RC-r"): K("Shift-F3"),
    K("M-Shift-key_5"): K("C-h"),
    # Cancel
    K("RC-g"): [K("esc"), set_mark(False)],
    # Escape
    K("RC-q"): escape_next_key,
    # C-x YYY
    K("RC-x"): {
        # C-x h (select all)
        K("h"): [K("C-home"), K("C-a"), set_mark(True)],
        # C-x C-f (open)
        K("RC-f"): K("C-o"),
        # C-x C-s (save)
        K("RC-s"): K("C-s"),
        # C-x k (kill tab)
        K("k"): K("C-f4"),
        # C-x C-c (exit)
        K("RC-c"): K("C-q"),
        # cancel
        K("RC-g"): pass_through_key,
        # C-x u (undo)
        K("u"): [K("C-z"), set_mark(False)],
    }
}, "Emacs-like keys")
