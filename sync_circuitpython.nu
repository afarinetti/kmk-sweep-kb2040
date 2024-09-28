#!/usr/bin/env nu

use std log

# Sync Python file changes in the current directory to the specified drive
def main [
    usb_drive: path # Path to the CircuitPython drive
] {
    if ($usb_drive | path exists) {
        watch . --glob=*.py { | op, path, new_path |
            log info $"($op) ---- ($path) ($new_path)"

            let filename = ($path | path basename)

            match $op {
                "Write" | "Create" => {
                    cp -vu $filename $usb_drive
                }
                "Rename" => {
                    let filename_new = ($new_path | path basename)
                    
                    let path_usb_old = ($usb_drive | path join $filename)
                    let path_usb_new = ($usb_drive | path join $filename_new)

                    mv -vu $path_usb_old $path_usb_new
                }
                # "Remove" => {
                #     let path_usb = ($usb_drive | path join $filename)
                #     if ($path_usb | path exists) {
                #         rm -v $path_usb
                #     } else {
                #         log warning $"Locally deleted file does not exist on USB drive: '($path_usb)'"
                #     }
                # }
                _ => {
                    log warning $"Operation '($op)' not yet implemented by script."
                }
            }
        }
    } else {
        log error $"Path '($usb_drive)' is not found."
    }
}
