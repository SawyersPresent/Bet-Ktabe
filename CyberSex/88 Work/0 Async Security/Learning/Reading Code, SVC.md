


|Access right|Description|
|---|---|
|**SC_MANAGER_ALL_ACCESS** (0xF003F)|Includes **STANDARD_RIGHTS_REQUIRED**, in addition to all access rights in this table.|
|**SC_MANAGER_CREATE_SERVICE** (0x0002)|Required to call the [**CreateService**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-createservicea) function to create a service object and add it to the database.|
|**SC_MANAGER_CONNECT** (0x0001)|Required to connect to the service control manager.|
|**SC_MANAGER_ENUMERATE_SERVICE** (0x0004)|Required to call the [**EnumServicesStatus**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-enumservicesstatusa) or [**EnumServicesStatusEx**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-enumservicesstatusexa) function to list the services that are in the database.  <br>Required to call the [**NotifyServiceStatusChange**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-notifyservicestatuschangea) function to receive notification when any service is created or deleted.|
|**SC_MANAGER_LOCK** (0x0008)|Required to call the [**LockServiceDatabase**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-lockservicedatabase) function to acquire a lock on the database.|
|**SC_MANAGER_MODIFY_BOOT_CONFIG** (0x0020)|Required to call the [**NotifyBootConfigStatus**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-notifybootconfigstatus) function.|
|**SC_MANAGER_QUERY_LOCK_STATUS** (0x0010)|Required to call the [**QueryServiceLockStatus**](https://learn.microsoft.com/en-us/windows/desktop/api/Winsvc/nf-winsvc-queryservicelockstatusa) function to retrieve the lock status information for the database.|


most of these most likely need local admin, for example creating a service, ALL access, Modifying the boot config most likely all need  local administrator




- g++ for c++ and better for cross compiling (so it doesnt only run on windows)
- cl is mainly for only windows applications
- `Hinstance` is mainly for GUI applications specifically for windows.



```
#ifndef UNICODE
#define UNICODE
#endif 

#include <windows.h>

// Automatically link required libraries for MSVC
LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam);

int main(HINSTANCE hInstance, HINSTANCE hPrevInstance, PWSTR pCmdLine, int nCmdShow)
{
    // Register the window class.
    const wchar_t CLASS_NAME[]  = L"Sample Window Class";
    
    WNDCLASS wc = { };

    wc.lpfnWndProc   = WindowProc;
    wc.hInstance     = hInstance;
    wc.lpszClassName = CLASS_NAME;

    RegisterClass(&wc);

    // Create the window.

    HWND hwnd = CreateWindowEx(
        0,                              // Optional window styles.
        CLASS_NAME,                     // Window class
        L"Learn to Program Windows",    // Window text
        WS_OVERLAPPEDWINDOW,            // Window style

        // Size and position
        CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT, CW_USEDEFAULT,

        NULL,       // Parent window    
        NULL,       // Menu
        hInstance,  // Instance handle
        NULL        // Additional application data
        );

    if (hwnd == NULL)
    {
        return 0;
    }

    ShowWindow(hwnd, nCmdShow);

    // Run the message loop.

    MSG msg = { };
    while (GetMessage(&msg, NULL, 0, 0) > 0)
    {
        TranslateMessage(&msg);
        DispatchMessage(&msg);
    }

    return 0;
}

LRESULT CALLBACK WindowProc(HWND hwnd, UINT uMsg, WPARAM wParam, LPARAM lParam)
{
    switch (uMsg)
    {
    case WM_DESTROY:
        PostQuitMessage(0);
        return 0;

    case WM_PAINT:
        {
            PAINTSTRUCT ps;
            HDC hdc = BeginPaint(hwnd, &ps);

            // All painting occurs here, between BeginPaint and EndPaint.

            FillRect(hdc, &ps.rcPaint, (HBRUSH) (COLOR_WINDOW+1));

            EndPaint(hwnd, &ps);
        }
        return 0;

    }
    return DefWindowProc(hwnd, uMsg, wParam, lParam);
}
```