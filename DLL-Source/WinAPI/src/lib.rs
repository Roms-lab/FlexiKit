#![no_std]

use windows_sys::Win32::UI::WindowsAndMessaging::MessageBoxW;
use core::panic::PanicInfo;

#[unsafe(no_mangle)]
pub unsafe extern "C" fn DisplayMessage(text: *const u16, title: *const u16, id: u32) {
    unsafe {
        MessageBoxW(
            core::ptr::null_mut(), 
            text, 
            title, 
            id
        );
    }
}

#[panic_handler]
fn panic(_info: &PanicInfo) -> ! {
    loop {}
}