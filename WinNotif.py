from win10toast import ToastNotifier


def ntf(msg, title='notification', icon=''):
    toast = ToastNotifier()
    toast.show_toast(
    title,
    msg,
    duration = 20,
    icon_path = r"{}".format(icon),
    threaded = True)