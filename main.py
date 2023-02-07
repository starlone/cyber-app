import urwid

__title__ = 'CyberAPP'

def get_body_base(text):
    return [urwid.Text(__title__ + text), urwid.Divider()]



def main_menu():
    body = get_body_base('')

    button = urwid.Button("Chat")
    urwid.connect_signal(button, 'click', chat_chosen)
    body.append(urwid.AttrMap(button, None, focus_map='reversed'))

    button = urwid.Button("Exit")
    urwid.connect_signal(button, 'click', exit_program)
    body.append(urwid.AttrMap(button, None, focus_map='reversed'))

    return urwid.ListBox(urwid.SimpleFocusListWalker(body))


def chat_chosen(button):
    body = get_body_base(' - Chat')

    b_server = urwid.Button(u'Server')
    server = urwid.AttrMap(b_server, None, focus_map='reversed')
    urwid.connect_signal(b_server, 'click', back_chosen)
    body.append(server)

    b_client = urwid.Button(u'Client')
    client = urwid.AttrMap(b_client, None, focus_map='reversed')
    urwid.connect_signal(b_client, 'click', back_chosen)
    body.append(client)

    b_back = urwid.Button(u'Back')
    back = urwid.AttrMap(b_back, None, focus_map='reversed')
    urwid.connect_signal(b_back, 'click', back_chosen)
    body.append(back)

    main.original_widget = urwid.ListBox(urwid.SimpleFocusListWalker(body))


def back_chosen(button):
    body = main_menu()
    main.original_widget = body


def exit_program(button):
    raise urwid.ExitMainLoop()


def exit_on_q(key):
    if key in ('q', 'Q'):
        raise urwid.ExitMainLoop()


listBox = main_menu()


main = urwid.Padding(listBox, left=2, right=2)
top = urwid.Overlay(main, urwid.SolidFill(u'\N{MEDIUM SHADE}'),
                    align='center', width=('relative', 60),
                    valign='middle', height=('relative', 60),
                    min_width=20, min_height=9)


loop = urwid.MainLoop(
    top, palette=[('reversed', 'standout', '')], unhandled_input=exit_on_q)
loop.run()
