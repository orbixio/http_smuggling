// Compile command: gcc main.c -o main.exe -w
// Source: https://github.com/gatariee/exe2c_sh/blob/main/tests/src/calc/main.c
// ----------------------------------------------------------------

#include <windows.h>

int main()
{
    STARTUPINFO startupInfo;
    PROCESS_INFORMATION processInfo;
    ZeroMemory(&startupInfo, sizeof(startupInfo));
    ZeroMemory(&processInfo, sizeof(processInfo));

    startupInfo.cb = sizeof(startupInfo);

    if (CreateProcessW(L"C:\\Windows\\System32\\calc.exe", NULL, NULL, NULL, FALSE, 0, NULL, NULL, &startupInfo, &processInfo))
    {
        WaitForSingleObject(processInfo.hProcess, INFINITE);
        CloseHandle(processInfo.hProcess);
        CloseHandle(processInfo.hThread);
    }
    else {
        return -1;
    }

    return 0;
}