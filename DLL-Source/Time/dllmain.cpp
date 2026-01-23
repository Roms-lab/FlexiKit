// dllmain.cpp : Defines the entry point for the DLL application.
#include "pch.h"
#include <thread>
#include <chrono>

BOOL APIENTRY DllMain( HMODULE hModule,
                       DWORD  ul_reason_for_call,
                       LPVOID lpReserved
                     )
{
    switch (ul_reason_for_call)
    {
    case DLL_PROCESS_ATTACH:
    case DLL_THREAD_ATTACH:
    case DLL_THREAD_DETACH:
    case DLL_PROCESS_DETACH:
        break;
    }
    return TRUE;
}

extern "C" {
    __declspec(dllexport) void WaitSeconds(int Seconds) {
        std::this_thread::sleep_for(std::chrono::seconds(Seconds));
    }
    __declspec(dllexport) void WaitMinutes(int Minutes) {
        std::this_thread::sleep_for(std::chrono::minutes(Minutes));
    }
    __declspec(dllexport) void WaitMiliSeconds(int MiliSeconds) {
        std::this_thread::sleep_for(std::chrono::milliseconds(MiliSeconds));
    }
    __declspec(dllexport) void WaitMicroSeconds(int MicroSeconds) {
        std::this_thread::sleep_for(std::chrono::microseconds(MicroSeconds));
    }
    __declspec(dllexport) void WaitNanoSeconds(int NanoSeconds) {
        std::this_thread::sleep_for(std::chrono::nanoseconds(NanoSeconds));
    }
}