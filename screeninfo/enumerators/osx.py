from screeninfo.common import Monitor


def enumerate():
    from pyobjus import autoclass
    from pyobjus.dylib_manager import load_framework, INCLUDE

    load_framework(INCLUDE.AppKit)

    screens = autoclass("NSScreen").screens()
    monitors = []

    for i in range(screens.count()):
        f = screens.objectAtIndex_(i).frame
        if callable(f):
            f = f()

        monitors.append(
            Monitor(f.origin.x, f.origin.y, f.size.width, f.size.height)
        )

    return monitors