import ctypes

# получить hwnd окна

enumWindows = ctypes.windll.user32.EnumWindows
enumWindowsProc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_int, ctypes.POINTER(ctypes.c_int))
getWindowText = ctypes.windll.user32.GetWindowTextW
getWindowTextLength = ctypes.windll.user32.GetWindowTextLengthW
isWindowVisible = ctypes.windll.user32.IsWindowVisible


def get_all_hwnds():
    wnd_list = []
    def foreach_window(hwnd, lparam):
        if ctypes.windll.user32.IsWindowVisible(hwnd) != 0:
            wnd_list.append(hwnd)
        return True
    enumWindows(enumWindowsProc(foreach_window), 0)

    return wnd_list

def getAllTitles():
    titles = []
    def foreach_window(hwnd, lparam):
        if isWindowVisible(hwnd):
            length = getWindowTextLength(hwnd)
            buff = ctypes.create_unicode_buffer(length + 1)
            getWindowText(hwnd, buff, length + 1)
            titles.append((hwnd, buff.value))
        return True
    enumWindows(enumWindowsProc(foreach_window), 0)
    return titles


def getWindowsWithTitle(title):
    hWndsAndTitles = getAllTitles()
    for hWnd, winTitle in hWndsAndTitles:
        if title.upper() in winTitle.upper():
            return hWnd            
    return False



wizard_hwnd = getWindowsWithTitle('VideoWizard')

if wizard_hwnd:
	print(wizard_hwnd)
else:
	print('VideoWizard is not found')
